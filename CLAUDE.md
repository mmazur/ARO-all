A list of subdirectories that might be present (each one is used to develop and release ARO HCP):
- ARO-HCP/ - primary github repo with most things
- ARO-Tools/ - github helper repo for the above
- aro-hcp-clusters-service/ - upstream for the clusters service component
- sdp-pipelines/ - Azure DevOps repo that contains tooling and configs to deploy ARO HCP into microsoft environments using EV2; subdirs of most interest: hcp, tooling, .pipelines
- release/ - openshift CI config repo for running prow jobs, mostly gating/periodic/pull tests; of interest is mostly release/ci-operator/config/Azure/ARO-HCP/ and release/ci-operator/step-registry/aro-hcp/ paths
- ci-tools/ - openshift's CI tooling including the ci-operator
- ci-docs/ - documentation for OpenShift CI service
- prow/ - upstream prow source code

Rules:
- Unless specified otherwise always focus answers and changes on the ARO HCP parts, even for repos that contain things not related to ARO HCP
- when referencing github commits, always print a cliackable URL for that commits
- to fetch latest version of all repos, run ./update.sh; must be outside of sandbox

Tools:
- use `gh` for github interactions
- sdp-pipelines/ is ADO so `az devops`
- when running git against repos use 'git -C repo/ $command'
