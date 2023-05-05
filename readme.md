# Clock-Count

mini clock count easy to use

![](https://i.imgur.com/JPYGur8.png)

## Getting Start Project

```
git clone https://github.com/watchakorn-18k/Clock-Count.git

cd Clock-Count

```

## Installation

```
# create virtualenv auto name
fenv onlyenv

# install package in requirements.txt
fenv install

```

## Tree

<!--- Start Tree --->

```bash
.
└── Clock-Count/
        └──.vscode/
                └──settings.json
        └──env_Clock-Count/
        └──.gitignore
        └──main.py
        └──readme.md
        └──requirements.txt

```

<!--- End Tree --->

## Build

```
pyinstaller --onefile --name "Clock Count" --add-data "asset/icon.ico;asset" --icon "asset/icon.ico" main.py
```

## Contributing

If you would like to contribute to the project, include a section on how to do so, including any guidelines and best practices.

## License

Include information about the license used for the project, such as the name of the license (e.g. MIT, Apache 2.0, etc.) and a link to the license text.
