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
        # Try to get the current branch's upstream tracking info
        upstream_ref=$(git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null)

        if [ -n "$upstream_ref" ]; then
            # Extract branch name from upstream reference (format: remote/branch)
            branch_name="${upstream_ref#*/}"
            echo "  Switching to tracked branch: $branch_name"
            git checkout "$branch_name" && git pull
        else
            # Fallback: try to determine default branch from remotes
            # Check upstream first (for fork workflows), then origin
            default_branch=$(git symbolic-ref refs/remotes/upstream/HEAD 2>/dev/null | sed 's@^refs/remotes/upstream/@@')

            if [ -z "$default_branch" ]; then
                default_branch=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@')
            fi

            if [ -n "$default_branch" ]; then
                echo "  Switching to default branch: $default_branch"
                git checkout "$default_branch" && git pull
            else
                echo "  Could not determine default branch, pulling current branch"
                git pull
            fi
        fi
    ) || echo "Failed to update $repo_dir"
    echo ""
done
