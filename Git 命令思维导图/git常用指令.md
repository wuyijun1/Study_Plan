git����ָ���ܽ�
ԭ��White Coco ��󷢲���2019-06-03 17:15:36 �Ķ��� 133  �ղ�


������ֿ�:
$ git init --bare
�ֿ�����ֿ�֮���ת����

$ git clone --bare
չ��
1. git��������
�����˻���Ϣ
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
����ssh key
ssh-keygen  -t  rsa  -C  "mail"
cat ~/.ssh/id_rsa.pub
1
2
��ssh key������gerrit���ӻ���github��

�������ø���
gedit  ~/.gedit .cshrc.user
source gitenv.csh
git submodule update
1
2
3
ͼ�λ�����
gitgui &
gitk &
1
2
����repo
git clone <link>
1
2. branch����
������֧
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
ɾ����֧
git branch �Cm oldbranch newbranch  // Modify branch
git branch �CD branch  // Delete local branch
1
2
����Զ�˷�֧
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
3. commit ����
�ļ�״̬����
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
���ɾ���ļ�
git add <file>  // Add changed files to local git stage
git add.  // Add all changed files to local git stage
git mv <old> <new> // Rename for file
git rm <file>  // Remove some files for current stage
1
2
3
4
����ע��
git commit <file>  // Commit files, Input comments
git commit �Ca  // Commit all files not git-add, Input comments
git commit �Ca �Cm ��your comments�� // Commit with comment, not suggest
git commit --amend  // Amend commit to last one 
1
2
3
4
push��Զ�˷�֧
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
commit ����
git fetch  // Fetch changes but no merge
git merge master  // Merge master to current devel branch
git pull  // this command = git fetch + git merge
1
2
3
�����ͻ��Cherry-pick
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
�����ͻ��git rebase
git rebase -i HEAD~4
git rebase -i <commit id>
git rebase �Ccontinue  # After problem resolved
git rebase �Cskip          # Skip this conflict patch
git rebase �Cabort       # Check out the original branch and stop rebasing
1
2
3
4
5
checkout �� clean����
git checkout -- // undo all changes in repo files
git checkout -f  // force checkout (throw away local modifications)
git clean �Cdfx // clean all ignores files  
1
2
3
����
git reset --hard  // Revert local branch same as remote 
git reset --hard <commit id>  // Revert to the commit id
git push origin HEAD --force  // used with caution
git reset --hard commit id
1
2
3
4
git config
??git config���������������git�������Ϣ��

����ȫ�ֵ��û��������䣬mac�¿�ͨ���ն���������cat ~/.gitconfig�鿴������Ϣ��
�����û�����git config --global user.name "name"
�����û����䣺git config --global user.email "eamil"
��Ե����ֿ������û��������䣬mac�¿�ͨ���ն˽��뵽��Ŀ�ĸ�Ŀ¼�У�Ȼ����������cat .git/config�鿴������Ϣ��
�����û�����git config user.name "name"
�����û����䣺git config user.email "eamil"
�鿴git����������Ϣ��git config --list
�鿴���õ��û�����git config user.name
�鿴���õ��û����䣺git config user.email
�������������
git config --global alias.st status����git status����git st����
git config --global alias.co checkout����git checkout����git co����
git config --global alias.ci commit����git commit����git ci����
git config --global alias.br branch����git branch����git br����
Ҳ�����Զ�����������ı�������Ҫ�����ҷ���������ɡ�

git init
??git init������������ڵ�ǰĿ¼�г�ʼ���ֿ⣬���Ҵ���һ����Ϊ.git����Ŀ¼����Ŀ¼�������ʼ����Git�ֿ������еı����ļ���

git status
??git status�������������ʾ�ļ�״̬����ɫ��ʾ����Ŀ¼���ļ����޸ĵ���û���ύ���ݴ�������ɫ��ʾ�Ѿ��ύ���ݴ�����

�Լ���ķ�ʽ��ʾ�ļ�״̬��git status -s
A�������������ļ�����������û�У�
C���ļ���һ���¿���
D������ɾ�����ļ����������ϻ��ڣ�
M����ɫΪ�޸Ĺ�δ����ӽ��ݴ����ģ���ɫΪ�Ѿ���ӽ��ݴ�����
R���ļ������޸�
T���ļ������ͱ��޸�
U���ļ�û�б��ϲ�(����Ҫ��ɺϲ����ܽ����ύ)
X��δ֪״̬(�ܿ���������git��bug�ˣ��������git�ύbug report)
?��δ��git���й�������ʹ��git add fileName���ļ���ӽ������й���
�Ѿ����޸ĵ���û�ύ���ݴ������ļ�������ͨ������git checkout -- fileName�������ġ�

git add
??git add����������ǽ��ļ��ӹ���Ŀ¼������ݴ���

�������޸ĵ���Ϣ��ӵ��ݴ�����git add .
�����и����ļ��б��޸Ĺ�����ɾ�����ļ���Ϣ������ݴ�����git add -u��git add --update�������ᴦ����Щû�б����ٵ��ļ�
�����и����ļ��б��޸Ĺ�����ɾ���ļ�������δ���ٵ��ļ���Ϣ��ӵ��ݴ�����git add -A��git add --all
ע�⣺git add .��git add -A��2.x�汾���ύ���ͷ��湦����ͬ��������Ϊ����Ŀ¼��ͬ�������죺

git add .ֻ���ύ��ǰĿ¼������Ŀ¼����Ӧ�ļ���
git add -A�������ĸ�Ŀ¼ִ�ж����ύ��Ӧ�ļ���
�Ѿ����ύ���ݴ������ļ�������ͨ������git reset HEAD -- fileName�����ύ��

git commit
??git commit����������ǽ��ݴ������޸��ύ�����زֿ⣬ͬʱ������һ��commmit-id��

���ݴ������޸��ύ�����زֿ⣺git commit -m "message"��"message"�Ǳ����ύ�ļ������ݣ���������¹��ܻ��޸�bug��
�����ع��������޸ĺ�δʹ��git add .������ӵ��ݴ����е��ļ�Ҳ�ύ�����زֿ⣺git commit �Ca �Cm "message"���������൱�������������
git add .���������޸ĵ���Ϣ��ӵ��ݴ���
git add -m "message"�����ݴ������޸��ύ�����زֿ�
�޸����һ���ύ��������©��ĳ���ļ����ύ�����±༭��Ϣ����git commit --amend
git pull
??git pull����������ǻ�ȡԶ������ĳ����֧�ĸ��£����뱾��ָ����֧�ϲ���git pull <Զ��������><Զ�̷�֧��>:<���ط�֧��>

ȡ��Զ�������ϵ�dev��֧�뱾�ص�master��֧�ϲ���git pull origin dev:master
ȡ��Զ�������ϵ�dev��֧�뵱ǰ��֧�ϲ���git pull origin dev���������൱�������������
git fetch origin����ȡԶ�����������з�֧�ĸ��£�Ҳ������git fetch origin dev��ʾ��ȡԶ��������dev��֧�ĸ���
git merge origin/dev����ǰ��֧�ϲ�dev��֧
ע�⣺ͨ��git fetch��ȡ�صĸ��£��ڱ�����������Ҫ�á�Զ��������/��֧��������ʽ��ȡ������origin������master��֧������Ҫ��origin/master����ȡ��

git fetch
??git fetch����������ǽ�Զ�����������з�֧�ĸ���ȡ�ر��أ�����¼��.git/FETCH_HEAD��

��ȡԶ��������master��֧�Ĵ��룺git fetch origin
�ڱ����½�test��֧������Զ��������master��֧�������ص�����test��֧��git fetch origin master:test
git push
??git push����������ǽ����ط�֧�ĸ������͵�Զ�������ϡ�

������master��֧�ĸ������͵�Զ�������ϣ�git push origin master
ɾ��Զ��dev��֧��git push origin --delete dev
git branch
??git branch�����������Ҫ������֧���������

�鿴���ط�֧��git branch
�鿴���غ�Զ�̷�֧��git branch -a
�½�����Ϊtest�ķ�֧��git branch test
��test��֧���ָ�Ϊdev��git branch -m test dev
ɾ������Ϊdev�ķ�֧��git branch -d dev
ǿ��ɾ������Ϊdev�ķ�֧��git branch -D dev
�����������Ա��زֿ��������Ӱ��Զ�ֿ̲⡣

git checkout
??git checkout������õ������Ǵ������л���֧�Լ��������������޸ġ�

�л���tagΪv1.0.0ʱ��Ӧ�Ĵ��룺git checkout v1.0.0
��tagΪv1.0.0�Ļ����ϴ�����֧��Ϊtest�ķ�֧��git checkout -b test v1.0.0���������൱�������������
git branch test v1.0.0����v1.0.0�Ļ����ϴ�����֧test
git checkout v1.0.0���л�����֧test
�ѵ�ǰĿ¼�����޸ĵ��ļ���HEAD���Ƴ����Ұ����ָ���δ�޸�ʱ�����ӣ�git checkout .
��������Ŀ¼���ļ����޸ģ��ļ��иĶ�����δgit add����git checkout -- fileName�����߳��������޸�ʹ��git checkout .
git tag
??git tag������Ҫ�Ƕ���Ŀ��ǩ���й���

�鿴���еı�ǩ��ʷ��¼��git tag
����ǰ���µ�commit���ϱ�ǩ��git tag <��ǩ�Ķ���>
����Ӧ��commit id���ϱ�ǩ��git tag <��ǩ����> <commit id>
git log
??git log����������ǲ鿴��ʷ�ύ��¼

�鿴��ʷ�ύ��¼��git log
��ÿ����ʷ�ύ��¼չʾ��һ�У�git log --oneline
�鿴ĳ���˵��ύ��¼��git log --author="name"
��ʾASCIIͼ�α�ʾ�ķ�֧�ϲ���ʷ��git log --graph
��ʾǰn����¼��git log -n
��ʾĳ������֮��ļ�¼��git log --after="2018-10-1"������2018��10��1�ŵļ�¼
��ʾĳ������֮ǰ�ļ�¼��git log --after="2018-10-1������2018��10��1�ŵļ�¼
��ʾĳ��������֮��ļ�¼��git log --after="2018-10-1" --before="2018-10-7"
git reset
??git reset����������ǳ����ݴ������޸Ļ򱾵زֿ���ύ��

�����Ѿ��ύ���ݴ������ļ����Ѿ�git add����δgit commit��:
�����Ѿ��ύ���ݴ������ļ���git reset HEAD fileName��git reset --mixed HEAD fileName
���������ύ��git reset HEAD .��git reset --mixed HEAD .
���Ѿ��ύ�����زֿ����������Ѿ�git commit����δgit push����
��ͷָ��ָ����Ѿ��ύ���ݴ����Լ������������ݶ����䣺git reset --soft commit-id��git reset --soft HEAD~1
��ͷָ��ָ����ҳ����ݴ������ύ�����ǹ����������ݲ��䣺git reset --mixed commit-id��git reset --mixed HEAD~1
���������ݻָ���ָ���汾��git reset --hard commit-id��git reset --hard HEAD~1
ע�⣺commit-id��ͨ��git log�鿴��ȡǰ��λ���ɣ���HEAD~1��ʾǰһ���ύ�����Դ����ƣ���

git remote
??git remote�����������Ҫ�ǹ���Զ�ֿ̲⡣

�鿴������Զ�ֿ̲�����ƣ�git remote
�鿴������Զ�ֿ̲����ϸ��Ϣ��git remote -v
���Զ�ֿ̲�Ĺ�����git remote add origin <Զ�ֿ̲��ַ>
ɾ��Զ�ֿ̲�Ĺ�����git remote remove <Զ�ֿ̲�����>
�޸�Զ�ֿ̲�Ĺ�����git remote set-url origin <�µ�Զ�ֿ̲��ַ>
����Զ�ֿ̲�ķ�֧��git remote update origin --prune
git merge
??git merge�����������Ҫ�Ƿ�֧�ĺϲ���

1�������ǰ��master��֧����Ҫ�ϲ�dev��֧��git merge dev

git stash
??git stash�����������Ҫ�����ǰ��֧�������޸��㻹�����ύ��������Ҫ�л���������֧ȥ�鿴���Ϳ���ʹ��git stash���浱ǰ���޸ġ�

���浱ǰ���ȣ�git stash
�鿴�Ѿ��������ʷ��¼��git stash list
����Ӧ��ĳ���Ѿ�����Ľ��ȣ�����ɾ�����ȼ�¼��git stash pop <��ʷ����id>��
����Ӧ��ĳ���Ѿ�����Ľ��ȣ�����ɾ�����ȼ�¼��git stash apply <��ʷ����id>�����ֱ��ʹ��git stashĬ����ʹ������ı���
ɾ��ĳ����ʷ���ȣ�git stash drop <��ʷ����id>
ɾ�����е���ʷ���ȣ�git stash clear
gitignore
??.gitignore�ļ��������Ǻ�����Щû��Ҫ���ύ������ϵͳ�������������ʱ�������ļ���GitHubΪ�����ṩ�˸������Ե�gitignore�ϼ�github/gitignore������Ҳ����Android.gitignore��

�������½�����Ŀ�ύ��Զ�ֿ̲�Ĳ���
��ʼ�����زֿ�git init
���������������git�����ݴ�����git add .
���ݴ�����������زֿ���git commit -m "first commit"
���Զ�ֿ̲�·��git remote add origin https://github.com/gybguohao/test.git
����������push��Զ�ֿ̲���git push -u origin master
��Կ����
mac�ն˲鿴�Ƿ��Ѿ�����SSH��Կ��cd ~/.ssh�����û����Կ�򲻻��д��ļ��С�

�����µ���Կ, ��������
ssh-keygen -t rsa -C "eamil"
����Ҫ���ʼ���ַ�������Լ����ʼ���ַ��Ȼ��һ·�س���ʹ��Ĭ��ֵ���ɣ���Ϊ�����Key�������ڼ򵥵ķ�������Ҳ�����������롣

��ɺ����������ʾ

Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/gybguohao/.ssh/id_rsa��
Your public key has been saved in /Users/gybguohao/.ssh/id_rsa.pub��
The key fingerprint is:
SHA256:5V6ZCQNS/3bVdl0GjGgQpWMFLazxTslnKbW2B1mbC+E eamil

�������������Ҫ��Կ, ֱ�Ӹ���.sshĿ¼�µ�id_rsa.pub���ݼ��ɡ�

���ߣ�gybguohao
���ӣ�https://www.jianshu.com/p/cdccfef91ae1
��Դ������
����Ȩ���������С���ҵת������ϵ���߻����Ȩ������ҵת����ע��������