#pasteit

pasteit is a program that allows you to paste files to pastebin like sites. Pull requests, bug reports and feature requests are highly welcome!

## Installation
This release is only tested for python 3 with python 2 support comming. To install clone the repo and simply use 
```python setup.py install```

## Usage

pasteit defaults to slexy.org if no other supported site was provided. The command `pasteit foo.txt` will paste foo.txt to slexy.org and print out the url for the paste. Other paste sites can be used with the --site option, to see a list of supported websites use the command `pasteit --list`. 

This release supports two other options to specify the author and syntax higlighting. `pasteit --author foo --language haskell bar.hs` will paste the file bar.hs with foo as the author and haskell for syntax highlighting.
