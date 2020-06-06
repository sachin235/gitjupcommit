# gitjupcommit

gitjupcommit is a jupyter notebook extension enabling users push ipython notebooks to a git repo.
The git button gets displayed in the notebook toolbar. After saving any notebook
the user can push notebook to pre-specified git repository. There are few
environment variables that must be exported. Currently this extension supports
commits to a single github repo defined in environment variable but in the long
run need help to modify this extension allowing user to select his repo and branch.

## Installation

You can currently install this directly from git:

```
pip install git+https://github.com/sachin235/gitjupcommit.git
jupyter serverextension enable --py gitjupcommit
jupyter nbextension install --py gitjupcommit
```

To enable this extension for all notebooks:

```
jupyter nbextension enable --py gitjupcommit
```

## Steps

* Install package using above commands
* Create Git repo where notebooks will be pushed if not already exists and clone it in your `GIT_PARENT_DIR`
* Clone this repo as well in your `GIT_PARENT_DIR` directory
* Replace the values in env.sh present in this repo itself
* Run the command - source ~/gitjupcommit/env.sh
* Configure ssh key (present in ~/.ssh/id_rsa.pub or specified location) in github account
* Run jupyter notebook from within your repo directory

## Example git configuration
export GIT_PARENT_DIR=~ <br />
export GIT_REPO_NAME=gitjupyter <br />
export GIT_BRANCH_NAME=master <br />
export GIT_USER=sachin235 <br />
export GIT_EMAIL=<your email linked with GitHub account> <br />
export GITHUB_ACCESS_TOKEN=#access-token from github developer settings <br />
export GIT_USER_UPSTREAM=sachin235 <br />

<!-- ## Screenshots -->


<!-- ## Credits -->

<!-- Thanks to https://github.com/Lab41/sunny-side-up and https://github.com/sat28/githubcommit for laying the foundation of this extension. -->

