"""This module contains the general information for HcItemNote ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class HcItemNoteConsts():
    pass


class HcItemNote(ManagedObject):
    """This is HcItemNote class."""

    consts = HcItemNoteConsts()
    naming_props = set([u'refItemId', u'id'])

    mo_meta = MoMeta("HcItemNote", "hcItemNote", "note-[ref_item_id]-[id]", None, "InputOutput", 0x7f, [], ["admin"], [u'hcAdapterFirmwareItem', u'hcAdapterItem', u'hcDriverItem', u'hcOsItem'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "uint", None, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "note": MoPropertyMeta("note", "note", "string", None, MoPropertyMeta.READ_WRITE, 0x8, 0, 510, None, [], []), 
        "ref_item_id": MoPropertyMeta("ref_item_id", "refItemId", "ulong", None, MoPropertyMeta.NAMING, 0x10, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "note": "note", 
        "refItemId": "ref_item_id", 
        "rn": "rn", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, ref_item_id, id, **kwargs):
        self._dirty_mask = 0
        self.ref_item_id = ref_item_id
        self.id = id
        self.child_action = None
        self.note = None
        self.status = None

        ManagedObject.__init__(self, "HcItemNote", parent_mo_or_dn, **kwargs)

