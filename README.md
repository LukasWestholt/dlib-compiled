# Dlib compiled binary wheels for Python 3.8 - 3.14 for multiple archs

This repository contains the compiled binary (.whl) files for the [Dlib](http://dlib.net/) library to install on:

- Python versions 3.8, 3.9, 3.10, 3.11, 3.12, 3.13 and 3.14 on a Windows x64 OS (win_amd64).
- Python versions 3.9, 3.10, 3.11, 3.12, 3.13 and 3.14 on a MacOS ARM OS (macosx_arm64).
- Python versions 3.8, 3.9, 3.10, 3.11, 3.12, 3.13 and 3.14 on a MacOS x64 OS (macosx_x86_64).
- Python versions 3.8, 3.9, 3.10, 3.11, 3.12, 3.13 and 3.14 on a Linux x64 OS (manylinux_x86_64, musllinux_x86_64).
- Python versions 3.8, 3.9, 3.10, 3.11, 3.12, 3.13 and 3.14 on a Linux ARM OS (manylinux_aarch64, musllinux_aarch64).

Windows ARM OS Python is currently not supported. PRs welcome!


## Steps to install Dlib:

* Install the wheels via GitHub URL:

```
pip install https://github.com/LukasWestholt/dlib-compiled/releases/download/v1.0.1/wheel_for_your_python_version.whl
```

Example:

```
python -m pip install https://github.com/LukasWestholt/dlib-compiled/releases/download/v1.0.1/dlib-20.0.99-cp310-cp310-win_amd64.whl
```


## Alternative way to install Dlib:

* Download the wheel file for your specific Python version 

* Open a terminal and install Dlib via:

```
python -m pip install <downloaded-file>.whl 
```

## Steps to build Dlib from source:
If you'd like to build it from source, follow these exact steps as per their [docs](https://github.com/davisking/dlib?tab=readme-ov-file#compiling-dlib-python-api).
You might need to install [Visual Studio 2022](https://visualstudio.microsoft.com/vs/community/) with the option **Desktop Development with C++** on Windows.

# Related

- https://github.com/z-mahmud22/Dlib_Windows_Python3.x
- https://github.com/sachadee/Dlib
