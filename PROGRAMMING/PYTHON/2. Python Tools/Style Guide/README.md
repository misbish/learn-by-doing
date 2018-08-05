**PYTHON STYLE GUIDE**

_https://www.python.org/dev/peps/pep-0008/_


_Indentation_

`Use 4 spaces per indentation level`

`Space is preferred than tab`

`Python 3 disallows mixing the use of tabs and spaces for indentation.`

**NOTE**: 

When invoking the Python 2 command line interpreter with the -t option, it issues warnings about code that illegally mixes tabs and spaces. When using -tt these warnings become errors.

_Maximum Line Length_

`Limit all lines to a maximum of 79 characters.`

**NOTE**:
 
 IntelliJ IDEA 2018
      File > Settings... > Editor > Code Style > Hard wrap at


_Blank Lines_

`Surround top-level function and class definitions with two blank lines.`

`Method definitions inside a class are surrounded by a single blank line.`

_Source File Encoding_

`Code in the core Python distribution should always use UTF-8`

_Imports_

`Imports should usually be on separate lines:`
 
 Yes: import os
      import sys
      
 No:  import sys, os


`Imports should be grouped in the following order:`
 1. Standard library imports.
 2. Related third party imports.
 3. Local application/library specific imports.
 
`Absolute imports are recommended,However, explicit relative imports are an acceptable`

from mypkg import sibling

from . import sibling


`Implicit relative imports should never be used and have been removed in Python 3.`

`Wildcard imports (from <module> import *) should be avoided`

_Pet Peeves_

`Avoid extraneous whitespace in the following situations:`

_Naming Convention_

`Class names should normally use the CapWords convention.`

`Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability.`
 
`Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.`

`Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.`

`Function names should be lowercase, with words separated by underscores as necessary to improve readability.`

`Variable names follow the same convention as function names.`

`Use one leading underscore only for non-public methods and instance variables.`

**NOTE:** 

Always use self for the first argument to instance methods.
Always use cls for the first argument to class methods.