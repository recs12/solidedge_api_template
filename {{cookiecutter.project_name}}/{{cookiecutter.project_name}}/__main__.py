#!python3
# 2019-11-20 by: recs
""" Convert threads in holes from imperial to metric.
"""

import clr

clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

import sys
import SolidEdgeFramework as SEFramework
import SolidEdgePart as SEPart
import SolidEdgeConstants as SEConstants
import System.Runtime.InteropServices as SRI

from solidedge.holes import Hole
from solidedge.api import Api, HoleCollection

def main():
    try:
        session = Api()
        session.check_valid_version('Solid Edge ST7')
        plate = session.active_document()
        print("part: %s\n" % plate.name)

        # Check if part is sheetmetal.
        assert plate.name.endswith(".psm"), "This macro only works on .psm not %s" %plate.name[-4:]

        # Get a reference to the variables collection.
        holes = HoleCollection(plate)

        print("Total of holes: %s" %holes.count)
        for hole in holes.threaded():
            print(hole.name)
            o = Hole(hole)
            ## print(repr(o))
            imperial = o.size_hole()
            print(imperial)
            # holedata = Hole.get_equivalence(o)
            # o.conversion_to_metric(holedata)
            # metric = o.size_hole()
            #print("| imperial | metric |" %(imperial, metric))
            #print("==================")
            #print("| %s | %s |" %(imperial, metric))
    except AssertionError as err:
        print(err.args)
    except Exception as ex:
        print(ex.args)
    else:
        pass
    finally:
        raw_input("\n(Press any key to exit ;)")
        sys.exit()



if __name__ == "__main__":
    main()


# logging system
# print before and afer diameter in same line
# print my acronym on display macro
# in conversion add assertion
# caught all the exceptions