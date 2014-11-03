"""
Support external plug-ins without dealing with package or directory problems.
Doing:

  from weblabdeusto_devices.ext.archimedes import foo

Will internally do:

  from wldevices_archimedes import foo

We use the flask.exthook to do this.
"""

import archimedes
assert archimedes is not None # pyflakes warning

def setup():
    from flask.exthook import ExtensionImporter
    importer = ExtensionImporter(['wldevices_%s'], __name__)
    importer.install()

setup()
del setup
