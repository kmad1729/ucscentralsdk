"""This module contains the general information for EquipmentLocalTemplDef ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class EquipmentLocalTemplDefConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    TYPE_INITIAL_TEMPLATE = "initial-template"
    TYPE_INSTANCE = "instance"
    TYPE_UPDATING_TEMPLATE = "updating-template"


class EquipmentLocalTemplDef(ManagedObject):
    """This is EquipmentLocalTemplDef class."""

    consts = EquipmentLocalTemplDefConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("EquipmentLocalTemplDef", "equipmentLocalTemplDef", "inst-[id]", None, "InputOutput", 0x7f, [], ["read-only"], [u'equipmentTemplate'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", None, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "flt_aggr": MoPropertyMeta("flt_aggr", "fltAggr", "ulong", None, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", None, MoPropertyMeta.NAMING, 0x8, None, None, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", None, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{1,128}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "system_name": MoPropertyMeta("system_name", "systemName", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["initial-template", "instance", "updating-template"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "fltAggr": "flt_aggr", 
        "id": "id", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "status": "status", 
        "systemName": "system_name", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.descr = None
        self.flt_aggr = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.status = None
        self.system_name = None
        self.type = None

        ManagedObject.__init__(self, "EquipmentLocalTemplDef", parent_mo_or_dn, **kwargs)

