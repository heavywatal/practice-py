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

1.  Update your `master` branch:
    ```sh
    % git checkout master
    % git status
    % git fetch upstream
    % git merge upstream/master
    % git status
    % git push  # origin master
    ```

1.  Make a new branch for a task.
    ```sh
    % git checkout -b issue-14-fitness
    % git status
    ```

1.  Edit your local files.

1.  Commit the change to your issue branch:
    ```sh
    % git status
    % git diff
    % git add main.py
    % git status
    % git commit -m "Create Individual class #2"
    % git status
    ```
    Don't forget to include the issue id in your comment.

1.  Check `upstream` again.
    Merge and rebase if necessary.
    ```sh
    % git checkout master
    % git status
    % git fetch upstream
    % git merge upstream/master
    % git status
    % git checkout issue-14-fitness
    % git rebase -i master
    ```

1.  Push the commit to your `origin`:
    ```sh
    % git push origin issue-14-fitness
    ```

1.  Send "Pull Request" with the button on your GitHub page
    ([Kazuki526](https://github.com/Kazuki526/practice-py), [hamazaki1990](https://github.com/hamazaki1990/practice-py)).

1.  Your PR will be corrected and merged to [heavywatal/practice-py](https://github.com/heavywatal/practice-py).
