"""This module contains the general information for EquipmentChassisProfileAssocCtx ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class EquipmentChassisProfileAssocCtxConsts():
    pass


class EquipmentChassisProfileAssocCtx(ManagedObject):
    """This is EquipmentChassisProfileAssocCtx class."""

    consts = EquipmentChassisProfileAssocCtxConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentChassisProfileAssocCtx", "equipmentChassisProfileAssocCtx", "cp-assoc-ctx", None, "InputOutput", 0xf, [], ["read-only"], [u'equipmentChassisProfile'], [u'equipmentChassisAssocCtx'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentChassisProfileAssocCtx", parent_mo_or_dn, **kwargs)

