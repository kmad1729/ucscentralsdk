"""This module contains the general information for FirmwareInfraPackConfig ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class FirmwareInfraPackConfigConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    UPDATE_TRIGGER_IMMEDIATE = "immediate"


class FirmwareInfraPackConfig(ManagedObject):
    """This is FirmwareInfraPackConfig class."""

    consts = FirmwareInfraPackConfigConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FirmwareInfraPackConfig", "firmwareInfraPackConfig", "fw-infra-pack-config[name]", None, "InputOutput", 0x3ff, [], ["admin", "operations"], [u'firmwareProductFamily', u'orgDomainGroup', u'orgOrg'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", None, MoPropertyMeta.READ_WRITE, 0x2, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "infra_bundle_name": MoPropertyMeta("infra_bundle_name", "infraBundleName", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "infra_bundle_version": MoPropertyMeta("infra_bundle_version", "infraBundleVersion", "string", None, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", None, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", None, MoPropertyMeta.NAMING, 0x20, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []), 
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", None, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x100, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", None, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "infraBundleName": "infra_bundle_name", 
        "infraBundleVersion": "infra_bundle_version", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "stageSize": "stage_size", 
        "status": "status", 
        "updateTrigger": "update_trigger", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.infra_bundle_name = None
        self.infra_bundle_version = None
        self.int_id = None
        self.mode = None
        self.policy_level = None
        self.policy_owner = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareInfraPackConfig", parent_mo_or_dn, **kwargs)

