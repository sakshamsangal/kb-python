# git commands

## git editor

git config --global core.editor "'E:/Microsoft VS Code/Code.exe' -w"

## delete branch locally

git branch -d localBranchName

## delete branch remotely

git push origin --delete remoteBranchName

## For me, the most secure way is to use the update-ref command:

git update-ref -d HEAD

## rebase

git rebase -i --root master

## terminal

"terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe"

## url

git push https://github.com/sakshamsangal/springFramework.git

## switch branch

git checkout [branch_name]

## make a new branch and switch to it

$ git checkout -b [name_of_your_new_branch]

## Set your username:

git config --global user.name "Deepika Padukone"

## Set your email address:

git config --global user.email "deepika@gmail.com"

## You can view all of your settings and where they are coming from using:

git config --list --show-origin

## for reference

https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

## install git

```
Make sure Use Git from Git Bash Only.

make git terminal as default terminal in intellij ide.
Go to settings >> Tools >> terminal
Set the path of git bash.exe
e.g. E:\Git\bin\bash.exe

Now run git commands from terminal in the intellij IDE.
```