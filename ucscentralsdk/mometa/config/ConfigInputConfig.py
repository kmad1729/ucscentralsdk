"""This module contains the general information for ConfigInputConfig ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class ConfigInputConfigConsts():
    pass


class ConfigInputConfig(ManagedObject):
    """This is ConfigInputConfig class."""

    consts = ConfigInputConfigConsts()
    naming_props = set([u'inputName', u'inputConfigStatus'])

    mo_meta = MoMeta("ConfigInputConfig", "configInputConfig", "name-[input_name]status-[input_config_status]", VersionMeta.Version111a, "InputOutput", 0x3f, [], ["read-only"], [u'configInputConfigSet'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_dn": MoPropertyMeta("config_dn", "configDn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "input_config_status": MoPropertyMeta("input_config_status", "inputConfigStatus", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x4, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "input_name": MoPropertyMeta("input_name", "inputName", "string", VersionMeta.Version111a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configDn": "config_dn", 
        "dn": "dn", 
        "inputConfigStatus": "input_config_status", 
        "inputName": "input_name", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, input_name, input_config_status, **kwargs):
        self._dirty_mask = 0
        self.input_name = input_name
        self.input_config_status = input_config_status
        self.child_action = None
        self.config_dn = None
        self.status = None

        ManagedObject.__init__(self, "ConfigInputConfig", parent_mo_or_dn, **kwargs)

