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


class HasBuildUploadedResponse(object):
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
        'has_build_uploaded': 'boolean'
    }

    attribute_map = {
        'has_build_uploaded': 'has_build_uploaded'
    }

    def __init__(self, has_build_uploaded=None):  # noqa: E501
        """HasBuildUploadedResponse - a model defined in Swagger"""  # noqa: E501
        self._has_build_uploaded = None
        self.discriminator = None
        if has_build_uploaded is not None:
            self.has_build_uploaded = has_build_uploaded

    @property
    def has_build_uploaded(self):
        """Gets the has_build_uploaded of this HasBuildUploadedResponse.  # noqa: E501

        true if a build has been uploaded, false otherwise  # noqa: E501

        :return: The has_build_uploaded of this HasBuildUploadedResponse.  # noqa: E501
        :rtype: boolean
        """
        return self._has_build_uploaded

    @has_build_uploaded.setter
    def has_build_uploaded(self, has_build_uploaded):
        """Sets the has_build_uploaded of this HasBuildUploadedResponse.

        true if a build has been uploaded, false otherwise  # noqa: E501

        :param has_build_uploaded: The has_build_uploaded of this HasBuildUploadedResponse.  # noqa: E501
        :type: boolean
        """

        self._has_build_uploaded = has_build_uploaded

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
        if not isinstance(other, HasBuildUploadedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
