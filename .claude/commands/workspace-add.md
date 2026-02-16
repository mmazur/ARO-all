---
allowed-tools: Bash
---

Create a new workspace for working across multiple repos on a single feature.

## Parameters

- `$ARGUMENTS` contains: `<workspace> [repos...]`
  - `workspace` (required): the workspace name (e.g. `my-feature`). Used as both the directory name under `work/` and the branch suffix (`mmazur/<workspace>`).
  - `repos` (optional): space-separated list of repo directory names (e.g. `ARO-HCP release sdp-pipelines`). Defaults to `ARO-HCP ARO-Tools release` if not provided.

Parse `$ARGUMENTS` by splitting on whitespace. The first token is the workspace name. Any remaining tokens are repo names. If there are no remaining tokens, default to `ARO-HCP release`.

## Steps

1. **Validate** each requested repo directory exists under `/home/mmazur/aro/` and is a git repo (has a `.git` directory or file).
2. **Create** the workspace directory: `mkdir -p /home/mmazur/aro/work/<workspace>`
3. **Copy** CLAUDE.md to the new workspace directory at '/home/mmazur/aro/work/<workspace>'
3. **For each repo**, create a git worktree:
   ```
   git -C /home/mmazur/aro/<repo> worktree add /home/mmazur/aro/work/<workspace>/<repo> -b mmazur/<workspace> main
   ```
   The trailing `main` ensures the new branch starts from the `main` ref, regardless of the current checkout state or uncommitted changes in the base repo.
4. **Report** success or failure for each repo. If any repo fails, continue with the remaining repos and report all errors at the end.
