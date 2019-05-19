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


class BuildConcurrencyResponse(object):
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
        'quantity': 'number',
        'committed_quantity': 'number'
    }

    attribute_map = {
        'quantity': 'quantity',
        'committed_quantity': 'committed_quantity'
    }

    def __init__(self, quantity=None, committed_quantity=None):  # noqa: E501
        """BuildConcurrencyResponse - a model defined in Swagger"""  # noqa: E501
        self._quantity = None
        self._committed_quantity = None
        self.discriminator = None
        if quantity is not None:
            self.quantity = quantity
        if committed_quantity is not None:
            self.committed_quantity = committed_quantity

    @property
    def quantity(self):
        """Gets the quantity of this BuildConcurrencyResponse.  # noqa: E501

        The number of pipelines set by the billing plan  # noqa: E501

        :return: The quantity of this BuildConcurrencyResponse.  # noqa: E501
        :rtype: number
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this BuildConcurrencyResponse.

        The number of pipelines set by the billing plan  # noqa: E501

        :param quantity: The quantity of this BuildConcurrencyResponse.  # noqa: E501
        :type: number
        """

        self._quantity = quantity

    @property
    def committed_quantity(self):
        """Gets the committed_quantity of this BuildConcurrencyResponse.  # noqa: E501

        The number of pipelines committed, which can be equal or greater than the number from the billing plan  # noqa: E501

        :return: The committed_quantity of this BuildConcurrencyResponse.  # noqa: E501
        :rtype: number
        """
        return self._committed_quantity

    @committed_quantity.setter
    def committed_quantity(self, committed_quantity):
        """Sets the committed_quantity of this BuildConcurrencyResponse.

        The number of pipelines committed, which can be equal or greater than the number from the billing plan  # noqa: E501

        :param committed_quantity: The committed_quantity of this BuildConcurrencyResponse.  # noqa: E501
        :type: number
        """

        self._committed_quantity = committed_quantity

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
        if not isinstance(other, BuildConcurrencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other