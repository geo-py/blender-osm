import math
from . import Roof


gabledProfile = (
    (0., 0.),
    (0.5, 1.),
    (1., 0.)
)

roundProfile = (
    (0., 0.),
    (0.01, 0.098),
    (0.038, 0.191),
    (0.084, 0.278),
    (0.146, 0.354),
    (0.222, 0.416),
    (0.309, 0.462),
    (0.402, 0.49),
    (0.5, 0.5),
    (0.598, 0.49),
    (0.691, 0.462),
    (0.778, 0.416),
    (0.854, 0.354),
    (0.916, 0.278),
    (0.962, 0.191),
    (0.99, 0.098),
    (1., 0.)
)

gambrelProfile = (
    (0., 0.),
    (0.2, 0.6),
    (0.5, 1.),
    (0.8, 0.6),
    (1., 0.)
)

saltboxProfile = (
    (0., 0.),
    (0.35, 1.),
    (0.65, 1.),
    (1., 0.)
)


class RoofProfile(Roof):
    
    defaultHeight = 10.
    
    def __init__(self, profile, numSamples):
        super().__init__()
        self.profile = profile
        self.numSamples = numSamples
        
        # quantize <profile> with <numSamples>
        _profile = tuple(math.ceil(p[0]*numSamples) for p in profile)
        profileQ = []
        index = 0
        for i in range(numSamples):
            if i >= _profile[index+1]:
                index += 1  
            profileQ.append(index)
        profileQ.append(len(_profile)-1)
        self.profileQ = profileQ
    
    def make(self, bldgMaxHeight, roofMinHeight, bldgMinHeight, osm):
        verts = self.verts
        polygon = self.polygon
        indices = polygon.indices
        
        _v = self.sampleProfile(verts[indices[0]])
        for i in range(1, polygon.n):
            v = self.sampleProfile(verts[indices[i]])
            _v = v
    
    def sampleProfile(self):
        pass