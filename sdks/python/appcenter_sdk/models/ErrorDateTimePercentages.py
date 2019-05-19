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


class ErrorDateTimePercentages(object):
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
        'datetime': 'string',
        'percentage': 'number'
    }

    attribute_map = {
        'datetime': 'datetime',
        'percentage': 'percentage'
    }

    def __init__(self, datetime=None, percentage=None):  # noqa: E501
        """ErrorDateTimePercentages - a model defined in Swagger"""  # noqa: E501
        self._datetime = None
        self._percentage = None
        self.discriminator = None
        if datetime is not None:
            self.datetime = datetime
        if percentage is not None:
            self.percentage = percentage

    @property
    def datetime(self):
        """Gets the datetime of this ErrorDateTimePercentages.  # noqa: E501

        the ISO 8601 datetime  # noqa: E501

        :return: The datetime of this ErrorDateTimePercentages.  # noqa: E501
        :rtype: string
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        """Sets the datetime of this ErrorDateTimePercentages.

        the ISO 8601 datetime  # noqa: E501

        :param datetime: The datetime of this ErrorDateTimePercentages.  # noqa: E501
        :type: string
        """

        self._datetime = datetime

    @property
    def percentage(self):
        """Gets the percentage of this ErrorDateTimePercentages.  # noqa: E501

        percentage of the object  # noqa: E501

        :return: The percentage of this ErrorDateTimePercentages.  # noqa: E501
        :rtype: number
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this ErrorDateTimePercentages.

        percentage of the object  # noqa: E501

        :param percentage: The percentage of this ErrorDateTimePercentages.  # noqa: E501
        :type: number
        """

        self._percentage = percentage

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
        if not isinstance(other, ErrorDateTimePercentages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
