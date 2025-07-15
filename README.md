# py-oiio
Python wheels for OpenImageIO

Currently just a simple explainer on how to create a usable Python module.

**Update 7/15/2025: This repository is unmaintained. There are now offical OpenImageIO Python wheels available at https://pypi.org/project/OpenImageIO/**

## Usage

```python
import oiio
from oiio import ImageInput, ImageOutput
from oiio import ImageBuf, ImageSpec, ImageBufAlgo
```

Everything else should be the same as in the official [OIIO documentation](https://openimageio.readthedocs.io/en/latest/index.html).


## Windows build steps

1. Get vcpkg and run script to install.
2. Install OpenImageIO with ``./vcpkg install openimageio[pybind11]:x64-windows``.
3. Copy the ``vcpkg\installed\x64-windows\lib\python3.10\site-packages\OpenImageIO.cp310-win_amd64.pyd`` file to the ``oiio`` folder.
4. Copy DLLs from ``vcpkg\installed\x64-windows\bin`` to the ``oiio`` folder.
5. Rename the .pyd file to ``OpenImageIO.pyd``.
6. (Optional) ``python3 -m pip install mypy`` then run ``stubgen -m OpenImageIO -o ./`` to generate a .pyi stub for code completion. (Thanks, [@pixel-ninja](https://github.com/pixel-ninja))


## Releasing on PyPI

- Follow the above steps to build OpenImageIO for Python
- Navigate to the root directory
- Run ``py -m build``
- Then run ``twine upload dist/*`` and follow the prompts.


# License

Licensed under the MIT license.
