"""This module contains the general information for EquipmentPool ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class EquipmentPoolConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    POOL_TYPE_NON_QUALIFER = "non-qualifer"
    POOL_TYPE_QUALIFER = "qualifer"


class EquipmentPool(ManagedObject):
    """This is EquipmentPool class."""

    consts = EquipmentPoolConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("EquipmentPool", "equipmentPool", "equipment-pool-[name]", None, "InputOutput", 0x3f, [], ["read-only"], [u'orgOrg'], [], [None])

    prop_meta = {
        "assigned": MoPropertyMeta("assigned", "assigned", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", None, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", None, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", None, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", None, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "pool_type": MoPropertyMeta("pool_type", "poolType", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["non-qualifer", "qualifer"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "size": MoPropertyMeta("size", "size", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "assigned": "assigned", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "poolType": "pool_type", 
        "rn": "rn", 
        "size": "size", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.assigned = None
        self.child_action = None
        self.descr = None
        self.flt_aggr = None
        self.int_id = None
        self.policy_level = None
        self.policy_owner = None
        self.pool_type = None
        self.size = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentPool", parent_mo_or_dn, **kwargs)

