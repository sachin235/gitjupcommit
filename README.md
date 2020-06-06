# gitjupcommit

gitjupcommit is a jupyter notebook extension enabling users push ipython notebooks to a git repo.
The git button gets displayed in the notebook toolbar. After saving any notebook
the user can push notebook to pre-specified git repository. There are few
environment variables that must be exported. 
Feel free to use the extension and open issue if you face any problems, or wish to add some utility to the extension.

## Installation

You can currently install this directly from git. 
Use the following commands to install the extension.

```
pip install git+https://github.com/sachin235/gitjupcommit.git
jupyter serverextension enable --py gitjupcommit
jupyter nbextension install --py gitjupcommit --user

```

To enable this extension for all notebooks:

```
jupyter nbextension enable gitjupcommit --user --py 

```

## Steps

* Install package using the above commands
* Create Git repo (eg. gitjupyter) where notebooks will be pushed if not already exists and clone it in your `GIT_PARENT_DIR`
* Clone this repo as well in your `GIT_PARENT_DIR` directory
* `GIT_PARENT_DIR` refers to the `home` directory of your system
* Replace the values in env.sh present in this repo itself (as shown in the example below)
* Run the command `source ~/gitjupcommit/env.sh`
* Configure ssh key (present in ~/.ssh/id_rsa.pub or specified location) in the github account
* Run jupyter notebook from within your repo directory (eg. gitjupyter here)


## Example git configuration
export GIT_PARENT_DIR=~ <br />
export GIT_REPO_NAME=gitjupyter <br />
export GIT_BRANCH_NAME=master <br />
export GIT_USER=`<your GitHub username>` <br />
export GIT_EMAIL=`<your email linked with GitHub account>` <br />
export GITHUB_ACCESS_TOKEN=`<access-token from github developer settings>` <br />
export GIT_USER_UPSTREAM=`<your GitHub username>` <br />

<!-- ## Screenshots -->


<!-- ## Credits -->

<!-- Thanks to https://github.com/Lab41/sunny-side-up and https://github.com/sat28/githubcommit for laying the foundation of this extension. -->

