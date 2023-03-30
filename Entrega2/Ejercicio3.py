import string
jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""
jupyter_info = jupyter_info.lower().split()
letra = input("Ingrese una letra:\n")
if letra in string.ascii_letters:
    for i in jupyter_info:
        if(i.startswith(letra)):
            print(i)
else:
    print("Tiene que ingresar una letra")
