# practice-py

Shared repository for python and pop-gen practice

## installation

1.  Install [Homebrew](http://brew.sh/)

1.  Install git and [pyenv](https://github.com/yyuu/pyenv) via Homebrew:
    `brew install git pyenv`

1.  Add `pyenv init` to your shell config file (`.bash_profile` or `.zshenv`):
    ```sh
    if which pyenv >/dev/null; then eval "$(pyenv init -)"; fi
    ```

1.  Install [Anaconda](https://docs.continuum.io/) via pyenv:
    ```sh
    exec $SHELL -l
    pyenv install --list | less
    pyenv install anaconda3-4.3.1
    pyenv global anaconda3-4.3.1
    pyenv versions
    ```

1.  Install and configure [Atom](https://heavywatal.github.io/dev/atom.html)
    ```sh
    brew cask install atom
    exec $SHELL -l
    conda install flake8
    apm install linter linter-flake8 file-icons
    ```

1.  Setup [`~/.gitconfig`](https://git-scm.com/book/ja/v1/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-%E6%9C%80%E5%88%9D%E3%81%AEGit%E3%81%AE%E6%A7%8B%E6%88%90)
    and [SSH key](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
    for your GitHub account

1.  Clone this repository to your local machine:
    ```sh
    mkdir ~/git
    cd ~/git
    git clone https://github.com/heavywatal/practice-py.git
    cd practice-py/
    atom .
    python hello.py
    ```
