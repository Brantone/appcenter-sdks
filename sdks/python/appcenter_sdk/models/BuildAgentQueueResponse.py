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


class BuildAgentQueueResponse(object):
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
        'build_definition': 'string',
        'name': 'string'
    }

    attribute_map = {
        'build_definition': 'build_definition',
        'name': 'name'
    }

    def __init__(self, build_definition=None, name=None):  # noqa: E501
        """BuildAgentQueueResponse - a model defined in Swagger"""  # noqa: E501
        self._build_definition = None
        self._name = None
        self.discriminator = None
        if build_definition is not None:
            self.build_definition = build_definition
        if name is not None:
            self.name = name

    @property
    def build_definition(self):
        """Gets the build_definition of this BuildAgentQueueResponse.  # noqa: E501

        Name of the build definition  # noqa: E501

        :return: The build_definition of this BuildAgentQueueResponse.  # noqa: E501
        :rtype: string
        """
        return self._build_definition

    @build_definition.setter
    def build_definition(self, build_definition):
        """Sets the build_definition of this BuildAgentQueueResponse.

        Name of the build definition  # noqa: E501

        :param build_definition: The build_definition of this BuildAgentQueueResponse.  # noqa: E501
        :type: string
        """

        self._build_definition = build_definition

    @property
    def name(self):
        """Gets the name of this BuildAgentQueueResponse.  # noqa: E501

        Name of the queue  # noqa: E501

        :return: The name of this BuildAgentQueueResponse.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BuildAgentQueueResponse.

        Name of the queue  # noqa: E501

        :param name: The name of this BuildAgentQueueResponse.  # noqa: E501
        :type: string
        """

        self._name = name

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
        if not isinstance(other, BuildAgentQueueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other