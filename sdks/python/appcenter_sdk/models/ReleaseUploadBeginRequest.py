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


class ReleaseUploadBeginRequest(object):
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
        'release_id': 'number'
    }

    attribute_map = {
        'release_id': 'release_id'
    }

    def __init__(self, release_id=None):  # noqa: E501
        """ReleaseUploadBeginRequest - a model defined in Swagger"""  # noqa: E501
        self._release_id = None
        self.discriminator = None
        if release_id is not None:
            self.release_id = release_id

    @property
    def release_id(self):
        """Gets the release_id of this ReleaseUploadBeginRequest.  # noqa: E501

        The ID of the release.  # noqa: E501

        :return: The release_id of this ReleaseUploadBeginRequest.  # noqa: E501
        :rtype: number
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this ReleaseUploadBeginRequest.

        The ID of the release.  # noqa: E501

        :param release_id: The release_id of this ReleaseUploadBeginRequest.  # noqa: E501
        :type: number
        """

        self._release_id = release_id

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
        if not isinstance(other, ReleaseUploadBeginRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
