import doctest
import importlib
import pkgutil
import unittest

import pydocxresizeimages


def load_tests(loader, tests, pattern):
    """Add doctests from every module in the package to unittest discovery."""
    suite = unittest.TestSuite()

    for module_info in pkgutil.walk_packages(
        pydocxresizeimages.__path__,
        prefix=pydocxresizeimages.__name__ + '.',
    ):
        module = importlib.import_module(module_info.name)
        suite.addTests(doctest.DocTestSuite(module))

    return suite
