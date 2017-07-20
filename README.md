# fzf :heart: gitignore.io

[fzf](https://github.com/junegunn/fzf) interface for creating `.gitignore` files using the [gitignore.io](https://www.gitignore.io/) API.
This plugin was inspired by [helm-gitignore](https://github.com/jupl/helm-gitignore).

## Requirements

* [Neovim](https://neovim.io/)
* [python-client](https://github.com/neovim/python-client)
* fzf

## Installation

First, install the Neovim python client.

```sh
pip3 install --upgrade neovim
```

Then, use your favorite Neovim plugin manager to install `fzf-gitignore`.

#### Using [vim-plug](https://github.com/junegunn/vim-plug)

```vim
Plug 'junegunn/fzf', {'dir': '~/.fzf', 'do': './install --all'}
Plug 'fszymanski/fzf-gitignore', {'do': ':UpdateRemotePlugins'}
```

## Documentation

For more information, see `:help fzf_gitignore.txt`.
