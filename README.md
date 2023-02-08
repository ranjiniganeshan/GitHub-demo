# GitHub Demo


This is a demo for Git workflow, which scans all repositories in an organization and performs various checks, such as verifying that a team has been added and that a pull request has been reviewed before merging to the master branch. The code generates a table with the organization and repository name, and only considers the master branch and ignores other branches.

# Steps to Run the Code

Clone the repository:
```
git clone [repository_url]
```

## Create a personal access token on GitHub:
In the upper-right corner of any page, click your profile photo.
Click Settings.
In the left sidebar, click Developer settings.
In the left sidebar, click Personal access tokens.
Click Generate new token.
Give your token a descriptive name.

## Requirements
* This code requires a GitHub token.
* Python 3 to be installed

## Running the Python Code

Install Python 3
Run the code:
```
python3 github.py
```
## Install the required library
```
pip3 install pygithub
pip3 install prettytable
```


