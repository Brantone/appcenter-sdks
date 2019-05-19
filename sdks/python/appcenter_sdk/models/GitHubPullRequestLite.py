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


class GitHubPullRequestLite(object):
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
        'head': '',
        'base': ''
    }

    attribute_map = {
        'head': 'head',
        'base': 'base'
    }

    def __init__(self, head=None, base=None):  # noqa: E501
        """GitHubPullRequestLite - a model defined in Swagger"""  # noqa: E501
        self._head = None
        self._base = None
        self.discriminator = None
        if head is not None:
            self.head = head
        if base is not None:
            self.base = base

    @property
    def head(self):
        """Gets the head of this GitHubPullRequestLite.  # noqa: E501

        The lite version of GitHub branch  # noqa: E501

        :return: The head of this GitHubPullRequestLite.  # noqa: E501
        :rtype: 
        """
        return self._head

    @head.setter
    def head(self, head):
        """Sets the head of this GitHubPullRequestLite.

        The lite version of GitHub branch  # noqa: E501

        :param head: The head of this GitHubPullRequestLite.  # noqa: E501
        :type: 
        """

        self._head = head

    @property
    def base(self):
        """Gets the base of this GitHubPullRequestLite.  # noqa: E501

        The lite version of GitHub branch  # noqa: E501

        :return: The base of this GitHubPullRequestLite.  # noqa: E501
        :rtype: 
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this GitHubPullRequestLite.

        The lite version of GitHub branch  # noqa: E501

        :param base: The base of this GitHubPullRequestLite.  # noqa: E501
        :type: 
        """

        self._base = base

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
        if not isinstance(other, GitHubPullRequestLite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
