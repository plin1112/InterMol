import simtk.unit as units

from intermol.decorators import accepts_compatible_units
from intermol.forces.abstract_bond_type import AbstractBondType


class HarmonicBondType(AbstractBondType):
    __slots__ = ['length', 'k', 'order', 'c']

    @accepts_compatible_units(None, None, 
                              length=units.nanometers,
                              k=units.kilojoules_per_mole * units.nanometers ** (-2),
                              order=None,
                              c=None)
    def __init__(self, bondingtype1, bondingtype2, 
                 length=0.0 * units.nanometers,
                 k=0.0 * units.kilojoules_per_mole * units.nanometers ** (-2),
                 order=1, c=False):
        AbstractBondType.__init__(self, bondingtype1, bondingtype2, order, c)
        self.length = length
        self.k = k


# if __name__ == '__main__':
#     hb = HarmonicBondType("BT1","BT2", length=10 * units.nanometers)