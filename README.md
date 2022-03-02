# py-oiio
Python wheels for OpenImageIO

Currently, just a simple explainer, etc on how to create a usable python module.


## Windows build steps

- Get vcpkg and run script to install 
- Install OpenImageIO ``./vcpkg install openimageio[pybind11]:x64-windows``
- Copy the ``vcpkg\installed\x64-windows\lib\python3.10\site-packages\OpenImageIO.cp310-win_amd64.pyd`` file to ``oiio``
- Copy DLLs from ``vcpkg\installed\x64-windows\bin`` to ``oiio``
- Rename pyd file to ``OpenImageIO``


## Usage

```python
import oiio
from oiio import ImageInput, ImageOutput
from oiio import ImageBuf, ImageSpec, ImageBufAlgo
```

Everything else should be the same as in the official [OIIO documentation](https://openimageio.readthedocs.io/en/latest/index.html).


# License

Licensed under the MIT license.
