"""This module contains the general information for ExtpolController ManagedObject."""

from ...ucscentralmo import ManagedObject
from ...ucscentralcoremeta import UcsCentralVersion, MoPropertyMeta, MoMeta
from ...ucscentralmeta import VersionMeta


class ExtpolControllerConsts():
    CONN_PROTOCOL_IPV4 = "ipv4"
    CONN_PROTOCOL_IPV6 = "ipv6"
    CONN_PROTOCOL_UNKNOWN = "unknown"
    CONNECTION_STATE_CONNECTED = "connected"
    CONNECTION_STATE_LOST_CONNECTIVITY = "lost-connectivity"
    OPER_STATE_LOST_VISIBILITY = "lost-visibility"
    OPER_STATE_REGISTERED = "registered"
    OPER_STATE_REGISTERING = "registering"
    OPER_STATE_SYNCHRONIZING = "synchronizing"
    OPER_STATE_UNREGISTERED = "unregistered"
    OPER_STATE_VERSION_MISMATCH = "version-mismatch"
    TYPE_BOOT_MGR = "boot-mgr"
    TYPE_CENTRAL_MGR = "central-mgr"
    TYPE_IDENTIFIER_MGR = "identifier-mgr"
    TYPE_MANAGED_ENDPOINT = "managed-endpoint"
    TYPE_MGMT_CONTROLLER = "mgmt-controller"
    TYPE_OPERATION_MGR = "operation-mgr"
    TYPE_POLICY_MGR = "policy-mgr"
    TYPE_RESOURCE_AGGR = "resource-aggr"
    TYPE_RESOURCE_MGR = "resource-mgr"
    TYPE_SERVICE_REG = "service-reg"
    TYPE_STATS_MGR = "stats-mgr"
    TYPE_STORAGE_BROKER = "storage-broker"
    TYPE_VIRTUAL_SWITCHING_MGR = "virtual-switching-mgr"
    TYPE_VM_MGR = "vm-mgr"


class ExtpolController(ManagedObject):
    """This is ExtpolController class."""

    consts = ExtpolControllerConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("ExtpolController", "extpolController", "contro-[id]", VersionMeta.Version101a, "InputOutput", 0x1f, [], ["admin"], [u'extpolControllerCont'], [u'dupeEp', u'faultInst', u'observeObserved', u'policyPolicyScopeCont'], ["Get"])

    prop_meta = {
        "capability": MoPropertyMeta("capability", "capability", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr),){0,28}(defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr){0,1}""", [], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101a, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "conn_protocol": MoPropertyMeta("conn_protocol", "connProtocol", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ipv4", "ipv6", "unknown"], []), 
        "connection_state": MoPropertyMeta("connection_state", "connectionState", "string", VersionMeta.Version121a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["connected", "lost-connectivity"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "host": MoPropertyMeta("host", "host", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""^[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?$|^[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?)*(\.[A-Za-z]([A-Za-z0-9-]*[A-Za-z0-9])?)$|^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$""", [], []), 
        "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version101a, MoPropertyMeta.NAMING, 0x4, None, None, None, [], []), 
        "interest": MoPropertyMeta("interest", "interest", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr),){0,28}(defaultValue|unspecified|vmm|infra-waf|vm-mgr|pcm|infra-fw|org-mgr|virtual-switching-mgr|service-reg|vm-vasw|infra-pasw|vm-admin|infra-aggr|identifier-mgr|infra-slb|policy-mgr|stats-mgr|vm-fw|infra-pdsw|operation-mgr|infra-crypto-offloa|infra-was|boot-mgr|ipam|central-mgr|vm-slb|storage-broker|resource-mgr){0,1}""", [], []), 
        "ip": MoPropertyMeta("ip", "ip", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""((([0-9]){1,3}\.){3}[0-9]{1,3})""", [], []), 
        "ipv6": MoPropertyMeta("ipv6", "ipv6", "string", VersionMeta.Version112a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "last_poll_ts": MoPropertyMeta("last_poll_ts", "lastPollTs", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "oper_state": MoPropertyMeta("oper_state", "operState", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lost-visibility", "registered", "registering", "synchronizing", "unregistered", "version-mismatch"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, 0x8, 0, 256, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101a, MoPropertyMeta.READ_WRITE, 0x10, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["boot-mgr", "central-mgr", "identifier-mgr", "managed-endpoint", "mgmt-controller", "operation-mgr", "policy-mgr", "resource-aggr", "resource-mgr", "service-reg", "stats-mgr", "storage-broker", "virtual-switching-mgr", "vm-mgr"], []), 
        "version": MoPropertyMeta("version", "version", "string", VersionMeta.Version101a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "capability": "capability", 
        "childAction": "child_action", 
        "connProtocol": "conn_protocol", 
        "connectionState": "connection_state", 
        "dn": "dn", 
        "host": "host", 
        "id": "id", 
        "interest": "interest", 
        "ip": "ip", 
        "ipv6": "ipv6", 
        "lastPollTs": "last_poll_ts", 
        "name": "name", 
        "operState": "oper_state", 
        "rn": "rn", 
        "status": "status", 
        "type": "type", 
        "version": "version", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.capability = None
        self.child_action = None
        self.conn_protocol = None
        self.connection_state = None
        self.host = None
        self.interest = None
        self.ip = None
        self.ipv6 = None
        self.last_poll_ts = None
        self.name = None
        self.oper_state = None
        self.status = None
        self.type = None
        self.version = None

        ManagedObject.__init__(self, "ExtpolController", parent_mo_or_dn, **kwargs)

