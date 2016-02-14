---
title: Introduction to GitHub
title: GitHub
permalink: /github/
---
# Introduction to Git and GitHub
Portions adpated from <http://stat545-ubc.github.io/git00_index.html> and <http://www.cureffi.org/2014/08/27/git-tutorial/>

## Why Git?
Git is a version control system. It’s original purpose was to help groups of developers work collaboratively on big software projects. Git manages the evolution of a set of files – called a repository – in a sane, highly structured way. If you have no idea what I’m talking about, think of it as the “Track Changes” features from Microsoft Word but much, much better.

Git has been re-purposed by the data science community. In addition to using it for source code, we use it to manage the motley collection of files that make up typical data analytical projects, which often consist of data, reports, and, yes, source code.

When you want to make your work visible to other people, either in a read-only way or for genuine collaboration, you can make the associated Git repository available on the web. This can be totally public or private to your closest friends. Regardless, this reduces the extra work associated with sharing and collaboration almost to zero, which has huge benefits. GitHub is a very popular hosting site that provides this service (and more). If you have no idea what I’m talking about, think of it as DropBox but much better (at least for our purposes).

Full participation in the “data community” these days practically requires familiarity with Git and GitHub. These tools are also helpful to us for course logistics, such as sharing code between instructor and student. For both reasons, we will be using Git and GitHub. Below we explain how to install the Git software locally on your computer.

### Make a GitHub account and Install Git
Go to <a href=https://github.com/>GitHub.com</a> and register yourself an account. You can have unlimited free public repositories; their business model is based on charging for private repositories. If you use your `.edu` email address, you can sign up for an <a href="https://education.github.com/discount_requests/new">education discount</a> which gives you five free private repos. You'll also need to <a href="https://help.github.com/articles/set-up-git/">install and configure git</a>; follow the directions for your operating system.

### Make a repo on GitHub

Go to <https://github.com> and make sure you are logged in.

Click green "New repository" button. Or, if you are on your own profile page, click on "Repositories", then click the green "New" button.

Repository name: `myrepo` (or whatever you wish)  
Public  
YES Initialize this repository with a README

Click big green button "Create repository."

Copy the HTTPS clone URL. It's near the bottom of the right sidebar.

### Clone the repo to your local computer

Go to the [shell](git09_shell.html).

Take charge of -- or at least notice! -- what directory you're in. `pwd` to display working directory. `cd` to move around. Personally, I would do this sort of thing in `~/tmp`.

Clone `myrepo` from GitHub to your computer. This URL should have **your GitHub username** and the name of **your practice repo**. If your [shell](git09_shell.html) cooperates, you should be able to paste the whole `https://....` bit that we copied above. But some shells are not (immediately) clipboard aware. Type it. **Accurately.**

``` bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```
        
This should look something like this:

``` bash
jenny@2015-mbp tmp $ git clone https://github.com/jennybc/myrepo.git
Cloning into 'myrepo'...
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
Checking connectivity... done.
```

Make this new repo your working directory, list its files, display the README, and get some information on its connection to GitHub:

``` bash
cd myrepo
ls
less README.md
git remote show origin
```

This should look something like this:

``` bash
jenny@2015-mbp ~ $ cd myrepo

jenny@2015-mbp myrepo $ ls
README.md

jenny@2015-mbp myrepo $ less README.md 
# myrepo
tutorial development

jenny@2015-mbp myrepo $ git remote show origin
* remote origin
  Fetch URL: https://github.com/jennybc/myrepo.git
  Push  URL: https://github.com/jennybc/myrepo.git
  HEAD branch: master
  Remote branch:
    master tracked
  Local branch configured for 'git pull':
    master merges with remote master
  Local ref configured for 'git push':
    master pushes to master (up to date)
```

### Make a local change, commit, and push

Add a line to README and verify that Git notices the change:

``` bash
echo "A line I wrote on my local computer" >> README.md
git status
```

This should look something like this:

``` bash
jenny@2015-mbp myrepo $ echo "A line I wrote on my local computer" >> README.md
jenny@2015-mbp myrepo $ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

Commit this change and push to your remote repo on GitHub.

``` bash
git add -A
git commit -m "A commit from my local computer"
git push
```

This should look something like this:

``` bash
jenny@2015-mbp myrepo $ git add -A

jenny@2015-mbp myrepo $ git commit -m "A commit from my local computer"
[master de669ba] A commit from my local computer
 1 file changed, 1 insertion(+)
 
jenny@2015-mbp myrepo $ git push
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 311 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/jennybc/myrepo.git
   b4112c5..de669ba  master -> master
```

If you're a new GitHub user, you will be challenged for your GitHub username and password. Provide them!

### Confirm the local change propagated to the GitHub remote

Go back to the browser. I assume we're still viewing your new GitHub repo.

Refresh.

You should see the new "A line I wrote on my local computer" in the README.

If you click on "commits," you should see one with the message "A commit from my local computer."

If you have made it this far, you are ready to graduate to [using Git and GitHub with RStudio](git07_git-github-rstudio.html). But first ...

### Am I really going to type GitHub username and password on each push?

It is likely that your first push, above, leads to a challenge for your GitHub username and password.

This will drive you crazy in the long-run and make you reluctant to push. Read more [here](git06_credential-caching.html) about GitHub credential caching.

Now is the perfect time to go there, since you have a functioning test repo.

### Clean up

When you're read to clean up, delete the local repo in the [shell](git09_shell.html):

``` bash
cd ..
rm -rf myrepo/
```

In the browser, viewing your repo's landing page on GitHub, click on "Settings", near the bottom or the right sidebar.

Scroll down, click on "delete repository," and do as it asks.

Go back to the [index for the all the Git stuff](git00_index.html).


### branching and merging
<http://pcottle.github.io/learnGitBranching/>

```
#see branches that are in your repo
git branch
#make a branch called test-branch
git branch test-branch 
#move to test-branch
git checkout test-branch
#make and commit changes
git add myscript.py
git commit -m 'fixed function2 in myscript.py'
git push
#merge the branch test-branch into the master branch
git checkout master 
git merge test-branch
#now merge master into test-branch so all branches are the same
git checkout test-branch
git merge master
```