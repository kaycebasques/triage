#!/usr/bin/env python3
import sys
import os
import shutil
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: bazelisk run //scripts:sphinx -- <issue_number>")
        sys.exit(1)
    
    issue_num = sys.argv[1]
    if not issue_num.isdigit():
        print(f"Error: Issue number must be digits, got '{issue_num}'")
        sys.exit(1)
        
    # This script must be run via 'bazel run', which sets BUILD_WORKSPACE_DIRECTORY.
    workspace_dir_env = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
    if not workspace_dir_env:
        print("Error: This script must be run via bazel/bazelisk (e.g., 'bazelisk run //scripts:sphinx -- <issue_number>')")
        sys.exit(1)
    workspace_root = Path(workspace_dir_env)

    template_dir = workspace_root / "sphinx" / "template"
    target_dir = workspace_root / "sphinx" / issue_num

    if not template_dir.exists():
        print(f"Error: Template directory not found at {template_dir}")
        sys.exit(1)

    if target_dir.exists():
        print(f"Error: Target directory {target_dir} already exists")
        sys.exit(1)

    # Determine files to copy (skipping bazel-* symlinks/dirs)
    files_to_copy = []
    for item in template_dir.iterdir():
        if item.name.startswith("bazel-"):
            continue
        if item.is_file():
            files_to_copy.append(item)

    # Sort for consistent output
    files_to_copy.sort(key=lambda x: x.name)

    print("Files planned to copy:")
    for f in files_to_copy:
        print(f"  - {f.relative_to(workspace_root)}")

    print(f"\nCreating directory {target_dir.relative_to(workspace_root)}")
    target_dir.mkdir(parents=True, exist_ok=False)

    for src_path in files_to_copy:
        dest_path = target_dir / src_path.name
        print(f"Copying {src_path.name} -> {dest_path.relative_to(workspace_root)}")
        
        try:
            content = src_path.read_text(encoding='utf-8')
            new_content = content.replace("x2f8gp0", issue_num)
            dest_path.write_text(new_content, encoding='utf-8')
        except UnicodeDecodeError:
            # Fallback for binary files if any
            shutil.copy2(src_path, dest_path)

    print("Done.")

if __name__ == "__main__":
    main()
