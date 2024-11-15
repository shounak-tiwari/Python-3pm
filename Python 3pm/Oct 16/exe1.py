"""
Exception in python :

"""
import py_compile

# Compiling a single Python file
py_compile.compile('exe1.py')


print("hello python")
# Or compiling all .py files in a directory
py_compile.compile('exe1.py', cfile='output.pyc')
