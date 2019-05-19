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


class ReleaseUpdateResponse(object):
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
        'mandatory_update': 'boolean',
        'release_notes': 'string',
        'provisioning_status_url': 'string',
        'destinations': 'array'
    }

    attribute_map = {
        'enabled': 'enabled',
        'mandatory_update': 'mandatory_update',
        'release_notes': 'release_notes',
        'provisioning_status_url': 'provisioning_status_url',
        'destinations': 'destinations'
    }

    def __init__(self, enabled=None, mandatory_update=None, release_notes=None, provisioning_status_url=None, destinations=None):  # noqa: E501
        """ReleaseUpdateResponse - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._mandatory_update = None
        self._release_notes = None
        self._provisioning_status_url = None
        self._destinations = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if mandatory_update is not None:
            self.mandatory_update = mandatory_update
        if release_notes is not None:
            self.release_notes = release_notes
        if provisioning_status_url is not None:
            self.provisioning_status_url = provisioning_status_url
        if destinations is not None:
            self.destinations = destinations

    @property
    def enabled(self):
        """Gets the enabled of this ReleaseUpdateResponse.  # noqa: E501


        :return: The enabled of this ReleaseUpdateResponse.  # noqa: E501
        :rtype: boolean
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ReleaseUpdateResponse.


        :param enabled: The enabled of this ReleaseUpdateResponse.  # noqa: E501
        :type: boolean
        """

        self._enabled = enabled

    @property
    def mandatory_update(self):
        """Gets the mandatory_update of this ReleaseUpdateResponse.  # noqa: E501


        :return: The mandatory_update of this ReleaseUpdateResponse.  # noqa: E501
        :rtype: boolean
        """
        return self._mandatory_update

    @mandatory_update.setter
    def mandatory_update(self, mandatory_update):
        """Sets the mandatory_update of this ReleaseUpdateResponse.


        :param mandatory_update: The mandatory_update of this ReleaseUpdateResponse.  # noqa: E501
        :type: boolean
        """

        self._mandatory_update = mandatory_update

    @property
    def release_notes(self):
        """Gets the release_notes of this ReleaseUpdateResponse.  # noqa: E501


        :return: The release_notes of this ReleaseUpdateResponse.  # noqa: E501
        :rtype: string
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this ReleaseUpdateResponse.


        :param release_notes: The release_notes of this ReleaseUpdateResponse.  # noqa: E501
        :type: string
        """

        self._release_notes = release_notes

    @property
    def provisioning_status_url(self):
        """Gets the provisioning_status_url of this ReleaseUpdateResponse.  # noqa: E501


        :return: The provisioning_status_url of this ReleaseUpdateResponse.  # noqa: E501
        :rtype: string
        """
        return self._provisioning_status_url

    @provisioning_status_url.setter
    def provisioning_status_url(self, provisioning_status_url):
        """Sets the provisioning_status_url of this ReleaseUpdateResponse.


        :param provisioning_status_url: The provisioning_status_url of this ReleaseUpdateResponse.  # noqa: E501
        :type: string
        """

        self._provisioning_status_url = provisioning_status_url

    @property
    def destinations(self):
        """Gets the destinations of this ReleaseUpdateResponse.  # noqa: E501


        :return: The destinations of this ReleaseUpdateResponse.  # noqa: E501
        :rtype: array
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this ReleaseUpdateResponse.


        :param destinations: The destinations of this ReleaseUpdateResponse.  # noqa: E501
        :type: array
        """

        self._destinations = destinations

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
        if not isinstance(other, ReleaseUpdateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
