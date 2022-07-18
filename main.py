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
    - **checkout <commit id>: show file at commit stage. changes won't be saved
    - revert <commit id>: show and undo changes at commit. a text editor window to edit
            commit message is given. to exit use>> :wq >>press 'enter' 
    - reset <commit id>: delete all commits after specified commit but changes in files
            are not reset
    - reset <commit id> --hard: delete all commits after plus file changes 
"""