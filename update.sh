#!/bin/bash

# Find all subdirectories with .git folders and update them
for git_dir in */.git; do
    # Extract the repository directory name
    repo_dir="${git_dir%/.git}"

    # Skip if no .git directories found
    [ "$git_dir" = "*/.git" ] && break

    echo "Updating $repo_dir..."
    (
        cd "$repo_dir" || exit
        # Get the default branch name
        default_branch=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@')
        if [ -n "$default_branch" ]; then
            echo "  Switching to default branch: $default_branch"
            git checkout "$default_branch" && git pull
        else
            echo "  Could not determine default branch, pulling current branch"
            git pull
        fi
    ) || echo "Failed to update $repo_dir"
    echo ""
done
