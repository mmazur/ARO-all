---
allowed-tools: Bash
---

Create a new workspace for working across multiple repos on a single feature.

## Parameters

- `$ARGUMENTS` contains: `<workspace> [repos...]`
  - `workspace` (required): the workspace name (e.g. `my-feature`). Used as both the directory name under `work/` and the branch suffix (`mmazur/<workspace>`).
  - `repos` (optional): space-separated list of repo directory names (e.g. `ARO-HCP release sdp-pipelines`). Defaults to `ARO-HCP ARO-Tools release` if not provided.

## Steps

1. **Execute** the workspace-add.py script with the provided arguments:
   ```
   /home/mmazur/aro/.claude/scripts/workspace-add.py $ARGUMENTS
   ```

The script will:
- Validate each requested repo directory exists and is a git repo
- Create the workspace directory under `/home/mmazur/aro/work/<workspace>`
- Copy CLAUDE.md to the new workspace directory
- Create git worktrees for each repo with branch `mmazur/<workspace>` based on `main`
- Report success or failure for each repo
