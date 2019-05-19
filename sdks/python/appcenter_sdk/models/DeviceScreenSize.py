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


class DeviceScreenSize(object):
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
        'cm': 'string',
        'in': 'string'
    }

    attribute_map = {
        'cm': 'cm',
        'in': 'in'
    }

    def __init__(self, cm=None, in=None):  # noqa: E501
        """DeviceScreenSize - a model defined in Swagger"""  # noqa: E501
        self._cm = None
        self._in = None
        self.discriminator = None
        if cm is not None:
            self.cm = cm
        if in is not None:
            self.in = in

    @property
    def cm(self):
        """Gets the cm of this DeviceScreenSize.  # noqa: E501


        :return: The cm of this DeviceScreenSize.  # noqa: E501
        :rtype: string
        """
        return self._cm

    @cm.setter
    def cm(self, cm):
        """Sets the cm of this DeviceScreenSize.


        :param cm: The cm of this DeviceScreenSize.  # noqa: E501
        :type: string
        """

        self._cm = cm

    @property
    def in(self):
        """Gets the in of this DeviceScreenSize.  # noqa: E501


        :return: The in of this DeviceScreenSize.  # noqa: E501
        :rtype: string
        """
        return self._in

    @in.setter
    def in(self, in):
        """Sets the in of this DeviceScreenSize.


        :param in: The in of this DeviceScreenSize.  # noqa: E501
        :type: string
        """

        self._in = in

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
        if not isinstance(other, DeviceScreenSize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
