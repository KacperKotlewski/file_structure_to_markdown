# file_structure_to_markdown
program to convert file structure to markdown representation

## Installation
### Requirments
>Install [python](https://www.python.org/downloads/) 3.7+ and when you install check checkbox to add python to your Path
### Install by pip:
```bash
python -m pip install git+https://github.com/KacperKotlewski/file_structure_to_markdown.git
```

---
## Usage
Using python & console or bash
>```bash
>python -m files2md
>```

---
## Project structure
```
file_structure_to_markdown
| .gitignore
| LICENSE
| README.md
| setup.bat
| setup.py
|-files2md
| | __init__.py
| | __main__.py
| |-config
| | | config.py
| | | isIgnored.py
| | | __init__.py
| |-structure_objects
| | | file.py
| | | structureObject.py
| | | __init__.py
| | |-structurable_directory
| | | | append_subdirs.py
| | | | build_tree.py
| | | | directoryObj.py
| | | | __init__.py
```

---
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)