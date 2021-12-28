# Quickstart

This is a short introduction to pyifc. To get more detailed description 
see [API Reference](api.html)

## Installation

Run following commands in your bash:

```bash
pip install pyifc
```

```bash
pip install install-ifcopenshell-python
```

```bash
python -m install_ifcopenshell_python
```

## Usage

import pyifc like:

```python
import pyifc
```

or

```python
from pyifc import <module>
```

### Modules

So far, pyifc contains only one module: [pyifc.compress](compress.html).

#### [pyifc.compress](compress.html)

Compress module provides set of functions responsible for compressing data. 
What is more, one can also pack .ifc file right after compressing with other 
functions.

Example:

```python
import ifcopenshell
from pyifc import compress

path = "example_file.ifc"

# Compress .ifc file
compress(path)

# Compress .ifc file and write to .zip archive
compress_and_zip(path)
```
