# py-oiio
Python wheels for OpenImageIO

Currently, just a simple explainer on how to create a usable python module.


# Windows build steps

- Get vcpkg and run script to install 
- Install OpenImageIO ``./vcpkg install openimageio[pybind11]:x64-windows``
- Copy the ``vcpkg\installed\x64-windows\lib\python3.10\site-packages\OpenImageIO.cp310-win_amd64.pyd`` file
- Copy DLLs from ``vcpkg\installed\x64-windows\bin``
