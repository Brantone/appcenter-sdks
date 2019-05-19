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


class ReleaseCount(object):
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
        'release_id': 'string',
        'distribution_group': 'string',
        'unique_count': 'integer',
        'total_count': 'integer'
    }

    attribute_map = {
        'release_id': 'release_id',
        'distribution_group': 'distribution_group',
        'unique_count': 'unique_count',
        'total_count': 'total_count'
    }

    def __init__(self, release_id=None, distribution_group=None, unique_count=None, total_count=None):  # noqa: E501
        """ReleaseCount - a model defined in Swagger"""  # noqa: E501
        self._release_id = None
        self._distribution_group = None
        self._unique_count = None
        self._total_count = None
        self.discriminator = None
        self.release_id = release_id
        if distribution_group is not None:
            self.distribution_group = distribution_group
        self.unique_count = unique_count
        self.total_count = total_count

    @property
    def release_id(self):
        """Gets the release_id of this ReleaseCount.  # noqa: E501


        :return: The release_id of this ReleaseCount.  # noqa: E501
        :rtype: string
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this ReleaseCount.


        :param release_id: The release_id of this ReleaseCount.  # noqa: E501
        :type: string
        """
        if release_id is None:
            raise ValueError("Invalid value for `release_id`, must not be `None`")  # noqa: E501

        self._release_id = release_id

    @property
    def distribution_group(self):
        """Gets the distribution_group of this ReleaseCount.  # noqa: E501

        Distribution group queried.
  # noqa: E501

        :return: The distribution_group of this ReleaseCount.  # noqa: E501
        :rtype: string
        """
        return self._distribution_group

    @distribution_group.setter
    def distribution_group(self, distribution_group):
        """Sets the distribution_group of this ReleaseCount.

        Distribution group queried.
  # noqa: E501

        :param distribution_group: The distribution_group of this ReleaseCount.  # noqa: E501
        :type: string
        """

        self._distribution_group = distribution_group

    @property
    def unique_count(self):
        """Gets the unique_count of this ReleaseCount.  # noqa: E501

        Count of unique downloads against user id.
  # noqa: E501

        :return: The unique_count of this ReleaseCount.  # noqa: E501
        :rtype: integer
        """
        return self._unique_count

    @unique_count.setter
    def unique_count(self, unique_count):
        """Sets the unique_count of this ReleaseCount.

        Count of unique downloads against user id.
  # noqa: E501

        :param unique_count: The unique_count of this ReleaseCount.  # noqa: E501
        :type: integer
        """
        if unique_count is None:
            raise ValueError("Invalid value for `unique_count`, must not be `None`")  # noqa: E501

        self._unique_count = unique_count

    @property
    def total_count(self):
        """Gets the total_count of this ReleaseCount.  # noqa: E501

        Total count of downloads.
  # noqa: E501

        :return: The total_count of this ReleaseCount.  # noqa: E501
        :rtype: integer
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ReleaseCount.

        Total count of downloads.
  # noqa: E501

        :param total_count: The total_count of this ReleaseCount.  # noqa: E501
        :type: integer
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

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
        if not isinstance(other, ReleaseCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
