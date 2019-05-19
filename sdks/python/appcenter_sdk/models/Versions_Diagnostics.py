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


class Versions_Diagnostics(object):
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
        'versions': 'array',
        'total': 'integer'
    }

    attribute_map = {
        'versions': 'versions',
        'total': 'total'
    }

    def __init__(self, versions=None, total=None):  # noqa: E501
        """Versions_Diagnostics - a model defined in Swagger"""  # noqa: E501
        self._versions = None
        self._total = None
        self.discriminator = None
        if versions is not None:
            self.versions = versions
        if total is not None:
            self.total = total

    @property
    def versions(self):
        """Gets the versions of this Versions_Diagnostics.  # noqa: E501

        list of version count  # noqa: E501

        :return: The versions of this Versions_Diagnostics.  # noqa: E501
        :rtype: array
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this Versions_Diagnostics.

        list of version count  # noqa: E501

        :param versions: The versions of this Versions_Diagnostics.  # noqa: E501
        :type: array
        """

        self._versions = versions

    @property
    def total(self):
        """Gets the total of this Versions_Diagnostics.  # noqa: E501

        the total count of versions  # noqa: E501

        :return: The total of this Versions_Diagnostics.  # noqa: E501
        :rtype: integer
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Versions_Diagnostics.

        the total count of versions  # noqa: E501

        :param total: The total of this Versions_Diagnostics.  # noqa: E501
        :type: integer
        """

        self._total = total

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
        if not isinstance(other, Versions_Diagnostics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
