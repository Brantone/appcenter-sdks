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


class EventSetting(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    Disabled = "Disabled"
    Individual = "Individual"
    Daily = "Daily"
    DailyAndIndividual = "DailyAndIndividual"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'event_type': 'string',
        'value': 'string',
        'default_value': 'string'
    }

    attribute_map = {
        'event_type': 'event_type',
        'value': 'value',
        'default_value': 'default_value'
    }

    def __init__(self, event_type=None, value=None, default_value=None):  # noqa: E501
        """EventSetting - a model defined in Swagger"""  # noqa: E501
        self._event_type = None
        self._value = None
        self._default_value = None
        self.discriminator = None
        self.event_type = event_type
        self.value = value
        if default_value is not None:
            self.default_value = default_value

    @property
    def event_type(self):
        """Gets the event_type of this EventSetting.  # noqa: E501

        Event Name  # noqa: E501

        :return: The event_type of this EventSetting.  # noqa: E501
        :rtype: string
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EventSetting.

        Event Name  # noqa: E501

        :param event_type: The event_type of this EventSetting.  # noqa: E501
        :type: string
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        allowed_values = [undefined, undefined, undefined, undefined, ]  # noqa: E501

        self._event_type = event_type

    @property
    def value(self):
        """Gets the value of this EventSetting.  # noqa: E501

        Frequency of event  # noqa: E501

        :return: The value of this EventSetting.  # noqa: E501
        :rtype: string
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EventSetting.

        Frequency of event  # noqa: E501

        :param value: The value of this EventSetting.  # noqa: E501
        :type: string
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        allowed_values = [undefined, undefined, undefined, undefined, ]  # noqa: E501

        self._value = value

    @property
    def default_value(self):
        """Gets the default_value of this EventSetting.  # noqa: E501

        Default frequency of event  # noqa: E501

        :return: The default_value of this EventSetting.  # noqa: E501
        :rtype: string
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this EventSetting.

        Default frequency of event  # noqa: E501

        :param default_value: The default_value of this EventSetting.  # noqa: E501
        :type: string
        """
        allowed_values = [undefinedundefinedundefinedundefined]  # noqa: E501

        self._default_value = default_value

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
        if not isinstance(other, EventSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
