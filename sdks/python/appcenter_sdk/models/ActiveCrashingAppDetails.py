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


class ActiveCrashingAppDetails(object):
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
        'next_link': 'string',
        'apps_with_crashes': 'array'
    }

    attribute_map = {
        'next_link': 'next_link',
        'apps_with_crashes': 'apps_with_crashes'
    }

    def __init__(self, next_link=None, apps_with_crashes=None):  # noqa: E501
        """ActiveCrashingAppDetails - a model defined in Swagger"""  # noqa: E501
        self._next_link = None
        self._apps_with_crashes = None
        self.discriminator = None
        if next_link is not None:
            self.next_link = next_link
        if apps_with_crashes is not None:
            self.apps_with_crashes = apps_with_crashes

    @property
    def next_link(self):
        """Gets the next_link of this ActiveCrashingAppDetails.  # noqa: E501


        :return: The next_link of this ActiveCrashingAppDetails.  # noqa: E501
        :rtype: string
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this ActiveCrashingAppDetails.


        :param next_link: The next_link of this ActiveCrashingAppDetails.  # noqa: E501
        :type: string
        """

        self._next_link = next_link

    @property
    def apps_with_crashes(self):
        """Gets the apps_with_crashes of this ActiveCrashingAppDetails.  # noqa: E501

        details of the apps with crashes  # noqa: E501

        :return: The apps_with_crashes of this ActiveCrashingAppDetails.  # noqa: E501
        :rtype: array
        """
        return self._apps_with_crashes

    @apps_with_crashes.setter
    def apps_with_crashes(self, apps_with_crashes):
        """Sets the apps_with_crashes of this ActiveCrashingAppDetails.

        details of the apps with crashes  # noqa: E501

        :param apps_with_crashes: The apps_with_crashes of this ActiveCrashingAppDetails.  # noqa: E501
        :type: array
        """

        self._apps_with_crashes = apps_with_crashes

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
        if not isinstance(other, ActiveCrashingAppDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other