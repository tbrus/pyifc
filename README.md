<p align="center">
  <img src="https://github.com/tbrus/pyifc/blob/master/logo.png?raw=true"/>
</p>

# pyifc: Utilities for .ifc files

[![License](https://img.shields.io/github/license/tbrus/pyifc)](https://github.com/tbrus/pyifc)
[![PyPI](https://img.shields.io/pypi/v/pyifc)](https://pypi.org/project/pyifc/)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

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

**TODO**
To install `ifcopenshell` (...):



## Documentation



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

## References

`compress` module is created based on:
* [*IFCCompressor: A content-based compression algorithm for otpimizing Industry Foundation Classes files*](http://cgcad.thss.tsinghua.edu.cn/liuyushen/main/pdf/LiuYS_AIC15IFCCompressor.pdf), Jing Sun, Yu-Shen Liu, Ge Gao, Xiao-Guang Han
* [*IfcOpenShell Optimizer tutorial*](https://academy.ifcopenshell.org/posts/ifcopenshell-optimizer-tutorial/) by Johan Luttun

Test data is available [here](http://cgcad.thss.tsinghua.edu.cn/liuyushen/IFCCompressor/).