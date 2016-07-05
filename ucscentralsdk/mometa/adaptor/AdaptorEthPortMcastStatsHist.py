"""This module contains the general information for AdaptorEthPortMcastStatsHist ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class AdaptorEthPortMcastStatsHistConsts():
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"


class AdaptorEthPortMcastStatsHist(ManagedObject):
    """This is AdaptorEthPortMcastStatsHist class."""

    consts = AdaptorEthPortMcastStatsHistConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("AdaptorEthPortMcastStatsHist", "adaptorEthPortMcastStatsHist", "[id]", VersionMeta.Version111a, "OutputOnly", 0xf, [], ["read-only"], [u'adaptorEthPortMcastStats'], [], [None])

    prop_meta = {
        "broadcast_packets": MoPropertyMeta("broadcast_packets", "broadcastPackets", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "broadcast_packets_delta": MoPropertyMeta("broadcast_packets_delta", "broadcastPacketsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "broadcast_packets_delta_avg": MoPropertyMeta("broadcast_packets_delta_avg", "broadcastPacketsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "broadcast_packets_delta_max": MoPropertyMeta("broadcast_packets_delta_max", "broadcastPacketsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "broadcast_packets_delta_min": MoPropertyMeta("broadcast_packets_delta_min", "broadcastPacketsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version111a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version111a, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "multicast_packets": MoPropertyMeta("multicast_packets", "multicastPackets", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "multicast_packets_delta": MoPropertyMeta("multicast_packets_delta", "multicastPacketsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "multicast_packets_delta_avg": MoPropertyMeta("multicast_packets_delta_avg", "multicastPacketsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "multicast_packets_delta_max": MoPropertyMeta("multicast_packets_delta_max", "multicastPacketsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "multicast_packets_delta_min": MoPropertyMeta("multicast_packets_delta_min", "multicastPacketsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version111a, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "unicast_packets": MoPropertyMeta("unicast_packets", "unicastPackets", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unicast_packets_delta": MoPropertyMeta("unicast_packets_delta", "unicastPacketsDelta", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unicast_packets_delta_avg": MoPropertyMeta("unicast_packets_delta_avg", "unicastPacketsDeltaAvg", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unicast_packets_delta_max": MoPropertyMeta("unicast_packets_delta_max", "unicastPacketsDeltaMax", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "unicast_packets_delta_min": MoPropertyMeta("unicast_packets_delta_min", "unicastPacketsDeltaMin", "ulong", VersionMeta.Version111a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
    }

    prop_map = {
        "broadcastPackets": "broadcast_packets", 
        "broadcastPacketsDelta": "broadcast_packets_delta", 
        "broadcastPacketsDeltaAvg": "broadcast_packets_delta_avg", 
        "broadcastPacketsDeltaMax": "broadcast_packets_delta_max", 
        "broadcastPacketsDeltaMin": "broadcast_packets_delta_min", 
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "multicastPackets": "multicast_packets", 
        "multicastPacketsDelta": "multicast_packets_delta", 
        "multicastPacketsDeltaAvg": "multicast_packets_delta_avg", 
        "multicastPacketsDeltaMax": "multicast_packets_delta_max", 
        "multicastPacketsDeltaMin": "multicast_packets_delta_min", 
        "rn": "rn", 
        "status": "status", 
        "suspect": "suspect", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
        "unicastPackets": "unicast_packets", 
        "unicastPacketsDelta": "unicast_packets_delta", 
        "unicastPacketsDeltaAvg": "unicast_packets_delta_avg", 
        "unicastPacketsDeltaMax": "unicast_packets_delta_max", 
        "unicastPacketsDeltaMin": "unicast_packets_delta_min", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.broadcast_packets = None
        self.broadcast_packets_delta = None
        self.broadcast_packets_delta_avg = None
        self.broadcast_packets_delta_max = None
        self.broadcast_packets_delta_min = None
        self.child_action = None
        self.most_recent = None
        self.multicast_packets = None
        self.multicast_packets_delta = None
        self.multicast_packets_delta_avg = None
        self.multicast_packets_delta_max = None
        self.multicast_packets_delta_min = None
        self.status = None
        self.suspect = None
        self.thresholded = None
        self.time_collected = None
        self.unicast_packets = None
        self.unicast_packets_delta = None
        self.unicast_packets_delta_avg = None
        self.unicast_packets_delta_max = None
        self.unicast_packets_delta_min = None

        ManagedObject.__init__(self, "AdaptorEthPortMcastStatsHist", parent_mo_or_dn, **kwargs)

