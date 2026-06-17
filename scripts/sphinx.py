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
    def ignore_patterns(path, names):
        return [name for name in names if name.startswith("bazel-")]

    def copy_and_replace(src, dst):
        src_path = Path(src)
        dst_path = Path(dst)
        try:
            content = src_path.read_text(encoding='utf-8')
            new_content = content.replace("x2f8gp0", issue_num)
            dst_path.write_text(new_content, encoding='utf-8')
        except UnicodeDecodeError:
            shutil.copy2(src_path, dst_path)

    try:
        shutil.copytree(template_dir, target_dir, ignore=ignore_patterns, copy_function=copy_and_replace, dirs_exist_ok=False)
    except FileExistsError:
        print(f"Error: Target directory {target_dir} already exists.")
        sys.exit(1)



if __name__ == "__main__":
    main()
