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


class AppRepoPostRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    github = "github"
    bitbucket = "bitbucket"
    vsts = "vsts"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'repo_url': 'string',
        'repo_provider': 'string',
        'user_id': 'string',
        'installation_id': 'string',
        'repo_id': 'string'
    }

    attribute_map = {
        'repo_url': 'repo_url',
        'repo_provider': 'repo_provider',
        'user_id': 'user_id',
        'installation_id': 'installation_id',
        'repo_id': 'repo_id'
    }

    def __init__(self, repo_url=None, repo_provider=None, user_id=None, installation_id=None, repo_id=None):  # noqa: E501
        """AppRepoPostRequest - a model defined in Swagger"""  # noqa: E501
        self._repo_url = None
        self._repo_provider = None
        self._user_id = None
        self._installation_id = None
        self._repo_id = None
        self.discriminator = None
        self.repo_url = repo_url
        if repo_provider is not None:
            self.repo_provider = repo_provider
        self.user_id = user_id
        if installation_id is not None:
            self.installation_id = installation_id
        if repo_id is not None:
            self.repo_id = repo_id

    @property
    def repo_url(self):
        """Gets the repo_url of this AppRepoPostRequest.  # noqa: E501

        The absolute URL of the repository  # noqa: E501

        :return: The repo_url of this AppRepoPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this AppRepoPostRequest.

        The absolute URL of the repository  # noqa: E501

        :param repo_url: The repo_url of this AppRepoPostRequest.  # noqa: E501
        :type: string
        """
        if repo_url is None:
            raise ValueError("Invalid value for `repo_url`, must not be `None`")  # noqa: E501

        self._repo_url = repo_url

    @property
    def repo_provider(self):
        """Gets the repo_provider of this AppRepoPostRequest.  # noqa: E501

        The provider of the repository  # noqa: E501

        :return: The repo_provider of this AppRepoPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._repo_provider

    @repo_provider.setter
    def repo_provider(self, repo_provider):
        """Sets the repo_provider of this AppRepoPostRequest.

        The provider of the repository  # noqa: E501

        :param repo_provider: The repo_provider of this AppRepoPostRequest.  # noqa: E501
        :type: string
        """
        allowed_values = [undefined, undefined, undefined, ]  # noqa: E501

        self._repo_provider = repo_provider

    @property
    def user_id(self):
        """Gets the user_id of this AppRepoPostRequest.  # noqa: E501

        The unique id (UUID) of the user who configured the repository  # noqa: E501

        :return: The user_id of this AppRepoPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AppRepoPostRequest.

        The unique id (UUID) of the user who configured the repository  # noqa: E501

        :param user_id: The user_id of this AppRepoPostRequest.  # noqa: E501
        :type: string
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def installation_id(self):
        """Gets the installation_id of this AppRepoPostRequest.  # noqa: E501

        Installation id from the provider  # noqa: E501

        :return: The installation_id of this AppRepoPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._installation_id

    @installation_id.setter
    def installation_id(self, installation_id):
        """Sets the installation_id of this AppRepoPostRequest.

        Installation id from the provider  # noqa: E501

        :param installation_id: The installation_id of this AppRepoPostRequest.  # noqa: E501
        :type: string
        """

        self._installation_id = installation_id

    @property
    def repo_id(self):
        """Gets the repo_id of this AppRepoPostRequest.  # noqa: E501

        Repository id from the provider  # noqa: E501

        :return: The repo_id of this AppRepoPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this AppRepoPostRequest.

        Repository id from the provider  # noqa: E501

        :param repo_id: The repo_id of this AppRepoPostRequest.  # noqa: E501
        :type: string
        """

        self._repo_id = repo_id

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
        if not isinstance(other, AppRepoPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
