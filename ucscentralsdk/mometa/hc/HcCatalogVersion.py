"""This module contains the general information for HcCatalogVersion ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class HcCatalogVersionConsts():
    IMPORT_METHOD_CISCO = "Cisco"
    IMPORT_METHOD_LOCAL = "local"


class HcCatalogVersion(ManagedObject):
    """This is HcCatalogVersion class."""

    consts = HcCatalogVersionConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("HcCatalogVersion", "hcCatalogVersion", "hc-catalog-version-[id]", None, "InputOutput", 0x3ff, [], ["admin"], [u'hcHolder'], [], [None])

    prop_meta = {
        "catalog_name": MoPropertyMeta("catalog_name", "catalogName", "string", None, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, [], []), 
        "catalog_updated_date": MoPropertyMeta("catalog_updated_date", "catalogUpdatedDate", "string", None, MoPropertyMeta.READ_WRITE, 0x4, 0, 510, None, [], []), 
        "catalog_version": MoPropertyMeta("catalog_version", "catalogVersion", "string", None, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "file_create_date": MoPropertyMeta("file_create_date", "fileCreateDate", "string", None, MoPropertyMeta.READ_WRITE, 0x20, 0, 510, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", None, MoPropertyMeta.NAMING, 0x40, None, None, None, [], []), 
        "import_method": MoPropertyMeta("import_method", "importMethod", "string", None, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Cisco", "local"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x100, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x200, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "catalogName": "catalog_name", 
        "catalogUpdatedDate": "catalog_updated_date", 
        "catalogVersion": "catalog_version", 
        "childAction": "child_action", 
        "dn": "dn", 
        "fileCreateDate": "file_create_date", 
        "id": "id", 
        "importMethod": "import_method", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.catalog_name = None
        self.catalog_updated_date = None
        self.catalog_version = None
        self.child_action = None
        self.file_create_date = None
        self.import_method = None
        self.status = None

        ManagedObject.__init__(self, "HcCatalogVersion", parent_mo_or_dn, **kwargs)

