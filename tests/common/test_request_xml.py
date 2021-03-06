# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

from nose.tools import *
from ..connection.info import custom_setup, custom_teardown

handle = None


def setup():
    global handle
    handle = custom_setup()


def teardown():
    custom_teardown(handle)

to_commit = {}


def commit():
    from ucscentralsdk.ucscentralbasetype import ConfigMap, Dn, DnSet, Pair
    import ucscentralsdk.ucscentralmethodfactory as mf
    import ucscentralsdk.ucscentralxmlcodec as xc

    global to_commit

    refresh_dict = {}
    mo_dict = to_commit
    if not mo_dict:
        print("No Mo to be Committed")
        return None

    config_map = ConfigMap()
    for mo_dn in mo_dict:
        mo = mo_dict[mo_dn]
        child_list = mo.child
        while len(child_list) > 0:
            current_child_list = child_list
            child_list = []
            for child_mo in current_child_list:
                if child_mo.is_dirty():
                    refresh_dict[child_mo.dn] = child_mo
                child_list.extend(child_mo.child)

        pair = Pair()
        pair.key = mo_dn
        pair.child_add(mo_dict[mo_dn])
        config_map.child_add(pair)

    xml_element = mf.config_conf_mos("cookie", config_map, False)
    xml_str = xc.to_xml_str(xml_element)
    to_commit = {}
    return xml_str


def add_mo(mo, modify_present=False):
    import ucscentralsdk.ucscentralgenutils as ucscentralgenutils
    global to_commit

    if modify_present in ucscentralgenutils.AFFIRMATIVE_LIST:
        mo.status = "created,modified"
    else:
        mo.status = "created"
    to_commit[mo.dn] = mo


def set_mo(mo):
    global to_commit

    if mo.is_dirty():
        mo.status = "modified"
        to_commit[mo.dn] = mo
    else:
        print("Nothing Modified")


def test_001_add_sp():
    from ucscentralsdk.mometa.ls.LsServer import LsServer
    sp = LsServer(parent_mo_or_dn="org-root", name="test_sp")
    add_mo(mo=sp)
    xml_str = commit()
    print(xml_str)

    expected = (b'''<configConfMos cookie="cookie" inHierarchical="false"><inConfigs><pair key="org-root/ls-test_sp">'''
    + b'''<lsServer dn="org-root/ls-test_sp" name="test_sp" status="created" /></pair></inConfigs></configConfMos>''')
    assert_equal(xml_str, expected)


def test_002_add_hierarchy():
    from ucscentralsdk.mometa.org.OrgOrg import OrgOrg
    from ucscentralsdk.mometa.ls.LsServer import LsServer

    org = OrgOrg(parent_mo_or_dn="org-root", name="test_org")
    sp = LsServer(parent_mo_or_dn=org, name="test_sp")
    add_mo(mo=org)
    xml_str = commit()
    print(xml_str)

    expected = (b'''<configConfMos cookie="cookie" inHierarchical="false"><inConfigs>''' +
    b'''<pair key="org-root/org-test_org"><orgOrg dn="org-root/org-test_org" name="test_org" status="created">''' +
    b'''<lsServer dn="org-root/org-test_org/ls-test_sp" name="test_sp" /></orgOrg></pair></inConfigs></configConfMos>''')
    assert_equal(xml_str, expected)


@with_setup(setup, teardown)
def test_003_get_org_and_add_sp_add_mo_sp():
    from ucscentralsdk.mometa.ls.LsServer import LsServer

    org = handle.query_dn("org-root")
    sp = LsServer(parent_mo_or_dn=org, name="test_sp")

    add_mo(sp)
    xml_str = commit()
    print(xml_str)

    expected = (b'''<configConfMos cookie="cookie" inHierarchical="false"><inConfigs><pair key="org-root/ls-test_sp">'''
    + b'''<lsServer dn="org-root/ls-test_sp" name="test_sp" status="created" /></pair></inConfigs></configConfMos>''')
    assert_equal(xml_str, expected)


@with_setup(setup, teardown)
def test_004_get_org_and_add_sp_set_mo_org():
    from ucscentralsdk.mometa.ls.LsServer import LsServer

    org = handle.query_dn("org-root")
    sp = LsServer(parent_mo_or_dn=org, name="test_sp")

    set_mo(org)
    xml_str = commit()
    print(xml_str)

    expected = (b'''<configConfMos cookie="cookie" inHierarchical="false"><inConfigs><pair key="org-root">''' +
    b'''<orgOrg dn="org-root" status="modified"><lsServer dn="org-root/ls-test_sp" name="test_sp" />''' +
    b'''</orgOrg></pair></inConfigs></configConfMos>''')
    assert_equal(xml_str, expected)


@with_setup(setup, teardown)
def test_005_add_sp_hw():
    from ucscentralsdk.mometa.ls.LsServer import LsServer

    sp = LsServer(parent_mo_or_dn="org-root", name="test_sp")
    handle.remove_mo(sp)
    handle.commit()
    handle.add_mo(sp)
    handle.commit()

    test_sp = handle.query_dn("org-root/ls-test_sp")
    test_sp.descr = "update_description"
    handle.set_mo(test_sp)
    handle.commit()

    test_sp = handle.query_dn("org-root/ls-test_sp")

    handle.remove_mo(sp)
    handle.commit()

    expected = '''update_description'''
    assert_equal(test_sp.descr, expected)


@with_setup(setup, teardown)
def test_005_add_hierarchy_hw():
    from ucscentralsdk.mometa.org.OrgOrg import OrgOrg
    from ucscentralsdk.mometa.ls.LsServer import LsServer

    org = OrgOrg(parent_mo_or_dn="org-root", name="test_org")

    handle.remove_mo(org)
    handle.commit()
    handle.add_mo(org)
    handle.commit()
    sp = LsServer(parent_mo_or_dn=org, name="test_sp")
    handle.add_mo(sp)
    handle.commit()

    test_sp = handle.query_dn("org-root/org-test_org/ls-test_sp")
    test_sp.descr = "update_description"
    handle.set_mo(test_sp)
    handle.commit()
    test_sp = handle.query_dn("org-root/org-test_org/ls-test_sp")

    handle.remove_mo(sp)
    handle.commit()
    handle.remove_mo(org)
    handle.commit()

    expected = "update_description"
    assert_equal(test_sp.descr, expected)
