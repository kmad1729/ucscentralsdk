"""This module contains the general information for FcpoolBlock ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class FcpoolBlockConsts():
    CONFIG_SCOPE_PRIVATE = "private"
    CONFIG_SCOPE_PUBLIC = "public"
    SCOPE_PRIVATE = "private"
    SCOPE_PUBLIC = "public"


class FcpoolBlock(ManagedObject):
    """This is FcpoolBlock class."""

    consts = FcpoolBlockConsts()
    naming_props = set([u'from', u'to'])

    mo_meta = MoMeta("FcpoolBlock", "fcpoolBlock", "block-[r_from]-[to]", VersionMeta.Version101a, "InputOutput", 0x7f, [], ["admin", "ls-storage-policy"], [u'fcpoolInitiators'], [u'fcpoolBootTarget'], ["Add", "Get", "Remove"])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_scope": MoPropertyMeta("config_scope", "configScope", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["private", "public"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "r_from": MoPropertyMeta("r_from", "from", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "scope": MoPropertyMeta("scope", "scope", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["private", "public"], []), 
        "size": MoPropertyMeta("size", "size", "uint", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "to": MoPropertyMeta("to", "to", "string", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x40, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "childAction": "child_action", 
        "configScope": "config_scope", 
        "dn": "dn", 
        "from": "r_from", 
        "qualifier": "qualifier", 
        "rn": "rn", 
        "scope": "scope", 
        "size": "size", 
        "status": "status", 
        "to": "to", 
    }

    def __init__(self, parent_mo_or_dn, r_from, to, **kwargs):
        self._dirty_mask = 0
        self.r_from = r_from
        self.to = to
        self.assigned = None
        self.child_action = None
        self.config_scope = None
        self.qualifier = None
        self.scope = None
        self.size = None
        self.status = None

        ManagedObject.__init__(self, "FcpoolBlock", parent_mo_or_dn, **kwargs)

