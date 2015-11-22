# *-8 coding: utf-8 -*-
"""
Parse requirements file, and work out whether there are any updates.
"""
import requests
from semantic_version import Version


def package_url(package):
    """Return fully-qualified URL to package on PyPI (JSON endpoint)."""
    return u"http://pypi.python.org/pypi/%s/json" % package


def package_info(package_url):
    """Return latest package version from PyPI (as JSON)."""
    return requests.get(package_url).json().get('info')


def package_version(package_info):
    """Return the latest version from package_version as semver Version."""
    return Version(package_info.get('version'))


class PackageVersion(object):

    """A specific version of a package."""

    def __init__(self, name, version_string, **kwargs):
        self.name = name
        self.version_string = version_string
        self.uploaded_at = kwargs.pop('uploaded_at', None)

    def __unicode__(self):
        return u"Package: %s (%s)" % (self.name, self.version)

    def __str__(self):
        return unicode(self).encode('utf-8')

    @property
    def version(self):
        """Return a semantic_version.Version object."""
        return Version(self.version_string, partial=True)

    def diff(self, package_to_compare):
        """Return string representing the diff between package versions.

        We're interested in whether this is a major, minor, patch or 'other'
        update. This method will compare the two versions and return None if
        they are the same, else it will return a string value indicating the
        type of diff - 'major', 'minor', 'patch', 'other'.

        """
        version1 = self.version
        version2 = package_to_compare.version

        if version1 == version2:
            return None

        for v in ('major', 'minor', 'patch'):
            if getattr(version1, v) != getattr(version2, v):
                return v

        return 'other'
