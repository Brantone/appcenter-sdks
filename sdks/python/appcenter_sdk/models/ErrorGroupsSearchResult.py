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


class ErrorGroupsSearchResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    open = "open"
    closed = "closed"
    ignored = "ignored"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'has_more_results': 'boolean',
        'error_groups': 'array'
    }

    attribute_map = {
        'has_more_results': 'has_more_results',
        'error_groups': 'error_groups'
    }

    def __init__(self, has_more_results=None, error_groups=None):  # noqa: E501
        """ErrorGroupsSearchResult - a model defined in Swagger"""  # noqa: E501
        self._has_more_results = None
        self._error_groups = None
        self.discriminator = None
        if has_more_results is not None:
            self.has_more_results = has_more_results
        if error_groups is not None:
            self.error_groups = error_groups

    @property
    def has_more_results(self):
        """Gets the has_more_results of this ErrorGroupsSearchResult.  # noqa: E501


        :return: The has_more_results of this ErrorGroupsSearchResult.  # noqa: E501
        :rtype: boolean
        """
        return self._has_more_results

    @has_more_results.setter
    def has_more_results(self, has_more_results):
        """Sets the has_more_results of this ErrorGroupsSearchResult.


        :param has_more_results: The has_more_results of this ErrorGroupsSearchResult.  # noqa: E501
        :type: boolean
        """

        self._has_more_results = has_more_results

    @property
    def error_groups(self):
        """Gets the error_groups of this ErrorGroupsSearchResult.  # noqa: E501


        :return: The error_groups of this ErrorGroupsSearchResult.  # noqa: E501
        :rtype: array
        """
        return self._error_groups

    @error_groups.setter
    def error_groups(self, error_groups):
        """Sets the error_groups of this ErrorGroupsSearchResult.


        :param error_groups: The error_groups of this ErrorGroupsSearchResult.  # noqa: E501
        :type: array
        """

        self._error_groups = error_groups

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
        if not isinstance(other, ErrorGroupsSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
