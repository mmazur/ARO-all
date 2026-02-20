#!/usr/bin/env python3
"""
Create a new workspace for working across multiple repos on a single feature.

Usage:
    workspace-add.py <workspace> [repos...]

Arguments:
    workspace: the workspace name (e.g. my-feature). Used as both the directory
               name under work/ and the branch suffix (mmazur/<workspace>).
    repos:     space-separated list of repo directory names (e.g. ARO-HCP release).
               Defaults to: ARO-HCP ARO-Tools release
"""

import sys
import os
import shutil
import subprocess
from pathlib import Path

BASE_DIR = Path("/home/mmazur/aro")
WORK_DIR = BASE_DIR / "work"
DEFAULT_REPOS = ["ARO-HCP", "ARO-Tools", "release"]
CLAUDE_MD = BASE_DIR / "CLAUDE.md"


def validate_repo(repo_path: Path) -> bool:
    """Check if directory exists and is a git repo."""
    if not repo_path.exists():
        return False
    git_dir = repo_path / ".git"
    return git_dir.exists()


def create_workspace(workspace: str, repos: list[str]) -> int:
    """
    Create a workspace with git worktrees for specified repos.

    Returns:
        0 on success, 1 if any errors occurred
    """
    errors = []

    # Validate all repos first
    print(f"Validating repos: {', '.join(repos)}")
    for repo in repos:
        repo_path = BASE_DIR / repo
        if not validate_repo(repo_path):
            errors.append(f"❌ {repo}: not found or not a git repo at {repo_path}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    # Create workspace directory
    workspace_dir = WORK_DIR / workspace
    print(f"\nCreating workspace directory: {workspace_dir}")
    workspace_dir.mkdir(parents=True, exist_ok=True)

    # Copy CLAUDE.md if it exists
    if CLAUDE_MD.exists():
        dest_claude_md = workspace_dir / "CLAUDE.md"
        print(f"Copying {CLAUDE_MD} to {dest_claude_md}")
        shutil.copy2(CLAUDE_MD, dest_claude_md)
    else:
        print(f"Warning: {CLAUDE_MD} not found, skipping copy")

    # Create worktrees
    print(f"\nCreating worktrees for branch: mmazur/{workspace}")
    for repo in repos:
        repo_path = BASE_DIR / repo
        worktree_path = workspace_dir / repo
        branch_name = f"mmazur/{workspace}"

        try:
            # git -C <repo> worktree add <worktree_path> -b <branch> main
            cmd = [
                "git", "-C", str(repo_path),
                "worktree", "add",
                str(worktree_path),
                "-b", branch_name,
                "main"
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )

            print(f"✓ {repo}: worktree created at {worktree_path}")

        except subprocess.CalledProcessError as e:
            error_msg = f"✗ {repo}: failed to create worktree"
            if e.stderr:
                error_msg += f"\n  {e.stderr.strip()}"
            errors.append(error_msg)
            print(error_msg, file=sys.stderr)

    # Summary
    print(f"\n{'='*60}")
    if errors:
        print(f"Workspace created with {len(errors)} error(s)")
        return 1
    else:
        print(f"✓ Workspace '{workspace}' created successfully at {workspace_dir}")
        print(f"  Branch: mmazur/{workspace}")
        print(f"  Repos: {', '.join(repos)}")
        return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 1

    workspace = sys.argv[1]
    repos = sys.argv[2:] if len(sys.argv) > 2 else DEFAULT_REPOS

    return create_workspace(workspace, repos)


if __name__ == "__main__":
    sys.exit(main())
