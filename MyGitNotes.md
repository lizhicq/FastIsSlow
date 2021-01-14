# Git show log tree
$git log --graph --decorate --pretty=oneline --abbrev-commit

# master merge feature
$git checkout master
$git merge feature

#feature rebase onto master
$git checkout feature
$git reabse master
$#resolve conflicts
$git add . # reslove 