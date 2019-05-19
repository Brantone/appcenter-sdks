# coding: utf-8

"""
    App Center Client

    Microsoft Visual Studio App Center API  # noqa: E501

    OpenAPI spec version: preview
    Contact: benedetto.abbenanti@gmail.com
    Project Repository: https://github.com/b3nab/appcenter-sdks
"""

import pprint
import re  # noqa: F401

import six


class ReleaseDetailsUpdateRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'boolean',
        'release_notes': 'string',
        'build': 'object'
    }

    attribute_map = {
        'enabled': 'enabled',
        'release_notes': 'release_notes',
        'build': 'build'
    }

    def __init__(self, enabled=None, release_notes=None, build=None):  # noqa: E501
        """ReleaseDetailsUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._release_notes = None
        self._build = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if release_notes is not None:
            self.release_notes = release_notes
        if build is not None:
            self.build = build

    @property
    def enabled(self):
        """Gets the enabled of this ReleaseDetailsUpdateRequest.  # noqa: E501

        Toggle this release to be enable distribute/download or not.  # noqa: E501

        :return: The enabled of this ReleaseDetailsUpdateRequest.  # noqa: E501
        :rtype: boolean
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ReleaseDetailsUpdateRequest.

        Toggle this release to be enable distribute/download or not.  # noqa: E501

        :param enabled: The enabled of this ReleaseDetailsUpdateRequest.  # noqa: E501
        :type: boolean
        """

        self._enabled = enabled

    @property
    def release_notes(self):
        """Gets the release_notes of this ReleaseDetailsUpdateRequest.  # noqa: E501

        Release notes for this release.  # noqa: E501

        :return: The release_notes of this ReleaseDetailsUpdateRequest.  # noqa: E501
        :rtype: string
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this ReleaseDetailsUpdateRequest.

        Release notes for this release.  # noqa: E501

        :param release_notes: The release_notes of this ReleaseDetailsUpdateRequest.  # noqa: E501
        :type: string
        """

        self._release_notes = release_notes

    @property
    def build(self):
        """Gets the build of this ReleaseDetailsUpdateRequest.  # noqa: E501

        Contains metadata about the build that produced the release being uploaded  # noqa: E501

        :return: The build of this ReleaseDetailsUpdateRequest.  # noqa: E501
        :rtype: object
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ReleaseDetailsUpdateRequest.

        Contains metadata about the build that produced the release being uploaded  # noqa: E501

        :param build: The build of this ReleaseDetailsUpdateRequest.  # noqa: E501
        :type: object
        """

        self._build = build

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReleaseDetailsUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other