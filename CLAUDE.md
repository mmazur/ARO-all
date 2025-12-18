There are multiple subdirectories here. Each one is required to develop and release ARO HCP:
- ARO-HCP/ - base repo with most of the stuff
- ARO-Tools/ - helper for the above
- sdp-pipelines/ - Azure DevOps repo that contains tooling and configs to deploy ARO HCP into microsoft environments using EV2
- release/ - openshift CI config repo for running prow jobs, mostly gating/periodic/pull tests; of interest is mostly release/ci-operator/config/Azure/ARO-HCP/ and release/ci-operator/step-registry/aro-hcp/
