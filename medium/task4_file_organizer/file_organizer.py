"""
Task 4: Safe File Organizer
Author: Himani Thakur
Description:
    Organizes files in a target directory into categorized subfolders
    (Images, Documents, Videos, Audio, Archives, and Others) based on their
    file extensions. Includes a Dry-Run preview mode, conflict avoidance,
    and strict directory boundary protections.
"""

import os
import shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv", ".odt", ".rtf"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
}

CATEGORY_FOLDERS = set(CATEGORIES.keys()) | {"Others"}


def get_category(filename: str) -> str:
    """Return the designated category name for a given filename based on its extension."""
    _, ext = os.path.splitext(filename)
    ext_lower = ext.lower()

    for category, extensions in CATEGORIES.items():
        if ext_lower in extensions:
            return category
    return "Others"


def get_safe_destination_path(destination_dir: str, filename: str) -> str:
    """
    Generate a safe file destination path that avoids overwriting existing files
    by appending an incremented numeric suffix (_1, _2, etc.) if needed.
    """
    dest_path = os.path.join(destination_dir, filename)
    if not os.path.exists(dest_path):
        return dest_path

    stem, ext = os.path.splitext(filename)
    counter = 1
    while True:
        new_name = f"{stem}_{counter}{ext}"
        new_dest_path = os.path.join(destination_dir, new_name)
        if not os.path.exists(new_dest_path):
            return new_dest_path
        counter += 1


def is_safe_target_directory(dir_path: str) -> tuple[bool, str]:
    """
    Validate that the directory exists and is NOT a root drive, system folder,
    or empty path.
    """
    if not dir_path or not dir_path.strip():
        return False, "Directory path cannot be empty."

    resolved = os.path.abspath(dir_path)

    if not os.path.exists(resolved):
        return False, f"Directory does not exist: '{resolved}'"

    if not os.path.isdir(resolved):
        return False, f"Path is not a directory: '{resolved}'"

    # Prevent root directory organization (e.g., C:\, /, D:\)
    parent = os.path.dirname(resolved)
    if parent == resolved or resolved in ("/", "\\", "C:\\", "c:\\"):
        return False, "Safety restriction: Cannot organize root drive directly."

    # Prevent dangerous system directories
    lower = resolved.lower()
    for dangerous in ("c:\\windows", "c:\\program files", "/usr", "/bin", "/etc"):
        if lower.startswith(dangerous):
            return False, f"Safety restriction: Cannot organize critical system folder '{resolved}'."

    return True, resolved


def organize_files(target_dir: str, dry_run: bool = True) -> list[dict]:
    """
    Scan the target directory and sort eligible files into category subdirectories.

    Parameters:
        target_dir (str): Absolute or relative path to the folder.
        dry_run (bool): If True, previews operations without modifying files.

    Returns:
        list[dict]: List of planned or executed move actions.
    """
    is_safe, resolved_dir = is_safe_target_directory(target_dir)
    if not is_safe:
        raise ValueError(resolved_dir)

    actions = []

    # Identify self script name to avoid accidentally moving this script if run locally
    current_script_name = os.path.basename(__file__)

    with os.scandir(resolved_dir) as entries:
        for entry in entries:
            # Skip subdirectories, including already created category folders
            if entry.is_dir():
                continue

            # Skip hidden/system files and the script itself
            if entry.name.startswith(".") or entry.name == current_script_name:
                continue

            # Determine category and destination
            category = get_category(entry.name)
            category_dir = os.path.join(resolved_dir, category)

            # Determine safe destination filename
            safe_dest_path = get_safe_destination_path(category_dir, entry.name)

            action_record = {
                "filename": entry.name,
                "source": entry.path,
                "category": category,
                "destination": safe_dest_path,
                "dry_run": dry_run,
            }

            if not dry_run:
                os.makedirs(category_dir, exist_ok=True)
                shutil.move(entry.path, safe_dest_path)
                action_record["status"] = "Moved"
            else:
                action_record["status"] = "Simulated"

            actions.append(action_record)

    return actions


def print_actions_summary(actions: list[dict], dry_run: bool):
    """Print a clean summary of file operations."""
    mode_text = "[DRY-RUN PREVIEW]" if dry_run else "[EXECUTION REPORT]"
    print("\n" + "=" * 65)
    print(f"        FILE ORGANIZER SUMMARY {mode_text}")
    print("=" * 65)

    if not actions:
        print("No loose files found to organize in the specified directory.")
        print("=" * 65)
        return

    for action in actions:
        dest_folder = os.path.basename(os.path.dirname(action['destination']))
        dest_filename = os.path.basename(action['destination'])
        print(f" - [{action['category']:<9}] {action['filename']} -> {dest_folder}/{dest_filename}")

    print("-" * 65)
    action_verb = "Proposed to organize" if dry_run else "Successfully organized"
    print(f"{action_verb}: {len(actions)} file(s).")
    print("=" * 65)


def main():
    print("=" * 60)
    print("              SAFE PYTHON FILE ORGANIZER              ")
    print("=" * 60)
    print("Organizes loose files into: Images, Documents, Videos,")
    print("Audio, Archives, and Others folders.")

    while True:
        folder = input("\nEnter target folder path (or 'q' to quit): ").strip()
        if folder.lower() in ("q", "quit", "exit"):
            print("Exiting File Organizer. Goodbye!")
            break

        is_safe, msg = is_safe_target_directory(folder)
        if not is_safe:
            print(f"[Error] {msg}")
            continue

        resolved_dir = msg
        print(f"\nAnalyzing directory: {resolved_dir}")

        # Step 1: Run dry-run preview first
        try:
            preview_actions = organize_files(resolved_dir, dry_run=True)
            print_actions_summary(preview_actions, dry_run=True)

            if not preview_actions:
                continue

            # Step 2: Request user confirmation before real move
            confirm = input("\nProceed with moving these files? (yes/no): ").strip().lower()
            if confirm in ("y", "yes"):
                executed_actions = organize_files(resolved_dir, dry_run=False)
                print_actions_summary(executed_actions, dry_run=False)
                print("Files organized safely!")
            else:
                print("Operation cancelled. No files were modified.")

        except Exception as e:
            print(f"[Error] Failed to organize files: {e}")

        again = input("\nOrganize another folder? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
