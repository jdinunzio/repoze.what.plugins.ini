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

"""
Plugin for repoze.what which sources are INI files.

This is a core plugin that provides ``source adapters`` for groups and
permissions stored in a format very similar to INI files.

TODO: Differences between the real INI files and these.

"""

from repoze.what.adapters import BaseSourceAdapter, SourceError

from repoze.what.plugins.ini.parser import parse_INIFile

__all__ = ['INIGroupAdapter', 'INIPermissionsAdapter']


class INIAdapter(BaseSourceAdapter):
    """Base class for INI File adapters."""

    def __init__(self, filename):
        """
        Create an INI file source adapter.

        @param filename: The filename with the sections information.

        """
        super(BaseSourceAdapter, self).__init__()
        self.filename = filename
        self.info = parse_INIFile(self.filename)


    def _get_all_sections(self):
        return self.info.keys()

    def _get_section_items(self, section):
        return set(sef.info[section])

    def _find_sections(self, hint):
        raise SourceError('This is implemented in the groups and '
                          'permissions adapters.')

    def _include_items(self, section, items):
        raise SourceError('For including items you must edit the '
                          'INI file directly.')

    def _exclude_items(self, section, items):
        raise SourceError('For excluding items you must edit the '
                          'INI file directly.')

    def _item_is_included(self, section, item):
        return item in self.info[section]

    def _create_section(self, section):
        raise SourceError('For create a new section you must edit the '
                          'INI file directly.')

    def _edit_section(self, section, new_section):
        raise SourceError('For edit a section you must edit the '
                          'INI file directly.')

    def _delete_section(self, section):
        raise SourceError('For delete a section you must edit the '
                          'INI file directly.')

    def _section_exists(self, section):
        return section in self.info


class INIGroupAdapter(INIAdapter):
    """INI Group Adapter."""

    def __init__(self, filename):
        """
        Create an INI group adapter.

        @param filename: The filename with the sections information.

        """
        super(INIGroupAdapter, self).__init__(filename)

    def _find_sections(self, hint):
        userid = hint['repoze.who.userid']
        answer = []
        for section in self.info.keys():
            if userid in self.info[section]:
                answer.append(section)
        return answer


class INIPermissionsAdapter(INIAdapter):
    """INI Permissions Adapters."""

    def __init__(self, filename):
        """
        Create an INI permissions adapter.

        @param filename: The filename with the sections information.

        """
        super(INIPermissionsAdapter, self).__init__(filename)

    def _find_sections(self, hint):
        answer = []
        for section in self.info.keys():
            if hint in self.info[section]:
                answer.append(section)
        return answer


