# -*- coding: utf-8 -*-
"""
``javaproperties`` provides support for reading & writing Java ``.properties``
files (both the "plain" format and XML) with a simple API based on the ``json``
module — though, for recovering Java addicts, it also includes a ``Properties``
class intended to match the behavior of Java 8's ``java.net.Properties`` as
much as is Pythonically possible.

Visit <https://github.com/jwodder/javaproperties> for more information.
"""

from .propclass import Properties
from .reading   import load, loads, parse, unescape
from .writing   import dump, dumps, join_key_value, escape, to_comment
from .xml       import load_xml, loads_xml, dump_xml, dumps_xml

__version__      = '0.1.0.dev1'
__author__       = 'John Thorvald Wodder II'
__author_email__ = 'javaproperties@varonathe.org'
__license__      = 'MIT'
__url__          = 'https://github.com/jwodder/javaproperties'

__all__ = [
    'Properties',
    'dump',
    'dump_xml',
    'dumps',
    'dumps_xml',
    'escape',
    'join_key_value',
    'load',
    'load_xml',
    'loads',
    'loads_xml',
    'parse',
    'to_comment',
    'unescape',
]
