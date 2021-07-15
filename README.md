# Toolbox

Toolbox is a Python package that contains handy functions. 
It's main goal, however, is to demonstrate how to create 
a package and demonstrate how to upload it to PyPi.  
Check out [this](https://mikehuls.medium.com/create-your-custom-python-package-that-you-can-pip-install-from-your-git-repository-f90465867893)
article for a detailed explanation on how to create your 
custom Python package and upload it to PyPi!

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Toolbox like below. 
Rerun this command to check for and install  updates .
```bash
pip install git+https://github.com/Muls/toolbox
```

## Usage
Features:
* functions.listChunker  --> generator that chunks and interable in evenly sized chunks 
* functions.weirdCase    --> converts a string to a totally unreadable format
* functions.report      --> prints to the console with a timestamp
* decorators.singleton  --> used for decoratint your class to make it a singleton

#### Demo of some of the features:

```python
import mikes_toolbox
from mikes_toolbox import report

message = mikes_toolbox.functions.weirdCase("The mikes_toolbox package is ready for use")
report(message)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for chunk in mikes_toolbox.functions.listChunker(lst=list_of_numbers, dsize=3):
    print(chunk)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)