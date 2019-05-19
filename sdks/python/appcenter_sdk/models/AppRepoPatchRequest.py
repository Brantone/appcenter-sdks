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


class AppRepoPatchRequest(object):
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
        'repo_url': 'string',
        'user_id': 'string'
    }

    attribute_map = {
        'repo_url': 'repo_url',
        'user_id': 'user_id'
    }

    def __init__(self, repo_url=None, user_id=None):  # noqa: E501
        """AppRepoPatchRequest - a model defined in Swagger"""  # noqa: E501
        self._repo_url = None
        self._user_id = None
        self.discriminator = None
        if repo_url is not None:
            self.repo_url = repo_url
        if user_id is not None:
            self.user_id = user_id

    @property
    def repo_url(self):
        """Gets the repo_url of this AppRepoPatchRequest.  # noqa: E501

        The absolute URL of the repository  # noqa: E501

        :return: The repo_url of this AppRepoPatchRequest.  # noqa: E501
        :rtype: string
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this AppRepoPatchRequest.

        The absolute URL of the repository  # noqa: E501

        :param repo_url: The repo_url of this AppRepoPatchRequest.  # noqa: E501
        :type: string
        """

        self._repo_url = repo_url

    @property
    def user_id(self):
        """Gets the user_id of this AppRepoPatchRequest.  # noqa: E501

        The unique id (UUID) of the user  # noqa: E501

        :return: The user_id of this AppRepoPatchRequest.  # noqa: E501
        :rtype: string
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AppRepoPatchRequest.

        The unique id (UUID) of the user  # noqa: E501

        :param user_id: The user_id of this AppRepoPatchRequest.  # noqa: E501
        :type: string
        """

        self._user_id = user_id

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
        if not isinstance(other, AppRepoPatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
