
"""
Api solidedge 
=======================

"""

import clr

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

import sys
import SolidEdgeFramework as SEFramework
import SolidEdgePart as SEPart
import SolidEdgeConstants as SEConstants
import System.Runtime.InteropServices as SRI

class Api():

    def __init__(self):
        # Connect to a running instance of Solid Edge
        self.api = SRI.Marshal.GetActiveObject("SolidEdge.Application")

    def check_valid_version(self, *valid_version):
        #validate solidedge version - 'Solid Edge ST7'
        print("version solidedge: %s" %self.api.Value)
        assert self.api.Value in valid_version, "Unvalid version of solidedge"

    def active_document(self):
        return self.api.ActiveDocument
    
    def open_document(self, path_to_item):
        return self.document.Open(path_to_item)

    def close_document(self):
        return self.document.Close()

    @property
    def name(cls, part):
        return cls.part.Name


class HoleCollection():

    def __init__(self, doc):
        self.holes = doc.HoleDataCollection
        self.count = self.holes.Count

    def threaded(self):
        return (hole for hole in self.holes if hole.SubType=="Standard Thread")
