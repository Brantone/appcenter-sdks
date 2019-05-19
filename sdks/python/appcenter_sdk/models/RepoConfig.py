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


class RepoConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    unauthorized = "unauthorized"
    inactive = "inactive"
    active = "active"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'string',
        'state': 'string',
        'repo_url': 'string',
        'id': 'string',
        'user_email': 'string',
        'installation_id': 'string'
    }

    attribute_map = {
        'type': 'type',
        'state': 'state',
        'repo_url': 'repo_url',
        'id': 'id',
        'user_email': 'user_email',
        'installation_id': 'installation_id'
    }

    def __init__(self, type=None, state=None, repo_url=None, id=None, user_email=None, installation_id=None):  # noqa: E501
        """RepoConfig - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._state = None
        self._repo_url = None
        self._id = None
        self._user_email = None
        self._installation_id = None
        self.discriminator = None
        self.type = type
        self.state = state
        if repo_url is not None:
            self.repo_url = repo_url
        if id is not None:
            self.id = id
        if user_email is not None:
            self.user_email = user_email
        if installation_id is not None:
            self.installation_id = installation_id

    @property
    def type(self):
        """Gets the type of this RepoConfig.  # noqa: E501

        Type of repository  # noqa: E501

        :return: The type of this RepoConfig.  # noqa: E501
        :rtype: string
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RepoConfig.

        Type of repository  # noqa: E501

        :param type: The type of this RepoConfig.  # noqa: E501
        :type: string
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def state(self):
        """Gets the state of this RepoConfig.  # noqa: E501

        State of the configuration  # noqa: E501

        :return: The state of this RepoConfig.  # noqa: E501
        :rtype: string
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RepoConfig.

        State of the configuration  # noqa: E501

        :param state: The state of this RepoConfig.  # noqa: E501
        :type: string
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = [undefined, undefined, undefined, ]  # noqa: E501

        self._state = state

    @property
    def repo_url(self):
        """Gets the repo_url of this RepoConfig.  # noqa: E501

        URL of the repository  # noqa: E501

        :return: The repo_url of this RepoConfig.  # noqa: E501
        :rtype: string
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this RepoConfig.

        URL of the repository  # noqa: E501

        :param repo_url: The repo_url of this RepoConfig.  # noqa: E501
        :type: string
        """

        self._repo_url = repo_url

    @property
    def id(self):
        """Gets the id of this RepoConfig.  # noqa: E501

        Repository identifier  # noqa: E501

        :return: The id of this RepoConfig.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RepoConfig.

        Repository identifier  # noqa: E501

        :param id: The id of this RepoConfig.  # noqa: E501
        :type: string
        """

        self._id = id

    @property
    def user_email(self):
        """Gets the user_email of this RepoConfig.  # noqa: E501

        email of user, who linked repository  # noqa: E501

        :return: The user_email of this RepoConfig.  # noqa: E501
        :rtype: string
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this RepoConfig.

        email of user, who linked repository  # noqa: E501

        :param user_email: The user_email of this RepoConfig.  # noqa: E501
        :type: string
        """

        self._user_email = user_email

    @property
    def installation_id(self):
        """Gets the installation_id of this RepoConfig.  # noqa: E501

        The GitHub Installation id  # noqa: E501

        :return: The installation_id of this RepoConfig.  # noqa: E501
        :rtype: string
        """
        return self._installation_id

    @installation_id.setter
    def installation_id(self, installation_id):
        """Sets the installation_id of this RepoConfig.

        The GitHub Installation id  # noqa: E501

        :param installation_id: The installation_id of this RepoConfig.  # noqa: E501
        :type: string
        """

        self._installation_id = installation_id

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
        if not isinstance(other, RepoConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
