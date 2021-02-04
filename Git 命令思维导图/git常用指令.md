git常用指令总结
原创White Coco 最后发布于2019-06-03 17:15:36 阅读数 133  收藏


创建裸仓库:
$ git init --bare
仓库于裸仓库之间的转换：

$ git clone --bare
展开
1. git环境设置
设置账户信息
git config user.name
git config user.email
git config --global user.name "name"
git config --global user.email "email"
git config --list
1
2
3
4
5
生成ssh key
ssh-keygen  -t  rsa  -C  "mail"
cat ~/.ssh/id_rsa.pub
1
2
将ssh key拷贝到gerrit链接或者github。

基本配置更新
gedit  ~/.gedit .cshrc.user
source gitenv.csh
git submodule update
1
2
3
图形化操作
gitgui &
gitk &
1
2
复制repo
git clone <link>
1
2. branch操作
创建分支
git checkout -b branch // Create a new branch
git branch  // Check local branch
git branch -v // Check all local branch and the head information
git branch -vv // Check all local branch and upstream branch
git branch -a  // Check all branch
git branch -av  // Check all branch  and the head information
1
2
3
4
5
6
删除分支
git branch –m oldbranch newbranch  // Modify branch
git branch –D branch  // Delete local branch
1
2
建立远端分支
git push origin branchname:branchname  // Create a new origin branch
git branch --set-upstream branchname origin/branchname  // Set upstream branch
git branch -r |grep branchname  origin/feat/branchname  // Find branch on remote

git remote show origin // Check remote origin branch
git remote prune origin // Update remote origin branch and local branch
1
2
3
4
5
6
3. commit 操作
文件状态操作
git status  // Check git tree, what changed currently
git log  // Check the commit history
git diff  // Check changed files
git patch > patch.diff  // Create a patch
patch -p1 <patch.diff  // Patch on branch
1
2
3
4
5
添加删除文件
git add <file>  // Add changed files to local git stage
git add.  // Add all changed files to local git stage
git mv <old> <new> // Rename for file
git rm <file>  // Remove some files for current stage
1
2
3
4
增加注释
git commit <file>  // Commit files, Input comments
git commit –a  // Commit all files not git-add, Input comments
git commit –a –m “your comments” // Commit with comment, not suggest
git commit --amend  // Amend commit to last one 
1
2
3
4
push到远端分支
git push origin master // Push to remote repo master branch
git push origin HEAD --force // Pusch commit by force
git push origin HEAD:refs/for/master  // Push commit for review
git push origin HEAD:refs/for/master  --no-verify // Push on master branch bypass pre-push hook
git push origin HEAD:refs/for/personal/ezyunch/branch  // Push commit on personal branch
1
2
3
4
5
commit 更新
git fetch  // Fetch changes but no merge
git merge master  // Merge master to current devel branch
git pull  // this command = git fetch + git merge
1
2
3
解决冲突，Cherry-pick
git cherry-pick <commit id>  // Fetch one commit to local
git cherry-pick <commit id1^..id2>  // Fetch some commits to local
git cherry-pick --quit
git cherry-pick --continue
git cherry-pick --abort
1
2
3
4
5
解决冲突，git rebase
git rebase -i HEAD~4
git rebase -i <commit id>
git rebase –continue  # After problem resolved
git rebase –skip          # Skip this conflict patch
git rebase –abort       # Check out the original branch and stop rebasing
1
2
3
4
5
checkout 和 clean操作
git checkout -- // undo all changes in repo files
git checkout -f  // force checkout (throw away local modifications)
git clean –dfx // clean all ignores files  
1
2
3
其它
git reset --hard  // Revert local branch same as remote 
git reset --hard <commit id>  // Revert to the commit id
git push origin HEAD --force  // used with caution
git reset --hard commit id
1
2
3
4
git config
??git config命令的作用是配置git的相关信息。

配置全局的用户名和邮箱，mac下可通过终端输入命令cat ~/.gitconfig查看配置信息。
设置用户名：git config --global user.name "name"
设置用户邮箱：git config --global user.email "eamil"
针对单个仓库配置用户名和邮箱，mac下可通过终端进入到项目的根目录中，然后输入命令cat .git/config查看配置信息。
设置用户名：git config user.name "name"
设置用户邮箱：git config user.email "eamil"
查看git所有配置信息：git config --list
查看配置的用户名：git config user.name
查看配置的用户邮箱：git config user.email
定义命令别名：
git config --global alias.st status：则git status可用git st代替
git config --global alias.co checkout：则git checkout可用git co代替
git config --global alias.ci commit：则git commit可用git ci代替
git config --global alias.br branch：则git branch可用git br代替
也可以自定义其他命令的别名，主要合理且方便操作即可。

git init
??git init命令的作用是在当前目录中初始化仓库，并且创建一个名为.git的子目录，该目录含有你初始化的Git仓库中所有的必须文件。

git status
??git status命令的作用是显示文件状态，红色表示工作目录的文件被修改但还没有提交到暂存区，绿色表示已经提交到暂存区。

以极简的方式显示文件状态：git status -s
A：本地新增的文件（服务器上没有）
C：文件的一个新拷贝
D：本地删除的文件（服务器上还在）
M：红色为修改过未被添加进暂存区的，绿色为已经添加进暂存区的
R：文件名被修改
T：文件的类型被修改
U：文件没有被合并(你需要完成合并才能进行提交)
X：未知状态(很可能是遇到git的bug了，你可以向git提交bug report)
?：未被git进行管理，可以使用git add fileName把文件添加进来进行管理
已经被修改但还没提交到暂存区的文件，可以通过命令git checkout -- fileName撤销更改。

git add
??git add命令的作用是将文件从工作目录添加至暂存区

把所有修改的信息添加到暂存区：git add .
把所有跟踪文件中被修改过或已删除的文件信息添加至暂存区：git add -u或git add --update，它不会处理那些没有被跟踪的文件
把所有跟踪文件中被修改过或已删除文件和所有未跟踪的文件信息添加到暂存区：git add -A或git add --all
注意：git add .和git add -A在2.x版本中提交类型方面功能相同，但会因为所在目录不同产生差异：

git add .只会提交当前目录或者子目录下相应文件。
git add -A无论在哪个目录执行都会提交相应文件。
已经被提交到暂存区的文件，可以通过命令git reset HEAD -- fileName撤销提交。

git commit
??git commit命令的作用是将暂存区的修改提交到本地仓库，同时会生成一个commmit-id。

将暂存区的修改提交到本地仓库：git commit -m "message"，"message"是本次提交的简述内容，比如添加新功能或修复bug等
将本地工作区中修改后还未使用git add .命令添加到暂存区中的文件也提交到本地仓库：git commit –a –m "message"，该命令相当于以下两条命令：
git add .：把所有修改的信息添加到暂存区
git add -m "message"：将暂存区的修改提交到本地仓库
修改最后一次提交（可用于漏掉某个文件的提交或重新编辑信息）：git commit --amend
git pull
??git pull命令的作用是获取远程主机某个分支的更新，再与本地指定分支合并。git pull <远程主机名><远程分支名>:<本地分支名>

取回远程主机上的dev分支与本地的master分支合并：git pull origin dev:master
取回远程主机上的dev分支与当前分支合并：git pull origin dev，该命令相当于以下两条命令：
git fetch origin：获取远程主机上所有分支的更新，也可以用git fetch origin dev表示获取远程主机上dev分支的更新
git merge origin/dev：当前分支合并dev分支
注意：通过git fetch所取回的更新，在本地主机上需要用“远程主机名/分支名”的形式读取，比如origin主机的master分支，就需要用origin/master来读取。

git fetch
??git fetch命令的作用是将远程主机上所有分支的更新取回本地，并记录在.git/FETCH_HEAD中

获取远程主机上master分支的代码：git fetch origin
在本地新建test分支，并将远程主机上master分支代码下载到本地test分支：git fetch origin master:test
git push
??git push命令的作用是将本地分支的更新推送到远程主机上。

将本地master分支的更新推送到远程主机上：git push origin master
删除远程dev分支：git push origin --delete dev
git branch
??git branch命令的作用主要是做分支管理操作。

查看本地分支：git branch
查看本地和远程分支：git branch -a
新建名字为test的分支：git branch test
将test分支名字改为dev：git branch -m test dev
删除名字为dev的分支：git branch -d dev
强制删除名字为dev的分支：git branch -D dev
以上命令都是针对本地仓库操作，不影响远程仓库。

git checkout
??git checkout命令最常用的情形是创建和切换分支以及撤销工作区的修改。

切换到tag为v1.0.0时对应的代码：git checkout v1.0.0
在tag为v1.0.0的基础上创建分支名为test的分支：git checkout -b test v1.0.0。该命令相当于以下两条命令：
git branch test v1.0.0：在v1.0.0的基础上创建分支test
git checkout v1.0.0：切换到分支test
把当前目录所有修改的文件从HEAD中移除并且把它恢复成未修改时的样子：git checkout .
撤销工作目录中文件的修改（文件有改动但还未git add）：git checkout -- fileName，或者撤销所有修改使用git checkout .
git tag
??git tag命令主要是对项目标签进行管理。

查看已有的标签历史记录：git tag
给当前最新的commit打上标签：git tag <标签的定义>
给对应的commit id打上标签：git tag <标签定义> <commit id>
git log
??git log命令的作用是查看历史提交记录

查看历史提交记录：git log
将每条历史提交记录展示成一行：git log --oneline
查看某个人的提交记录：git log --author="name"
显示ASCII图形表示的分支合并历史：git log --graph
显示前n条记录：git log -n
显示某个日期之后的记录：git log --after="2018-10-1"，包含2018年10月1号的记录
显示某个日期之前的记录：git log --after="2018-10-1，包含2018年10月1号的记录
显示某两个日期之间的记录：git log --after="2018-10-1" --before="2018-10-7"
git reset
??git reset命令的作用是撤销暂存区的修改或本地仓库的提交。

撤销已经提交到暂存区的文件（已经git add但还未git commit）:
撤销已经提交到暂存区的文件：git reset HEAD fileName或git reset --mixed HEAD fileName
撤销所有提交：git reset HEAD .或git reset --mixed HEAD .
对已经提交到本地仓库做撤销（已经git commit但还未git push）：
将头指针恢复，已经提交到暂存区以及工作区的内容都不变：git reset --soft commit-id或git reset --soft HEAD~1
将头指针恢复并且撤销暂存区的提交，但是工作区的内容不变：git reset --mixed commit-id或git reset --mixed HEAD~1
将所有内容恢复到指定版本：git reset --hard commit-id或git reset --hard HEAD~1
注意：commit-id可通过git log查看（取前六位即可），HEAD~1表示前一次提交（可以此类推）。

git remote
??git remote命令的作用主要是管理远程仓库。

查看关联的远程仓库的名称：git remote
查看关联的远程仓库的详细信息：git remote -v
添加远程仓库的关联：git remote add origin <远程仓库地址>
删除远程仓库的关联：git remote remove <远程仓库名称>
修改远程仓库的关联：git remote set-url origin <新的远程仓库地址>
更新远程仓库的分支：git remote update origin --prune
git merge
??git merge命令的作用主要是分支的合并。

1：如果当前是master分支，需要合并dev分支：git merge dev

git stash
??git stash命令的作用主要如果当前分支所做的修改你还不想提交，但又需要切换到其他分支去查看，就可以使用git stash保存当前的修改。

保存当前进度：git stash
查看已经保存的历史记录：git stash list
重新应用某个已经保存的进度，并且删除进度记录：git stash pop <历史进度id>，
重新应用某个已经保存的进度，但不删除进度记录：git stash apply <历史进度id>，如果直接使用git stash默认是使用最近的保存
删除某个历史进度：git stash drop <历史进度id>
删除所有的历史进度：git stash clear
gitignore
??.gitignore文件的作用是忽略那些没必要的提交，比如系统环境或程序运行时产生的文件。GitHub为我们提供了各个语言的gitignore合集github/gitignore，其中也包括Android.gitignore。

将本地新建的项目提交到远程仓库的步骤
初始化本地仓库git init
将本地内容添加至git本地暂存区中git add .
将暂存区添加至本地仓库中git commit -m "first commit"
添加远程仓库路径git remote add origin https://github.com/gybguohao/test.git
将本地内容push至远程仓库中git push -u origin master
秘钥配置
mac终端查看是否已经存在SSH密钥：cd ~/.ssh，如果没有密钥则不会有此文件夹。

生成新的秘钥, 命令如下
ssh-keygen -t rsa -C "eamil"
你需要把邮件地址换成你自己的邮件地址，然后一路回车，使用默认值即可，因为这个个Key仅仅用于简单的服务，所以也无需设置密码。

完成后会有如下显示

Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/gybguohao/.ssh/id_rsa。
Your public key has been saved in /Users/gybguohao/.ssh/id_rsa.pub。
The key fingerprint is:
SHA256:5V6ZCQNS/3bVdl0GjGgQpWMFLazxTslnKbW2B1mbC+E eamil

如果服务器端需要公钥, 直接复制.ssh目录下的id_rsa.pub内容即可。

作者：gybguohao
链接：https://www.jianshu.com/p/cdccfef91ae1
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。