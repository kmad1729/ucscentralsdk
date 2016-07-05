"""This module contains the general information for CallhomeHttp ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class CallhomeHttpConsts():
    pass


class CallhomeHttp(ManagedObject):
    """This is CallhomeHttp class."""

    consts = CallhomeHttpConsts()
    naming_props = set([])

    mo_meta = MoMeta("CallhomeHttp", "callhomeHttp", "http", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["admin", "operations"], [u'callhomeEp'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "url": MoPropertyMeta("url", "url", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "url": "url", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.url = None

        ManagedObject.__init__(self, "CallhomeHttp", parent_mo_or_dn, **kwargs)

