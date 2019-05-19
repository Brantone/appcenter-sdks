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


class JavaScriptSolution(object):
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
        'package_json_path': 'string',
        'react_native_version': 'string'
    }

    attribute_map = {
        'package_json_path': 'package_json_path',
        'react_native_version': 'react_native_version'
    }

    def __init__(self, package_json_path=None, react_native_version=None):  # noqa: E501
        """JavaScriptSolution - a model defined in Swagger"""  # noqa: E501
        self._package_json_path = None
        self._react_native_version = None
        self.discriminator = None
        if package_json_path is not None:
            self.package_json_path = package_json_path
        if react_native_version is not None:
            self.react_native_version = react_native_version

    @property
    def package_json_path(self):
        """Gets the package_json_path of this JavaScriptSolution.  # noqa: E501

        The path to the detected package.json  # noqa: E501

        :return: The package_json_path of this JavaScriptSolution.  # noqa: E501
        :rtype: string
        """
        return self._package_json_path

    @package_json_path.setter
    def package_json_path(self, package_json_path):
        """Sets the package_json_path of this JavaScriptSolution.

        The path to the detected package.json  # noqa: E501

        :param package_json_path: The package_json_path of this JavaScriptSolution.  # noqa: E501
        :type: string
        """

        self._package_json_path = package_json_path

    @property
    def react_native_version(self):
        """Gets the react_native_version of this JavaScriptSolution.  # noqa: E501

        Version of React Native from package.json files  # noqa: E501

        :return: The react_native_version of this JavaScriptSolution.  # noqa: E501
        :rtype: string
        """
        return self._react_native_version

    @react_native_version.setter
    def react_native_version(self, react_native_version):
        """Sets the react_native_version of this JavaScriptSolution.

        Version of React Native from package.json files  # noqa: E501

        :param react_native_version: The react_native_version of this JavaScriptSolution.  # noqa: E501
        :type: string
        """

        self._react_native_version = react_native_version

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
        if not isinstance(other, JavaScriptSolution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
