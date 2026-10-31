# Git Command Cheat Sheet

## Setup

| Command | Purpose |
| --- | --- |
| `git --version` | Check the installed Git version |
| `git config --global user.name "Your Name"` | Set your Git username |
| `git config --global user.email "you@email.com"` | Set your Git email address |
| `git config --list` | Show Git configuration |

## Basic Workflow

| Command | Purpose |
| --- | --- |
| `git clone <repository-url>` | Download a repository from GitHub |
| `git status` | Show the status of files |
| `git add .` | Stage all changed files |
| `git commit -m "message"` | Save staged changes locally |
| `git push` | Upload local commits to GitHub |
| `git pull` | Download changes from GitHub |
| `git log --oneline` | Show commit history |

## Branching

| Command | Purpose |
| --- | --- |
| `git branch <branch-name>` | Create a new branch |
| `git checkout <branch-name>` | Switch to another branch |
| `git merge <branch-name>` | Merge a branch into the current branch |
