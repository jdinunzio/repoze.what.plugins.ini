repoze.what.plugins.ini -- Plugin for repoze.what authorization framework
=========================================================================

    What is repoze.what.plugins.ini?
    --------------------------------

    repoze.what.plugins.ini is a plugin for repoze.what that offers group and
    permissions adapters for sources based on INI files.


    What is repoze.what?
    --------------------

    From repoze.what site:

        repoze.what is an authorization framework for WSGI applications, based
        on repoze.who (which deals with authentication).

        On the one hand, it enables an authorization system based on the groups 
        to which the authenticated or anonymous user belongs and the permissions 
        granted to such groups by loading these groups and permissions into the 
        request on the way in to the downstream WSGI application.

        And on the other hand, it enables you to manage your groups and 
        permissions from the application itself or another program, under a 
        backend-independent API. For example, it would be easy for you to switch 
        from one back-end to another, and even use this framework to migrate the
        data.

    repoze.what can be used as authorization framework for turbogear, repoze.bfg 
    or your own WSGI server.
            

    How to install repoze.what.plugins.ini?
    ---------------------------------------

    You can install the last stable version with easy_install::


        easy_install repoze.what.plugins.ini


    or the developer version via git::


        git clone git://github.com/jdinuncio/repoze.what.plugins.ini.git
        cd repoze.what.plugins.ini
        python setup.py install


    The source file format
    ----------------------

    The format used in the source files is similar to the INI file format. The 
    file consists in a serie of sections, each one with a section header of the 
    form “[section-name]”, followed by entries of the form “value”. Spaces 
    before and after section headers or entries are ignored. Characters after 
    ”#” are ignored.

    An example of a group file::


        [admins]
        rms

        [developers]
        rms
        linus

        [trolls]
        sballmer

        [python]
        [php]


    An example of a permissions file:


        [see-site]
        trolls

        [edit-site]
        admins
        developers

        [commit]
        developers


    How to use it?
    --------------
                  
    All you need to do is to instantiate a repoze.what middleware using 
    repoze.what.plugins.ini.INIGroupAdapter or 
    repoze.what.plugins.ini.INIPermissionsAdapter::

       
        # First, we'll need a WSGI application
        my_app = None   # Of course, you'll change None for your WSGI app

        # We need to set up the repoze.who components used by repoze.what for
        # authentication
        from repoze.who.plugins.htpasswd import HTPasswdPlugin, crypt_check
        from repoze.who.plugins.basicauth import BasicAuthPlugin

        htpasswd = HTPasswdPlugin('passwd', crypt_check)
        basicauth = BasicAuthPlugin('MyRepoze')
        identifiers = [('basicauth', basicauth)]
        authenticators = [('htpasswd', htpasswd)]
        challengers = [('basicauth', basicauth)]
        mdproviders = []

        # We'll use group and permission based exclusively on INI files
        from repoze.what.plugins.ini import INIGroupAdapter
        from repoze.what.plugins.ini import INIPermissionsAdapter

        groups = {'all_groups': INIGroupAdapter('groups.ini')}
        permissions = {'all_perms': INIPermissionsAdapter('permissions.ini')}

        # Finally, we create the repoze.what middleware
        import logging

        from repoze.what.middleware import setup_auth

        middleware = setup_auth(
            app = my_app,
            group_adapters = groups,
            permission_adapters = permissions, 
            identifiers = identifiers, 
            authenticators = authenticators,
            challengers = challengers, 
            mdproviders = mdproviders, 
            log_level = logging.DEBUG
            )

