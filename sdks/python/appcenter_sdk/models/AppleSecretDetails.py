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


class AppleSecretDetails(object):
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
        'username': 'string',
        'auth_code': 'string',
        'password': 'string'
    }

    attribute_map = {
        'username': 'username',
        'auth_code': 'auth_code',
        'password': 'password'
    }

    def __init__(self, username=None, auth_code=None, password=None):  # noqa: E501
        """AppleSecretDetails - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._auth_code = None
        self._password = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if auth_code is not None:
            self.auth_code = auth_code
        if password is not None:
            self.password = password

    @property
    def username(self):
        """Gets the username of this AppleSecretDetails.  # noqa: E501

        username to connect to apple store.  # noqa: E501

        :return: The username of this AppleSecretDetails.  # noqa: E501
        :rtype: string
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AppleSecretDetails.

        username to connect to apple store.  # noqa: E501

        :param username: The username of this AppleSecretDetails.  # noqa: E501
        :type: string
        """

        self._username = username

    @property
    def auth_code(self):
        """Gets the auth_code of this AppleSecretDetails.  # noqa: E501

        6 digit auth code  # noqa: E501

        :return: The auth_code of this AppleSecretDetails.  # noqa: E501
        :rtype: string
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """Sets the auth_code of this AppleSecretDetails.

        6 digit auth code  # noqa: E501

        :param auth_code: The auth_code of this AppleSecretDetails.  # noqa: E501
        :type: string
        """

        self._auth_code = auth_code

    @property
    def password(self):
        """Gets the password of this AppleSecretDetails.  # noqa: E501

        password to connect to apple store.  # noqa: E501

        :return: The password of this AppleSecretDetails.  # noqa: E501
        :rtype: string
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AppleSecretDetails.

        password to connect to apple store.  # noqa: E501

        :param password: The password of this AppleSecretDetails.  # noqa: E501
        :type: string
        """

        self._password = password

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
        if not isinstance(other, AppleSecretDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
