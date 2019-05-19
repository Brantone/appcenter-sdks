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


class StartSessionLog_Diagnostics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    event = "event"
    page = "page"
    start_session = "start_session"
    error = "error"
    push_installation = "push_installation"
    start_service = "start_service"
    custom_properties = "custom_properties"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'session_id': 'string'
    }

    attribute_map = {
        'session_id': 'session_id'
    }

    def __init__(self, session_id=None):  # noqa: E501
        """StartSessionLog_Diagnostics - a model defined in Swagger"""  # noqa: E501
        self._session_id = None
        self.discriminator = None
        self.session_id = session_id

    @property
    def session_id(self):
        """Gets the session_id of this StartSessionLog_Diagnostics.  # noqa: E501

        Session ID.
  # noqa: E501

        :return: The session_id of this StartSessionLog_Diagnostics.  # noqa: E501
        :rtype: string
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this StartSessionLog_Diagnostics.

        Session ID.
  # noqa: E501

        :param session_id: The session_id of this StartSessionLog_Diagnostics.  # noqa: E501
        :type: string
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

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
        if not isinstance(other, StartSessionLog_Diagnostics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
