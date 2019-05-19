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


class Commit(object):
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
        'sha': 'string',
        'url': 'string'
    }

    attribute_map = {
        'sha': 'sha',
        'url': 'url'
    }

    def __init__(self, sha=None, url=None):  # noqa: E501
        """Commit - a model defined in Swagger"""  # noqa: E501
        self._sha = None
        self._url = None
        self.discriminator = None
        if sha is not None:
            self.sha = sha
        if url is not None:
            self.url = url

    @property
    def sha(self):
        """Gets the sha of this Commit.  # noqa: E501

        The commit SHA  # noqa: E501

        :return: The sha of this Commit.  # noqa: E501
        :rtype: string
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this Commit.

        The commit SHA  # noqa: E501

        :param sha: The sha of this Commit.  # noqa: E501
        :type: string
        """

        self._sha = sha

    @property
    def url(self):
        """Gets the url of this Commit.  # noqa: E501

        The URL to the commit  # noqa: E501

        :return: The url of this Commit.  # noqa: E501
        :rtype: string
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Commit.

        The URL to the commit  # noqa: E501

        :param url: The url of this Commit.  # noqa: E501
        :type: string
        """

        self._url = url

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
        if not isinstance(other, Commit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
