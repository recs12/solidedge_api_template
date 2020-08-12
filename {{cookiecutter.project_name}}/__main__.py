# -*- coding: utf-8 -*-

"""
Template SolidEdge with Ironpython.
"""

import sys
import clr

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System")
clr.AddReference("System.Runtime.InteropServices")

import System
import System.Runtime.InteropServices as SRI
from System import Console
from System.IO import Directory
from System.IO.Path import Combine


def main():
    try:
        application = SRI.Marshal.GetActiveObject("SolidEdge.Application")
        asm = application.ActiveDocument
        print("Part: %s\n" % asm.Name)
        # asm.Type =>  plate :4 , assembly : 3, partdocument: 1
        assert asm.Type == 3, "This macro only works on .asm"

        # Start code here.


    except AssertionError as err:
        print(err.args)

    except Exception as ex:
        print(ex.args)

    finally:
        raw_input("\nPress any key to exit...")
        sys.exit()


def confirmation(func):
    response = raw_input("""Wanna create something? (Press y/[Y] to proceed.)""")
    if response.lower() not in ["y", "yes", "oui"]:
        print("Process canceled")
        sys.exit()
    else:
        func()


if __name__ == "__main__":
    confirmation(main)
