**_PIP_**

`pip is already installed if you are using Python 2 >=2.7.9 
or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by virtualenv or pyvenv.
`



_**Installing with get-pip.py**_

pip is a command line program. When you install pip,it got added to PATH
 
`To verify `

_$ pip <pip arguments>_
 or 
_$ python -m pip <pip arguments>_ 
 
To install pip, securely download get-pip.py. 

_curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py_

_python get-pip.py_

**NOTE:**

get-pip.py also installs setuptools and wheel if they are not already. 

setuptools is required to install source distributions.
 
Both are required in order to build a Wheel Cache (which improves installation speed), although neither are required to install pre-built wheels.

--no-setuptools   If set, do not attempt to install setuptools

--no-wheel   If set, do not attempt to install wheel

_**Upgrading pip**_

_pip install -U pip_ (on Linux)

_python -m pip install -U pip_ (on windows)


_**USAGE**_

`Install a package from PyPI:`

_$ pip install SomePackage_   # latest version

_$ pip install SomePackage-1.0-py2.py3-none-any.whl_  ( If already downloaded)

_$ pip install SomePackage==1.0.4_     # specific version

_$ pip install 'SomePackage>=1.0.4'_     # minimum version

_$ pip install -r requirements.txt_  #From Requirement Files

**NOTE :**

_pip freeze > requirements.txt_


so:
Requirements File Format
pip freeze
"setup.py vs requirements.txt" (an article by Donald Stufft)

https://pip.pypa.io/en/stable/user_guide/

https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format




`Show what files were installed:`

_$ pip show --files SomePackage_

`List what packages are outdated:`

_$ pip list --outdated_

`Upgrade a package:`

_$ pip install --upgrade SomePackage_

`Uninstall a package:`

_$ pip uninstall SomePackage_
