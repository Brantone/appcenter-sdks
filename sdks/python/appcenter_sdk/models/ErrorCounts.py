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


class ErrorCounts(object):
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
        'count': 'integer',
        'errors': 'array'
    }

    attribute_map = {
        'count': 'count',
        'errors': 'errors'
    }

    def __init__(self, count=None, errors=None):  # noqa: E501
        """ErrorCounts - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._errors = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if errors is not None:
            self.errors = errors

    @property
    def count(self):
        """Gets the count of this ErrorCounts.  # noqa: E501

        total error count  # noqa: E501

        :return: The count of this ErrorCounts.  # noqa: E501
        :rtype: integer
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ErrorCounts.

        total error count  # noqa: E501

        :param count: The count of this ErrorCounts.  # noqa: E501
        :type: integer
        """

        self._count = count

    @property
    def errors(self):
        """Gets the errors of this ErrorCounts.  # noqa: E501

        the total error count for day  # noqa: E501

        :return: The errors of this ErrorCounts.  # noqa: E501
        :rtype: array
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ErrorCounts.

        the total error count for day  # noqa: E501

        :param errors: The errors of this ErrorCounts.  # noqa: E501
        :type: array
        """

        self._errors = errors

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
        if not isinstance(other, ErrorCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
