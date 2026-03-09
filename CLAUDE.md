# Rules
## General
- Unless specified otherwise always focus answers and changes on the ARO HCP parts, even for repos that contain things not related to ARO HCP
- when referencing commits or PRs, always print a cliackable URL
- to fetch latest version of all repos, run ./update.sh; must be outside of sandbox

## Tools Use
- use `gh` for github interactions
- sdp-pipelines/ is ADO so `az devops`
- when running git against repos use 'git -C repo/ $command' for permissions reasons

# A list of repositories that might be present:
## Main repos
- ARO-HCP/ - primary github repo with most things
- ARO-Tools/ - github helper repo for the above
- sdp-pipelines/ - Azure DevOps repo that contains tooling and configs to deploy ARO HCP into microsoft environments using EV2; subdirs of most interest: hcp, tooling, .pipelines
- release/ - openshift CI config repo for running prow jobs, mostly gating/periodic/pull tests; of interest is mostly release/ci-operator/config/Azure/ARO-HCP/ and release/ci-operator/step-registry/aro-hcp/ paths

## Repos for upstream components
- aro-hcp-clusters-service/ - clusters service
- hypershift/ - hypershift operator

## For OpenShift CI / prow deep dives:
- ci-tools/ - openshift's CI tooling including the ci-operator
- ci-docs/ - documentation for OpenShift CI service
- prow/ - upstream prow source code
