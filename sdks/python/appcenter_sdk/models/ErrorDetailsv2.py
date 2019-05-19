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


class ErrorDetailsv2(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    BadRequest = "BadRequest"
    Conflict = "Conflict"
    NotAcceptable = "NotAcceptable"
    NotFound = "NotFound"
    InternalServerError = "InternalServerError"
    Unauthorized = "Unauthorized"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'string',
        'message': 'string'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message'
    }

    def __init__(self, code=None, message=None):  # noqa: E501
        """ErrorDetailsv2 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self.discriminator = None
        self.code = code
        self.message = message

    @property
    def code(self):
        """Gets the code of this ErrorDetailsv2.  # noqa: E501


        :return: The code of this ErrorDetailsv2.  # noqa: E501
        :rtype: string
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorDetailsv2.


        :param code: The code of this ErrorDetailsv2.  # noqa: E501
        :type: string
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        allowed_values = [undefined, undefined, undefined, undefined, undefined, undefined, ]  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this ErrorDetailsv2.  # noqa: E501


        :return: The message of this ErrorDetailsv2.  # noqa: E501
        :rtype: string
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorDetailsv2.


        :param message: The message of this ErrorDetailsv2.  # noqa: E501
        :type: string
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, ErrorDetailsv2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
