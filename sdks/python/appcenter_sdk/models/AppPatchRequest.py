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


class AppPatchRequest(object):
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
        'description': 'string',
        'display_name': 'string',
        'release_type': 'string',
        'name': 'string',
        'icon_url': 'string'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'release_type': 'release_type',
        'name': 'name',
        'icon_url': 'icon_url'
    }

    def __init__(self, description=None, display_name=None, release_type=None, name=None, icon_url=None):  # noqa: E501
        """AppPatchRequest - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._display_name = None
        self._release_type = None
        self._name = None
        self._icon_url = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if release_type is not None:
            self.release_type = release_type
        if name is not None:
            self.name = name
        if icon_url is not None:
            self.icon_url = icon_url

    @property
    def description(self):
        """Gets the description of this AppPatchRequest.  # noqa: E501

        A short text describing the app  # noqa: E501

        :return: The description of this AppPatchRequest.  # noqa: E501
        :rtype: string
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppPatchRequest.

        A short text describing the app  # noqa: E501

        :param description: The description of this AppPatchRequest.  # noqa: E501
        :type: string
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this AppPatchRequest.  # noqa: E501

        The display name of the app  # noqa: E501

        :return: The display_name of this AppPatchRequest.  # noqa: E501
        :rtype: string
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AppPatchRequest.

        The display name of the app  # noqa: E501

        :param display_name: The display_name of this AppPatchRequest.  # noqa: E501
        :type: string
        """

        self._display_name = display_name

    @property
    def release_type(self):
        """Gets the release_type of this AppPatchRequest.  # noqa: E501

        A one-word descriptive release type value that starts with a capital letter but is otherwise lowercase  # noqa: E501

        :return: The release_type of this AppPatchRequest.  # noqa: E501
        :rtype: string
        """
        return self._release_type

    @release_type.setter
    def release_type(self, release_type):
        """Sets the release_type of this AppPatchRequest.

        A one-word descriptive release type value that starts with a capital letter but is otherwise lowercase  # noqa: E501

        :param release_type: The release_type of this AppPatchRequest.  # noqa: E501
        :type: string
        """

        self._release_type = release_type

    @property
    def name(self):
        """Gets the name of this AppPatchRequest.  # noqa: E501

        The name of the app used in URLs  # noqa: E501

        :return: The name of this AppPatchRequest.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppPatchRequest.

        The name of the app used in URLs  # noqa: E501

        :param name: The name of this AppPatchRequest.  # noqa: E501
        :type: string
        """

        self._name = name

    @property
    def icon_url(self):
        """Gets the icon_url of this AppPatchRequest.  # noqa: E501

        The string representation of the URL pointing to the app's icon  # noqa: E501

        :return: The icon_url of this AppPatchRequest.  # noqa: E501
        :rtype: string
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this AppPatchRequest.

        The string representation of the URL pointing to the app's icon  # noqa: E501

        :param icon_url: The icon_url of this AppPatchRequest.  # noqa: E501
        :type: string
        """

        self._icon_url = icon_url

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
        if not isinstance(other, AppPatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other