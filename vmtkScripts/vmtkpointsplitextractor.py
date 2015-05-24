#!/usr/bin/env python

## Program:   VMTK
## Module:    $RCSfile: vmtkpointSplitextractor.py,v $
## Language:  Python
## Date:      $Date: 2006/03/01 11:54:16 $
## Version:   $Revision: 1.9 $

##   Copyright (c) Luca Antiga, David Steinman. All rights reserved.
##   See LICENCE file for details.

##      This software is distributed WITHOUT ANY WARRANTY; without even 
##      the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
##      PURPOSE.  See the above copyright notices for more information.


import vtk
import vtkvmtk
import sys

import pypes

vmtkpointsplitextractor = 'vmtkPointSplitExtractor'

class vmtkPointSplitExtractor(pypes.pypeScript):

    def __init__(self):

        pypes.pypeScript.__init__(self)
        
        self.Centerlines = None

        self.RadiusArrayName = ''

        self.GroupIdsArrayName = 'GroupIds'
        self.CenterlineIdsArrayName = 'CenterlineIds'
        self.BlankingArrayName = 'Blanking'
        self.TractIdsArrayName = 'TractIds'

        self.SplitPoint = [0.0,0.0,0.0]
        self.GapLength = 1.0
        self.Tolerance = 1E-4

        self.SetScriptName('vmtkpointsplitextractor')
        self.SetInputMembers([
            ['Centerlines','i','vtkPolyData',1,'','','vmtksurfacereader'],
            ['GroupIdsArrayName','groupidsarray','str',1],
            ['TractIdsArrayName','tractidsarray','str',1],
            ['CenterlineIdsArrayName','centerlineidsarray','str',1],
            ['RadiusArrayName','radiusarray','str',1],
      	    ['BlankingArrayName','blankingarray','str',1],
      	    ['SplitPoint','splitpoint','float',3],
      	    ['GapLength','gaplength','float',1,'(0.0,)'],
      	    ['Tolerance','tolerance','float',1,'(0.0,)']
            ])
        self.SetOutputMembers([
            ['Centerlines','o','vtkPolyData',1,'','','vmtksurfacewriter'],
            ['GroupIdsArrayName','groupidsarray','str',1],
            ['TractIdsArrayName','tractidsarray','str',1],
            ['CenterlineIdsArrayName','centerlineidsarray','str',1],
      	    ['BlankingArrayName','blankingarray','str',1]
            ])

    def Execute(self):

        if self.Centerlines == None:
            self.PrintError('Error: No input centerlines.')

        pointSplitExtractor = vtkvmtk.vtkvmtkCenterlineSplitExtractor()
        pointSplitExtractor.SetInputData(self.Centerlines)
        pointSplitExtractor.SetRadiusArrayName(self.RadiusArrayName)
        pointSplitExtractor.SetGroupIdsArrayName(self.GroupIdsArrayName)
        pointSplitExtractor.SetTractIdsArrayName(self.TractIdsArrayName)
        pointSplitExtractor.SetCenterlineIdsArrayName(self.CenterlineIdsArrayName)
      	pointSplitExtractor.SetBlankingArrayName(self.BlankingArrayName)
        pointSplitExtractor.SetSplitPoint(self.SplitPoint)
        pointSplitExtractor.SetGapLength(self.GapLength)
        pointSplitExtractor.SetTolerance(self.Tolerance)
        pointSplitExtractor.Update()

        self.Centerlines = pointSplitExtractor.GetOutputPort()



if __name__=='__main__':

    main = pypes.pypeMain()
    main.Arguments = sys.argv
    main.Execute()
