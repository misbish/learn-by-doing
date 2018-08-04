##VIRTUAL ENVIRONMENT

`https://docs.python-guide.org/dev/virtualenvs/`

_virtualenv_ is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.


It can be used standalone, in place of _Pipenv_.


`Install virtualenv via pip:`

_$ pip install virtualenv_

`Test your installation`

_$ virtualenv --version_

`Create a virtual environment for a project:`

_$ cd my_project_folder_

_$ virtualenv my_project_

_virtualenv my_project_ will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages

`You can also use the Python interpreter of your choice (like python2.7).
`

_$ virtualenv -p /usr/bin/python2.7 my_project_

`or change the interpreter globally with an env variable in ~/.bashrc:`

_$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7_

`To begin using the virtual environment, it needs to be activated:`
  
 _$ source my_project/bin/activate_
 
 `If you are done working in the virtual environment for the moment, you can deactivate it:`
 
 _$ deactivate_
 
 **NOTE:**
 
 To delete a virtual environment, just delete its folder. (In this case, it would be rm -rf my_project.)
 
 
 **NOTE:**
 
 Running virtualenv with the option --no-site-packages will not include the packages that are installed globally. This can be useful for keeping the package list clean in case it needs to be accessed later. [This is the default behavior for virtualenv 1.7 and later.]
 
 
 
 
 ##virtualenvwrapper
 
 virtualenvwrapper provides a set of commands which makes working with virtual environments much more pleasant. 
 
 It also places all your virtual environments in one place.
 
 `To install (make sure virtualenv is already installed):`
 
 _$ pip install virtualenvwrapper_
 
 _$ export WORKON_HOME=~/Envs_
 
 _$ source /usr/local/bin/virtualenvwrapper.sh_
 
 `For Windows, you can use the virtualenvwrapper-win.`
 
 `To install (make sure virtualenv is already installed):`
 
 _$ pip install virtualenvwrapper-win_
 
**NOTE:**
 
In Windows, the default path for WORKON_HOME is %USERPROFILE%Envs


`Create a virtual environment:`

_$ mkvirtualenv my_project_   (This creates the my_project folder inside ~/Envs.)

`Work on a virtual environment:(This will deactivate other environemnt)`

_$ workon my_project_

`Deactivating is still the same:`

_$ deactivate_

`To delete:`

_$ rmvirtualenv venv_

`List all of the environments.`

_$ lsvirtualenv_

`Create both virutal Envirnment and project`

_$ mkproject myproject_



##ACTIVATE FROM INTELLIJ

`Goto File >>Project Structure >> Virutal Environment `

