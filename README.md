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
>python -m file2md
>```

---
## Project structure
```
CBS_DiscordBot
| README.md
| .gitignore
| LICENCSE
| setup.py                <- module setup
| run.py                  <- run file in python
| run.bat                 <- run file for windows
| run.sh                  <- run file for linux
|-example
| | bot.py                <-example bot
| | conf                  <- configuration file of example bot
|-cbs_db                  <- src folder
| | __init__.py           <- main bot instance
| | config.py             <- pure config 
| |-bot_class
| | | __init__.py         <- bot builder class for new istances
| |-cogs                  <- cogs
| | |-musicbot
| | | | __init__.py       <- musicbot main cog
| | |-util
| | | | __init__.py       <- utilities
| | | ...                 <- other cogs in future
|-test                    <- unit test folder
|-build
|-dist
```

---
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU](https://choosealicense.com/licenses/gpl-3.0/)