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


class FilterReleasesContainer(object):
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
        'releases': 'array'
    }

    attribute_map = {
        'releases': 'releases'
    }

    def __init__(self, releases=None):  # noqa: E501
        """FilterReleasesContainer - a model defined in Swagger"""  # noqa: E501
        self._releases = None
        self.discriminator = None
        if releases is not None:
            self.releases = releases

    @property
    def releases(self):
        """Gets the releases of this FilterReleasesContainer.  # noqa: E501


        :return: The releases of this FilterReleasesContainer.  # noqa: E501
        :rtype: array
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this FilterReleasesContainer.


        :param releases: The releases of this FilterReleasesContainer.  # noqa: E501
        :type: array
        """

        self._releases = releases

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
        if not isinstance(other, FilterReleasesContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
