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


class ApiTokenDeleteResponse(object):
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
        'id': 'string',
        'token_hash': 'string'
    }

    attribute_map = {
        'id': 'id',
        'token_hash': 'token_hash'
    }

    def __init__(self, id=None, token_hash=None):  # noqa: E501
        """ApiTokenDeleteResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._token_hash = None
        self.discriminator = None
        self.id = id
        self.token_hash = token_hash

    @property
    def id(self):
        """Gets the id of this ApiTokenDeleteResponse.  # noqa: E501

        The unique id (UUID) of the api token  # noqa: E501

        :return: The id of this ApiTokenDeleteResponse.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiTokenDeleteResponse.

        The unique id (UUID) of the api token  # noqa: E501

        :param id: The id of this ApiTokenDeleteResponse.  # noqa: E501
        :type: string
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def token_hash(self):
        """Gets the token_hash of this ApiTokenDeleteResponse.  # noqa: E501

        The hashed value of api token  # noqa: E501

        :return: The token_hash of this ApiTokenDeleteResponse.  # noqa: E501
        :rtype: string
        """
        return self._token_hash

    @token_hash.setter
    def token_hash(self, token_hash):
        """Sets the token_hash of this ApiTokenDeleteResponse.

        The hashed value of api token  # noqa: E501

        :param token_hash: The token_hash of this ApiTokenDeleteResponse.  # noqa: E501
        :type: string
        """
        if token_hash is None:
            raise ValueError("Invalid value for `token_hash`, must not be `None`")  # noqa: E501

        self._token_hash = token_hash

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
        if not isinstance(other, ApiTokenDeleteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
