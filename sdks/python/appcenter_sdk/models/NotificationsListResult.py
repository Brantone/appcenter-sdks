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


class NotificationsListResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    Queued = "Queued"
    Sending = "Sending"
    Completed = "Completed"
    Failed = "Failed"
    NoTargetFound = "NoTargetFound"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'values': 'array',
        'total': 'integer',
        'next_link': 'string'
    }

    attribute_map = {
        'values': 'values',
        'total': 'total',
        'next_link': 'next_link'
    }

    def __init__(self, values=None, total=None, next_link=None):  # noqa: E501
        """NotificationsListResult - a model defined in Swagger"""  # noqa: E501
        self._values = None
        self._total = None
        self._next_link = None
        self.discriminator = None
        self.values = values
        if total is not None:
            self.total = total
        if next_link is not None:
            self.next_link = next_link

    @property
    def values(self):
        """Gets the values of this NotificationsListResult.  # noqa: E501


        :return: The values of this NotificationsListResult.  # noqa: E501
        :rtype: array
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this NotificationsListResult.


        :param values: The values of this NotificationsListResult.  # noqa: E501
        :type: array
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    @property
    def total(self):
        """Gets the total of this NotificationsListResult.  # noqa: E501

        the total count of notifications  # noqa: E501

        :return: The total of this NotificationsListResult.  # noqa: E501
        :rtype: integer
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NotificationsListResult.

        the total count of notifications  # noqa: E501

        :param total: The total of this NotificationsListResult.  # noqa: E501
        :type: integer
        """

        self._total = total

    @property
    def next_link(self):
        """Gets the next_link of this NotificationsListResult.  # noqa: E501


        :return: The next_link of this NotificationsListResult.  # noqa: E501
        :rtype: string
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this NotificationsListResult.


        :param next_link: The next_link of this NotificationsListResult.  # noqa: E501
        :type: string
        """

        self._next_link = next_link

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
        if not isinstance(other, NotificationsListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
