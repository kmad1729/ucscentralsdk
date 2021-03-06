"""This module contains the general information for EquipmentRequirement ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class EquipmentRequirementConsts():
    OPER_STATE_FAILED_TO_APPLY = "failed-to-apply"
    OPER_STATE_UNUSED = "unused"
    OPER_STATE_USED = "used"
    RESTRICT_MIGRATION_FALSE = "false"
    RESTRICT_MIGRATION_NO = "no"
    RESTRICT_MIGRATION_TRUE = "true"
    RESTRICT_MIGRATION_YES = "yes"


class EquipmentRequirement(ManagedObject):
    """This is EquipmentRequirement class."""

    consts = EquipmentRequirementConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentRequirement", "equipmentRequirement", "chassis-req", None, "InputOutput", 0x7f, [], ["admin", "pn-equipment", "pn-maintenance", "pn-policy", "read-only"], [u'equipmentChassisProfile'], [u'faultInst'], [None])

    prop_meta = {
        "assigned_to_dn": MoPropertyMeta("assigned_to_dn", "assignedToDn", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "chassis_dn": MoPropertyMeta("chassis_dn", "chassisDn", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "chassis_pool_dn": MoPropertyMeta("chassis_pool_dn", "chassisPoolDn", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "issues": MoPropertyMeta("issues", "issues", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|not-applicable|chassis-profile-not-supported|migration|non-interrupt-fsm-running|insufficient-resources|firmware-version-mismatch|physical-requirement|chassis-undiscovered|resource-ownership-conflict|chassis-unavailable|invalid-chassis-pack|missing-firmware-image|insufficient-power-budget),){0,13}(defaultValue|not-applicable|chassis-profile-not-supported|migration|non-interrupt-fsm-running|insufficient-resources|firmware-version-mismatch|physical-requirement|chassis-undiscovered|resource-ownership-conflict|chassis-unavailable|invalid-chassis-pack|missing-firmware-image|insufficient-power-budget){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", None, MoPropertyMeta.READ_WRITE, 0x4, None, None, r"""[\-\.:_a-zA-Z0-9]{0,32}""", [], []), 
        "oper_name": MoPropertyMeta("oper_name", "operName", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["failed-to-apply", "unused", "used"], []), 
        "qualifier": MoPropertyMeta("qualifier", "qualifier", "string", None, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "restrict_migration": MoPropertyMeta("restrict_migration", "restrictMigration", "string", None, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "assignedToDn": "assigned_to_dn", 
        "chassisDn": "chassis_dn", 
        "chassisPoolDn": "chassis_pool_dn", 
        "childAction": "child_action", 
        "dn": "dn", 
        "issues": "issues", 
        "name": "name", 
        "operName": "oper_name", 
        "operState": "oper_state", 
        "qualifier": "qualifier", 
        "restrictMigration": "restrict_migration", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.assigned_to_dn = None
        self.chassis_dn = None
        self.chassis_pool_dn = None
        self.child_action = None
        self.issues = None
        self.name = None
        self.oper_name = None
        self.oper_state = None
        self.qualifier = None
        self.restrict_migration = None
        self.status = None

        ManagedObject.__init__(self, "EquipmentRequirement", parent_mo_or_dn, **kwargs)

