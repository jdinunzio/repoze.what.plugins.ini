# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008, José Dinuncio <jdinunci@uc.edu.ve>
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

'''Test suite for the INI plugin.'''

import os.path
import unittest

from repoze.what.adapters.testutil import GroupsAdapterTester
from repoze.what.adapters.testutil import PermissionsAdapterTester

from repoze.what.plugins.ini import INIGroupAdapter
from repoze.what.plugins.ini import INIPermissionsAdapter


class TestINIGroupAdapterTester(GroupsAdapterTester, unittest.TestCase):
    '''Test Suite for INI group source adapter.'''
    def setUp(self):
        super(TestINIGroupAdapterTester, self).setUp()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        fake_groups = os.path.join(current_dir, 'groups.ini')
        self.adapter = INIGroupAdapter(fake_groups)


class TestINIPermissionsTester(PermissionsAdapterTester, unittest.TestCase):
    '''Test Suite for INI permission source adapter.'''
    def setUp(self):
        super(TestINIPermissionsAdapterTester, self).setUp()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        fake_permissions = os.path.join(current_dir, 'permissions.ini')
        self.adapter = INIPermissionsAdapter(fake_permissions)

