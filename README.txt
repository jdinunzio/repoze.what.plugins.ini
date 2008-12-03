repoze.what.plugins.ini -- Plugin for repoze.what authorization framework
=========================================================================

repoze.what.plugins.ini is a plugin for repoze.what authorization framework
which sources are INI-like files.

An example of the file format for repoze.what.plugins.ini is given::

    [admins]
    rms

    [developers]
    # Here comes a comment
    rms

    linus # Yes, that one!

    [trolls]
    sballmer

    [python]
    [php]

