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


class DeviceResolution(object):
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
        'height': 'string',
        'width': 'string',
        'ppi': 'string'
    }

    attribute_map = {
        'height': 'height',
        'width': 'width',
        'ppi': 'ppi'
    }

    def __init__(self, height=None, width=None, ppi=None):  # noqa: E501
        """DeviceResolution - a model defined in Swagger"""  # noqa: E501
        self._height = None
        self._width = None
        self._ppi = None
        self.discriminator = None
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if ppi is not None:
            self.ppi = ppi

    @property
    def height(self):
        """Gets the height of this DeviceResolution.  # noqa: E501


        :return: The height of this DeviceResolution.  # noqa: E501
        :rtype: string
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DeviceResolution.


        :param height: The height of this DeviceResolution.  # noqa: E501
        :type: string
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this DeviceResolution.  # noqa: E501


        :return: The width of this DeviceResolution.  # noqa: E501
        :rtype: string
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DeviceResolution.


        :param width: The width of this DeviceResolution.  # noqa: E501
        :type: string
        """

        self._width = width

    @property
    def ppi(self):
        """Gets the ppi of this DeviceResolution.  # noqa: E501


        :return: The ppi of this DeviceResolution.  # noqa: E501
        :rtype: string
        """
        return self._ppi

    @ppi.setter
    def ppi(self, ppi):
        """Sets the ppi of this DeviceResolution.


        :param ppi: The ppi of this DeviceResolution.  # noqa: E501
        :type: string
        """

        self._ppi = ppi

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
        if not isinstance(other, DeviceResolution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
