import sys
import os
import shutil
from pathlib import Path


def usage():
    print("Usage: bazelisk run //scripts:sphinx -- <issue_number>")


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    issue_num = sys.argv[1]
    if not issue_num.isdigit():
        usage()
        sys.exit(1)
    workspace_dir_env = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
    if not workspace_dir_env:
        usage()
        sys.exit(1)
    workspace_root = Path(workspace_dir_env)
    template_dir = workspace_root / "sphinx" / "template"
    target_dir = workspace_root / "sphinx" / issue_num
    files_to_copy = []
    for root, dirs, files in os.walk(template_dir):
        # Exclude bazel-* directories from walk
        dirs[:] = [d for d in dirs if not d.startswith("bazel-")]
        for file in files:
            if file.startswith("bazel-"):
                continue
            src_path = Path(root) / file
            rel_path = src_path.relative_to(template_dir)
            files_to_copy.append((src_path, rel_path))
    files_to_copy.sort(key=lambda x: x[1])
    target_dir.mkdir(parents=True, exist_ok=False)
    for src_path, rel_path in files_to_copy:
        dest_path = target_dir / rel_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            content = src_path.read_text(encoding='utf-8')
            new_content = content.replace("x2f8gp0", issue_num)
            dest_path.write_text(new_content, encoding='utf-8')
        except UnicodeDecodeError:
            # Fallback for binary files if any
            shutil.copy2(src_path, dest_path)


if __name__ == "__main__":
    main()
