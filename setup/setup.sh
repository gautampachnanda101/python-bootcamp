#!/bin/bash

# Update Homebrew
echo "Updating Homebrew..."
brew update

# Install Python (includes IDLE)
echo "Installing Python (includes IDLE)..."
python --verion | brew install python
echo "export PATH=\"$(brew --prefix python)/libexec/bin:$PATH\"" >> ~/.zshrc
pipx --version | brew install pipx

# Install Visual Studio Code
echo "Installing Visual Studio Code..."
code --version | brew install --cask visual-studio-code || true
# Install Venv for python
cd ~/ && python -m venv local && source local/bin/activate
# Install Jupyter
echo "Installing Jupyter..."
pip install --upgrade pip || true
pip3 install jupyter || true
brew install jupyterlab || true
brew install pycharm || true
brew install pyenv || true
brew install pyenv-virtualenv || true
brew install pyenv-virtualenvwrapper || true
brew install --cask jetbrains-toolbox || true
echo "Installation complete!"