# practice-py

Shared repository for python and pop-gen practice

## Installation and configuration

1.  Install [Homebrew](http://brew.sh/)

1.  Install git and [pyenv](https://github.com/yyuu/pyenv) via Homebrew:
    `brew install git pyenv`

1.  Add `pyenv init` to your shell config file (`.bash_profile` or `.zshenv`):
    ```sh
    if which pyenv >/dev/null; then eval "$(pyenv init -)"; fi
    ```

1.  Install [Anaconda](https://docs.continuum.io/) via pyenv:
    ```sh
    % exec $SHELL -l
    % pyenv install --list | less
    % pyenv install anaconda3-4.3.1
    % pyenv versions
    % pyenv global anaconda3-4.3.1
    ```

1.  Install and configure [Atom](https://heavywatal.github.io/dev/atom.html)
    ```sh
    % brew cask install atom
    % exec $SHELL -l
    % conda install flake8
    % apm install linter linter-flake8 file-icons
    ```

1.  Setup [`~/.gitconfig`](https://git-scm.com/book/ja/v1/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-%E6%9C%80%E5%88%9D%E3%81%AEGit%E3%81%AE%E6%A7%8B%E6%88%90)
    and [SSH key](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
    for your GitHub account to do `git push` without entering password

1.  Fork this repository to your GitHub account.
    Press "Fork" button at top-right of this page.
    
1.  Clone the forked repository to your local machine:
    ```sh
    % mkdir ~/git
    % cd ~/git
    % git clone https://github.com/{YOURNAME}/practice-py.git
    % cd practice-py/
    % atom .
    % python hello.py
    ```

1.  Make an alias to `upstream` repository:
    ```sh
    % git remote add upstream https://github.com/heavywatal/practice-py.git
    % git remote -v
    origin  https://github.com/{YOURNAME}/practice-py.git (fetch)
    origin  git@github.com:{YOURNAME}/practice-py.git (push)
    upstream  https://github.com/heavywatal/practice-py.git (fetch)
    upstream  git@github.com:heavywatal/practice-py.git (push)
    ```
    Note that your forked repository is named `origin`.


## Usage

1.  See tasks/issues in "To Do" column of [Projects page](https://github.com/heavywatal/practice-py/projects/1).

1.  Synchronize your `master` branch with `upstream/master`:
    ```sh
    % git checkout master
    % git status
    % git fetch --all
    % git merge upstream/master
    % git status
    % git push  # origin master
    ```

1.  Make a new branch from `master` for each task, and switch to it:
    ```sh
    % git checkout -b issue-2-individual
    % git status
    ```
    Do not commit to `master` or old branches.

1.  Edit your local files.

1.  Commit the change to the task branch:
    ```sh
    % git status
    % git diff
    % git add main.py
    % git status
    % git commit -m "Create Individual class #2"
    % git status
    ```
    Please include the issue tag in your comment.

1.  Check `upstream` again, merge it to your `master`, and rebase the task branch if necessary:
    ```sh
    % git fetch upstream
    ##### if any updates are available
    % git checkout master
    % git merge upstream/master
    % git status
    % git checkout issue-2-individual
    % git rebase -i master
    ```

1.  Push the commit to your `origin`:
    ```sh
    % git push origin issue-2-individual
    ```
    You may need to rename the branch or `push --force` to solve a conflict.

1.  Send "Pull Request" from your GitHub page
    ([Kazuki526](https://github.com/Kazuki526/practice-py), [hamazaki1990](https://github.com/hamazaki1990/practice-py)).
    Check commit log and diffs before submission.
    Comments and questions are welcomed.

1.  You can commit and push again to your branch if you want to fix something.

1.  The PR will be corrected and merged to [heavywatal/practice-py](https://github.com/heavywatal/practice-py).
    You can go back to the step 1 to move on to the next task before the PR merging.

1.  After PR merging, the task branch can be deleted by pushing a button on the PR page or by pushing an empty branch with `git push origin :issue-2-individual`
