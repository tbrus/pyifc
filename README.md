<p align="center">
  <img src="https://github.com/tbrus/pyifc/blob/master/logo.png?raw=true"/>
</p>

# pyifc: Utilities for .ifc files

[![License](https://img.shields.io/github/license/tbrus/pyifc)](https://github.com/tbrus/pyifc)

## What is it?

**pyifc** is a Python package that provides utilities for working with .ifc files.

According to [Wikipedia](https://en.wikipedia.org/wiki/Industry_Foundation_Classes):
> The **Industry Foundation Classes (IFC)** data model is intended to describe architectural, building and construction industry data.

IFC format provides interoperability. This way, it doesn't matter what 
software you work on or what file format you deal with on a daily basis. 
There is a high probability that your software has import and export 
functions for .ifc files. Learn more about IFC format 
[here](https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/).

At this point, the project is in development. If you have any ideas on how it 
can be improved check [Contributions](https://github.com/tbrus/pyifc#contributions). 
If you want to know what the project currently consists of, check 
[Modules](https://github.com/tbrus/pyifc#modules).

## Table of Contents

[Modules](https://github.com/tbrus/pyifc#modules) | 
[Installation](https://github.com/tbrus/pyifc#installation) | 
[Documentation](https://github.com/tbrus/pyifc#documentation) | 
[Usage](https://github.com/tbrus/pyifc#usage) | 
[Found a bug?](https://github.com/tbrus/pyifc#found-a-bug) | 
[Changelog](https://github.com/tbrus/pyifc#changelog) | 
[Contributions](https://github.com/tbrus/pyifc#contributions) | 
[Code of Conduct](https://github.com/tbrus/pyifc#code-of-conduct) | 
[License](https://github.com/tbrus/pyifc#license)

## Modules

`compress` - set of functions responsible for compressing files  

In the future:

`compare` - set of functions responsible for comparing files  
`count` - set of functions responsible for counting elements in a file  
`modify` - set of functions responsible for modifying files  

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 
**pyifc**.

```bash
pip install pyifc
```

Unfortunately dependency package [ifcopenshell](http://ifcopenshell.org/python) 
is not distributed via PyPi. Hence you can get error while trying to 
import pyifc:

```bash
ModuleNotFoundError: No module named 'ifcopenshell'
```

To install `ifcopenshell` run from current directory:

```bash
python init_script.py
```

The script will download ifcopenshell based on given or automatically 
detected arguments. Possible arguments are listed below:

```bash
python init_script.py -h
usage: init_script.py [-h] [-s {linux,win,macos}] [-a {32,64}] [-v {37,38,39}]

Download ifcopenshell based on platform system, platform architecture 
and running python version.

optional arguments:
  -h, --help            show this help message and exit
  -s {linux,win,macos}, --system {linux,win,macos}
                        Platform system.
  -a {32,64}, --architecture {32,64}
                        Platform architecture.
  -v {37,38,39}, --python-version {37,38,39}
                        Running python version; string of major and 
                        minor version, e.g. '39'. pyifc supports python >= 3.7.
```

## Documentation


## Usage


## Found a bug?

Feel free to add a new issue on the the 
[pyifc repository](https://github.com/tbrus/my-own-package/issues). 
If you found a solution, feel free to add a new pull request.

## Changelog

See [CHANGELOG.md](https://github.com/tbrus/pyifc/blob/master/CHANGELOG.md).

## Contributions

See [CONTRIBUTING.md](https://github.com/tbrus/pyifc/blob/master/CONTRIBUTING.md).

## Code of Conduct

Everyone interacting in the pyifc project's development is expected to follow 
the [Code of Conduct](https://github.com/tbrus/pyifc/blob/master/CODE_OF_CONDUCT.md).

## License

**pyifc** is released under the terms of [the MIT License](https://github.com/tbrus/pyifc/blob/master/LICENSE).