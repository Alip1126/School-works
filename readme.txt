Microsoft Windows [Version 10.0.19042.1165]
(c) Microsoft Corporation. All rights reserved.

C:\Users\moonl>cd desktop

C:\Users\moonl\Desktop> cd \Users\moonl\.spyder-py3\schoolwork

C:\Users\moonl\.spyder-py3\schoolwork>git init
Initialized empty Git repository in C:/Users/moonl/.spyder-py3/schoolwork/.git/

C:\Users\moonl\.spyder-py3\schoolwork>repo/readme.txt
'repo' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\moonl\.spyder-py3\schoolwork>touch repo/readme.txt
'touch' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\moonl\.spyder-py3\schoolwork>git commit
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'moonl@DESKTOP-HAOI4AK.(none)')

C:\Users\moonl\.spyder-py3\schoolwork>git config --global user.email "moonligh1738@gmail.com"

C:\Users\moonl\.spyder-py3\schoolwork>git config --global user.name "Alip"

C:\Users\moonl\.spyder-py3\schoolwork>git commit
On branch master

Initial commit

nothing to commit (create/copy files and use "git add" to track)

C:\Users\moonl\.spyder-py3\schoolwork>git add readme.txt
fatal: pathspec 'readme.txt' did not match any files

C:\Users\moonl\.spyder-py3\schoolwork>git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Turn this message off by running
hint: "git config advice.addEmptyPathspec false"

C:\Users\moonl\.spyder-py3\schoolwork>git add readme.txt

C:\Users\moonl\.spyder-py3\schoolwork>git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.txt


C:\Users\moonl\.spyder-py3\schoolwork>git commit -m "added readme.txt"
[master (root-commit) 438cc11] added readme.txt
 1 file changed, 1 insertion(+)
 create mode 100644 readme.txt

C:\Users\moonl\.spyder-py3\schoolwork>git status
On branch master
nothing to commit, working tree clean

C:\Users\moonl\.spyder-py3\schoolwork>git remote add origin https://github.com/Alip1126/School-works.git

C:\Users\moonl\.spyder-py3\schoolwork>git checkout master
Already on 'master'

C:\Users\moonl\.spyder-py3\schoolwork>git push -u origin master
info: please complete authentication in your browser...
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 217 bytes | 108.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Alip1126/School-works.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.

C:\Users\moonl\.spyder-py3\schoolwork>git add .

C:\Users\moonl\.spyder-py3\schoolwork>git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   PongPongGame.py
        new file:   linear_equation.py
        new file:   p707_recursion.py
        new file:   r_tip_calc.py
        new file:   rational_num_class.py
        new file:   student_class.py


C:\Users\moonl\.spyder-py3\schoolwork>git commit -m "added multiple school works and mini programs"
[master e906d54] added multiple school works and mini programs
 6 files changed, 777 insertions(+)
 create mode 100644 PongPongGame.py
 create mode 100644 linear_equation.py
 create mode 100644 p707_recursion.py
 create mode 100644 r_tip_calc.py
 create mode 100644 rational_num_class.py
 create mode 100644 student_class.py

C:\Users\moonl\.spyder-py3\schoolwork>git push
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 4 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 6.76 KiB | 3.38 MiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Alip1126/School-works.git
   438cc11..e906d54  master -> master

C:\Users\moonl\.spyder-py3\schoolwork>
