"""This module contains the general information for FirmwareChassisPack ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class FirmwareChassisPackConsts():
    FORCE_DEPLOY_FALSE = "false"
    FORCE_DEPLOY_NO = "no"
    FORCE_DEPLOY_TRUE = "true"
    FORCE_DEPLOY_YES = "yes"
    INT_ID_NONE = "none"
    OVERRIDE_DEFAULT_EXCLUSION_FALSE = "false"
    OVERRIDE_DEFAULT_EXCLUSION_NO = "no"
    OVERRIDE_DEFAULT_EXCLUSION_TRUE = "true"
    OVERRIDE_DEFAULT_EXCLUSION_YES = "yes"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    POLICY_OWNER_UNSPECIFIED = "unspecified"
    UPDATE_TRIGGER_IMMEDIATE = "immediate"


class FirmwareChassisPack(ManagedObject):
    """This is FirmwareChassisPack class."""

    consts = FirmwareChassisPackConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FirmwareChassisPack", "firmwareChassisPack", "fw-chassis-pack-[name]", None, "InputOutput", 0xfff, [], ["read-only"], [u'orgDomainGroup', u'orgOrg'], [u'firmwareExcludeChassisComponent'], [None])

    prop_meta = {
        "chassis_bundle_name": MoPropertyMeta("chassis_bundle_name", "chassisBundleName", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "chassis_bundle_version": MoPropertyMeta("chassis_bundle_version", "chassisBundleVersion", "string", None, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", None, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "force_deploy": MoPropertyMeta("force_deploy", "forceDeploy", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", None, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", None, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", None, MoPropertyMeta.NAMING, 0x40, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "override_default_exclusion": MoPropertyMeta("override_default_exclusion", "overrideDefaultExclusion", "string", None, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["false", "no", "true", "yes"], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", None, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local", "pending-policy", "policy", "unspecified"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "stage_size": MoPropertyMeta("stage_size", "stageSize", "ushort", None, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x400, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "update_trigger": MoPropertyMeta("update_trigger", "updateTrigger", "string", None, MoPropertyMeta.READ_WRITE, 0x800, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", ["immediate"], []), 
    }

    prop_map = {
        "chassisBundleName": "chassis_bundle_name", 
        "chassisBundleVersion": "chassis_bundle_version", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "forceDeploy": "force_deploy", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "overrideDefaultExclusion": "override_default_exclusion", 
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
        self.chassis_bundle_name = None
        self.chassis_bundle_version = None
        self.child_action = None
        self.descr = None
        self.force_deploy = None
        self.int_id = None
        self.mode = None
        self.override_default_exclusion = None
        self.policy_level = None
        self.policy_owner = None
        self.stage_size = None
        self.status = None
        self.update_trigger = None

        ManagedObject.__init__(self, "FirmwareChassisPack", parent_mo_or_dn, **kwargs)

