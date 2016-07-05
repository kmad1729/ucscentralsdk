"""This module contains the general information for LsbootSanImage ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class LsbootSanImageConsts():
    pass


class LsbootSanImage(ManagedObject):
    """This is LsbootSanImage class."""

    consts = LsbootSanImageConsts()
    naming_props = set([u'type'])

    mo_meta = MoMeta("LsbootSanImage", "lsbootSanImage", "san-[type]", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], [u'lsbootStorage'], [u'lsbootSanImagePath'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []), 
        "vnic_name": MoPropertyMeta("vnic_name", "vnicName", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "vnicName": "vnic_name", 
    }

    def __init__(self, parent_mo_or_dn, type, **kwargs):
        self._dirty_mask = 0
        self.type = type
        self.child_action = None
        self.status = None
        self.vnic_name = None

        ManagedObject.__init__(self, "LsbootSanImage", parent_mo_or_dn, **kwargs)

