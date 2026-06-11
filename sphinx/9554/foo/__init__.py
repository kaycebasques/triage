from pathlib import Path


HOMEDIR_MODULE_ATTRIBUTE = Path.home()
"""Path object as a module attribute"""


class Foo:
    """class that contains a Path object as an attribute"""

    homedir_class_attribute = Path.home()
    """Path object as a class attribute"""
