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


class NotificationConfigWindows(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    apns_token_config = "apns_token_config"
    gcm_config = "gcm_config"
    wns_config = "wns_config"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'package_sid': 'string',
        'secret_key': 'string'
    }

    attribute_map = {
        'package_sid': 'package_sid',
        'secret_key': 'secret_key'
    }

    def __init__(self, package_sid=None, secret_key=None):  # noqa: E501
        """NotificationConfigWindows - a model defined in Swagger"""  # noqa: E501
        self._package_sid = None
        self._secret_key = None
        self.discriminator = None
        self.package_sid = package_sid
        self.secret_key = secret_key

    @property
    def package_sid(self):
        """Gets the package_sid of this NotificationConfigWindows.  # noqa: E501

        Package security identifier (SID).  # noqa: E501

        :return: The package_sid of this NotificationConfigWindows.  # noqa: E501
        :rtype: string
        """
        return self._package_sid

    @package_sid.setter
    def package_sid(self, package_sid):
        """Sets the package_sid of this NotificationConfigWindows.

        Package security identifier (SID).  # noqa: E501

        :param package_sid: The package_sid of this NotificationConfigWindows.  # noqa: E501
        :type: string
        """
        if package_sid is None:
            raise ValueError("Invalid value for `package_sid`, must not be `None`")  # noqa: E501

        self._package_sid = package_sid

    @property
    def secret_key(self):
        """Gets the secret_key of this NotificationConfigWindows.  # noqa: E501

        Secret key.  # noqa: E501

        :return: The secret_key of this NotificationConfigWindows.  # noqa: E501
        :rtype: string
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this NotificationConfigWindows.

        Secret key.  # noqa: E501

        :param secret_key: The secret_key of this NotificationConfigWindows.  # noqa: E501
        :type: string
        """
        if secret_key is None:
            raise ValueError("Invalid value for `secret_key`, must not be `None`")  # noqa: E501

        self._secret_key = secret_key

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
        if not isinstance(other, NotificationConfigWindows):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
