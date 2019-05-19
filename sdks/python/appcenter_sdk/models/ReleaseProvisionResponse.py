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


class ReleaseProvisionResponse(object):
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
        'status_url': 'string'
    }

    attribute_map = {
        'status_url': 'status_url'
    }

    def __init__(self, status_url=None):  # noqa: E501
        """ReleaseProvisionResponse - a model defined in Swagger"""  # noqa: E501
        self._status_url = None
        self.discriminator = None
        if status_url is not None:
            self.status_url = status_url

    @property
    def status_url(self):
        """Gets the status_url of this ReleaseProvisionResponse.  # noqa: E501

        The url to check provisioning status.  # noqa: E501

        :return: The status_url of this ReleaseProvisionResponse.  # noqa: E501
        :rtype: string
        """
        return self._status_url

    @status_url.setter
    def status_url(self, status_url):
        """Sets the status_url of this ReleaseProvisionResponse.

        The url to check provisioning status.  # noqa: E501

        :param status_url: The status_url of this ReleaseProvisionResponse.  # noqa: E501
        :type: string
        """

        self._status_url = status_url

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
        if not isinstance(other, ReleaseProvisionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other