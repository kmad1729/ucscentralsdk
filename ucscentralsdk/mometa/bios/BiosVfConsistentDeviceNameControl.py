"""This module contains the general information for BiosVfConsistentDeviceNameControl ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class BiosVfConsistentDeviceNameControlConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_CDNCONTROL_DISABLED = "disabled"
    VP_CDNCONTROL_ENABLED = "enabled"
    VP_CDNCONTROL_PLATFORM_DEFAULT = "platform-default"
    VP_CDNCONTROL_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfConsistentDeviceNameControl(ManagedObject):
    """This is BiosVfConsistentDeviceNameControl class."""

    consts = BiosVfConsistentDeviceNameControlConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfConsistentDeviceNameControl", "biosVfConsistentDeviceNameControl", "Consistent-Device-Name-Control", VersionMeta.Version141a, "InputOutput", 0x1f, [], ["read-only"], [u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version141a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_cdn_control": MoPropertyMeta("vp_cdn_control", "vpCDNControl", "string", VersionMeta.Version141a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpCDNControl": "vp_cdn_control", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.supported_by_default = None
        self.vp_cdn_control = None

        ManagedObject.__init__(self, "BiosVfConsistentDeviceNameControl", parent_mo_or_dn, **kwargs)

