#!/bin/bash

curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
sudo yum install -y git gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel xz xz-devel
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv install 3.6.3
pyenv install 2.7.14
pip install virtualenv
cd $HOME
rm -rf $HOME/projects
mkdir projects
cd projects
mkdir environments
cd environments
virtualenv python2.7.14
virtualenv python3.6.3
source $HOME/projects/environments/python2.7.14/bin/activate
pyenv local 2.7.14
source $HOME/projects/environments/python3.6.3/bin/activate
pyenv local 3.6.3
