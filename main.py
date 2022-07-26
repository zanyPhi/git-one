def git_message():
    print("you're commited to the right path")

git_message()

"""Git commands

- cmd commands:
    - cd <filepath> :move to directory
    - mkdir <filename/foldername>: create a file or directory
    - rm <filename/foldername>: remove file or directory
    - rmdir <filename>: remove file or directory
    - touch <filenaem> (cmder/linux/mac): create a file or directory

- git:
    - --version: check git version if installed
    - config --global init.defaultBranch main: set default branch to main
    - branch -m <branchname>: rename master branch
    - config --global user.name <username>: add username
    - config --global user.email <email>: add user email
    - init: create new repository
    - status: check whether files are untracked, staged or commited
    - add: stage files
    - add . : stage all files in a repo
    - rm --cached <filename>: unstage file
    - commit -m "<message/commit details>": commit staged files with a message
    - log: show commit history
    - log --oneline: show "concise" commit history
    - *checkout <commit id>: show file at commit stage. changes won't be saved
    - revert <commit id>: show and undo changes at commit. a text editor 
        window to edit commit message is given. to exit use>> :wq >>press
        'enter' 
    - reset <commit id>: delete all commits after specified commit but changes
        in files are not reset
    - reset <commit id> --hard: delete all commits after plus file changes 
     - branch <branchname>: create a branch
    - branch -a: list all branches
    - checkout <branchname>: switch to <branchname>
    - branch -d <branchname>: delete merged branch
    - branch -D <branchname>: delete unmerged branch
    - checkout -b <branchname>: create and switch to branch
    - merge <branchname>: you must be on main(master) branch to merge
    - push <remote repo path> <branchname>: to push to remote repo o github
    - remote add <alias> <remote repo path>: create alias for remote repo path
    - push <alias> <branchname>: push to remote
    - clone <remote repo path>: create a local repo from github. will create
        folder with repository name

    (Collaboration workflow)
    - pull origin <branch>: update cloned repo
    - create new branch
    - stage, commit
    - push branch, not main
    - compare and create pull request(to merge with master branch)


    (Contribution workflow)
    - fork on github to your account
    - clone forked repo
    - stage, commit
    - push main on origin
    - create pull request
    - only author can merge
"""