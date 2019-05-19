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


class CrashGroupModels(object):
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
        'crash_count': 'integer',
        'models': 'array'
    }

    attribute_map = {
        'crash_count': 'crash_count',
        'models': 'models'
    }

    def __init__(self, crash_count=None, models=None):  # noqa: E501
        """CrashGroupModels - a model defined in Swagger"""  # noqa: E501
        self._crash_count = None
        self._models = None
        self.discriminator = None
        if crash_count is not None:
            self.crash_count = crash_count
        if models is not None:
            self.models = models

    @property
    def crash_count(self):
        """Gets the crash_count of this CrashGroupModels.  # noqa: E501


        :return: The crash_count of this CrashGroupModels.  # noqa: E501
        :rtype: integer
        """
        return self._crash_count

    @crash_count.setter
    def crash_count(self, crash_count):
        """Sets the crash_count of this CrashGroupModels.


        :param crash_count: The crash_count of this CrashGroupModels.  # noqa: E501
        :type: integer
        """

        self._crash_count = crash_count

    @property
    def models(self):
        """Gets the models of this CrashGroupModels.  # noqa: E501


        :return: The models of this CrashGroupModels.  # noqa: E501
        :rtype: array
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this CrashGroupModels.


        :param models: The models of this CrashGroupModels.  # noqa: E501
        :type: array
        """

        self._models = models

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
        if not isinstance(other, CrashGroupModels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
