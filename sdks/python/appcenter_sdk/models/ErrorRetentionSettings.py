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


class ErrorRetentionSettings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    28 = "28"
    90 = "90"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'retention_in_days': 'integer'
    }

    attribute_map = {
        'retention_in_days': 'retention_in_days'
    }

    def __init__(self, retention_in_days=None):  # noqa: E501
        """ErrorRetentionSettings - a model defined in Swagger"""  # noqa: E501
        self._retention_in_days = None
        self.discriminator = None
        self.retention_in_days = retention_in_days

    @property
    def retention_in_days(self):
        """Gets the retention_in_days of this ErrorRetentionSettings.  # noqa: E501


        :return: The retention_in_days of this ErrorRetentionSettings.  # noqa: E501
        :rtype: integer
        """
        return self._retention_in_days

    @retention_in_days.setter
    def retention_in_days(self, retention_in_days):
        """Sets the retention_in_days of this ErrorRetentionSettings.


        :param retention_in_days: The retention_in_days of this ErrorRetentionSettings.  # noqa: E501
        :type: integer
        """
        if retention_in_days is None:
            raise ValueError("Invalid value for `retention_in_days`, must not be `None`")  # noqa: E501
        allowed_values = [undefinedundefined]  # noqa: E501

        self._retention_in_days = retention_in_days

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
        if not isinstance(other, ErrorRetentionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
