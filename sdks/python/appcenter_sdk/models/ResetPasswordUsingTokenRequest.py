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


class ResetPasswordUsingTokenRequest(object):
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
        'new_password': 'string',
        'token': 'string'
    }

    attribute_map = {
        'new_password': 'new_password',
        'token': 'token'
    }

    def __init__(self, new_password=None, token=None):  # noqa: E501
        """ResetPasswordUsingTokenRequest - a model defined in Swagger"""  # noqa: E501
        self._new_password = None
        self._token = None
        self.discriminator = None
        self.new_password = new_password
        self.token = token

    @property
    def new_password(self):
        """Gets the new_password of this ResetPasswordUsingTokenRequest.  # noqa: E501

        The new password. Needs to be at least 8 characters long and contain at least one lower- and one uppercase letter.  # noqa: E501

        :return: The new_password of this ResetPasswordUsingTokenRequest.  # noqa: E501
        :rtype: string
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ResetPasswordUsingTokenRequest.

        The new password. Needs to be at least 8 characters long and contain at least one lower- and one uppercase letter.  # noqa: E501

        :param new_password: The new_password of this ResetPasswordUsingTokenRequest.  # noqa: E501
        :type: string
        """
        if new_password is None:
            raise ValueError("Invalid value for `new_password`, must not be `None`")  # noqa: E501

        self._new_password = new_password

    @property
    def token(self):
        """Gets the token of this ResetPasswordUsingTokenRequest.  # noqa: E501

        The reset password token that was sent to the user  # noqa: E501

        :return: The token of this ResetPasswordUsingTokenRequest.  # noqa: E501
        :rtype: string
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ResetPasswordUsingTokenRequest.

        The reset password token that was sent to the user  # noqa: E501

        :param token: The token of this ResetPasswordUsingTokenRequest.  # noqa: E501
        :type: string
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

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
        if not isinstance(other, ResetPasswordUsingTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other