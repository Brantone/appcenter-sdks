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


class ErrorGroupModel(object):
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
        'model_name': 'string',
        'model_code': 'string',
        'error_count': 'integer'
    }

    attribute_map = {
        'model_name': 'model_name',
        'model_code': 'model_code',
        'error_count': 'error_count'
    }

    def __init__(self, model_name=None, model_code=None, error_count=None):  # noqa: E501
        """ErrorGroupModel - a model defined in Swagger"""  # noqa: E501
        self._model_name = None
        self._model_code = None
        self._error_count = None
        self.discriminator = None
        if model_name is not None:
            self.model_name = model_name
        if model_code is not None:
            self.model_code = model_code
        if error_count is not None:
            self.error_count = error_count

    @property
    def model_name(self):
        """Gets the model_name of this ErrorGroupModel.  # noqa: E501

        model name  # noqa: E501

        :return: The model_name of this ErrorGroupModel.  # noqa: E501
        :rtype: string
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this ErrorGroupModel.

        model name  # noqa: E501

        :param model_name: The model_name of this ErrorGroupModel.  # noqa: E501
        :type: string
        """

        self._model_name = model_name

    @property
    def model_code(self):
        """Gets the model_code of this ErrorGroupModel.  # noqa: E501

        model code  # noqa: E501

        :return: The model_code of this ErrorGroupModel.  # noqa: E501
        :rtype: string
        """
        return self._model_code

    @model_code.setter
    def model_code(self, model_code):
        """Sets the model_code of this ErrorGroupModel.

        model code  # noqa: E501

        :param model_code: The model_code of this ErrorGroupModel.  # noqa: E501
        :type: string
        """

        self._model_code = model_code

    @property
    def error_count(self):
        """Gets the error_count of this ErrorGroupModel.  # noqa: E501

        count of errors in a model  # noqa: E501

        :return: The error_count of this ErrorGroupModel.  # noqa: E501
        :rtype: integer
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this ErrorGroupModel.

        count of errors in a model  # noqa: E501

        :param error_count: The error_count of this ErrorGroupModel.  # noqa: E501
        :type: integer
        """

        self._error_count = error_count

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
        if not isinstance(other, ErrorGroupModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
