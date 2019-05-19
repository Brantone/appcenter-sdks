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


class DeviceSetConfiguration(object):
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
        'id': 'string',
        'image': '',
        'model': '',
        'os': 'string',
        'os_name': 'string'
    }

    attribute_map = {
        'id': 'id',
        'image': 'image',
        'model': 'model',
        'os': 'os',
        'os_name': 'os_name'
    }

    def __init__(self, id=None, image=None, model=None, os=None, os_name=None):  # noqa: E501
        """DeviceSetConfiguration - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._image = None
        self._model = None
        self._os = None
        self._os_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if model is not None:
            self.model = model
        if os is not None:
            self.os = os
        if os_name is not None:
            self.os_name = os_name

    @property
    def id(self):
        """Gets the id of this DeviceSetConfiguration.  # noqa: E501

        The unique id of the device configuration  # noqa: E501

        :return: The id of this DeviceSetConfiguration.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceSetConfiguration.

        The unique id of the device configuration  # noqa: E501

        :param id: The id of this DeviceSetConfiguration.  # noqa: E501
        :type: string
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this DeviceSetConfiguration.  # noqa: E501


        :return: The image of this DeviceSetConfiguration.  # noqa: E501
        :rtype: 
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this DeviceSetConfiguration.


        :param image: The image of this DeviceSetConfiguration.  # noqa: E501
        :type: 
        """

        self._image = image

    @property
    def model(self):
        """Gets the model of this DeviceSetConfiguration.  # noqa: E501


        :return: The model of this DeviceSetConfiguration.  # noqa: E501
        :rtype: 
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DeviceSetConfiguration.


        :param model: The model of this DeviceSetConfiguration.  # noqa: E501
        :type: 
        """

        self._model = model

    @property
    def os(self):
        """Gets the os of this DeviceSetConfiguration.  # noqa: E501


        :return: The os of this DeviceSetConfiguration.  # noqa: E501
        :rtype: string
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this DeviceSetConfiguration.


        :param os: The os of this DeviceSetConfiguration.  # noqa: E501
        :type: string
        """

        self._os = os

    @property
    def os_name(self):
        """Gets the os_name of this DeviceSetConfiguration.  # noqa: E501


        :return: The os_name of this DeviceSetConfiguration.  # noqa: E501
        :rtype: string
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this DeviceSetConfiguration.


        :param os_name: The os_name of this DeviceSetConfiguration.  # noqa: E501
        :type: string
        """

        self._os_name = os_name

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
        if not isinstance(other, DeviceSetConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
