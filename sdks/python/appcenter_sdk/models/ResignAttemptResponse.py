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


class ResignAttemptResponse(object):
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
        'status': 'string',
        'user_id': 'string',
        'app_id': 'string',
        'original_release_id': 'number',
        'resign_id': 'string',
        'context_id': 'string',
        'start_time': 'number',
        'destinations': 'array',
        'error_code': 'string',
        'error_message': 'string'
    }

    attribute_map = {
        'status': 'status',
        'user_id': 'user_id',
        'app_id': 'app_id',
        'original_release_id': 'original_release_id',
        'resign_id': 'resign_id',
        'context_id': 'context_id',
        'start_time': 'start_time',
        'destinations': 'destinations',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, status=None, user_id=None, app_id=None, original_release_id=None, resign_id=None, context_id=None, start_time=None, destinations=None, error_code=None, error_message=None):  # noqa: E501
        """ResignAttemptResponse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._user_id = None
        self._app_id = None
        self._original_release_id = None
        self._resign_id = None
        self._context_id = None
        self._start_time = None
        self._destinations = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None
        self.status = status
        if user_id is not None:
            self.user_id = user_id
        if app_id is not None:
            self.app_id = app_id
        if original_release_id is not None:
            self.original_release_id = original_release_id
        if resign_id is not None:
            self.resign_id = resign_id
        if context_id is not None:
            self.context_id = context_id
        if start_time is not None:
            self.start_time = start_time
        if destinations is not None:
            self.destinations = destinations
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def status(self):
        """Gets the status of this ResignAttemptResponse.  # noqa: E501

        The status of the resigning operation.  # noqa: E501

        :return: The status of this ResignAttemptResponse.  # noqa: E501
        :rtype: string
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResignAttemptResponse.

        The status of the resigning operation.  # noqa: E501

        :param status: The status of this ResignAttemptResponse.  # noqa: E501
        :type: string
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def user_id(self):
        """Gets the user_id of this ResignAttemptResponse.  # noqa: E501

        ID of the user performing the resign operaiton.  # noqa: E501

        :return: The user_id of this ResignAttemptResponse.  # noqa: E501
        :rtype: string
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ResignAttemptResponse.

        ID of the user performing the resign operaiton.  # noqa: E501

        :param user_id: The user_id of this ResignAttemptResponse.  # noqa: E501
        :type: string
        """

        self._user_id = user_id

    @property
    def app_id(self):
        """Gets the app_id of this ResignAttemptResponse.  # noqa: E501

        App ID that the resign operation is being performed against.  # noqa: E501

        :return: The app_id of this ResignAttemptResponse.  # noqa: E501
        :rtype: string
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ResignAttemptResponse.

        App ID that the resign operation is being performed against.  # noqa: E501

        :param app_id: The app_id of this ResignAttemptResponse.  # noqa: E501
        :type: string
        """

        self._app_id = app_id

    @property
    def original_release_id(self):
        """Gets the original_release_id of this ResignAttemptResponse.  # noqa: E501

        ID of the release which is being resigned.  # noqa: E501

        :return: The original_release_id of this ResignAttemptResponse.  # noqa: E501
        :rtype: number
        """
        return self._original_release_id

    @original_release_id.setter
    def original_release_id(self, original_release_id):
        """Sets the original_release_id of this ResignAttemptResponse.

        ID of the release which is being resigned.  # noqa: E501

        :param original_release_id: The original_release_id of this ResignAttemptResponse.  # noqa: E501
        :type: number
        """

        self._original_release_id = original_release_id

    @property
    def resign_id(self):
        """Gets the resign_id of this ResignAttemptResponse.  # noqa: E501

        ID of the resign operation.  # noqa: E501

        :return: The resign_id of this ResignAttemptResponse.  # noqa: E501
        :rtype: string
        """
        return self._resign_id

    @resign_id.setter
    def resign_id(self, resign_id):
        """Sets the resign_id of this ResignAttemptResponse.

        ID of the resign operation.  # noqa: E501

        :param resign_id: The resign_id of this ResignAttemptResponse.  # noqa: E501
        :type: string
        """

        self._resign_id = resign_id

    @property
    def context_id(self):
        """Gets the context_id of this ResignAttemptResponse.  # noqa: E501

        Context ID for the resigning operation.  # noqa: E501

        :return: The context_id of this ResignAttemptResponse.  # noqa: E501
        :rtype: string
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """Sets the context_id of this ResignAttemptResponse.

        Context ID for the resigning operation.  # noqa: E501

        :param context_id: The context_id of this ResignAttemptResponse.  # noqa: E501
        :type: string
        """

        self._context_id = context_id

    @property
    def start_time(self):
        """Gets the start_time of this ResignAttemptResponse.  # noqa: E501

        The time that the resign operation was started.  # noqa: E501

        :return: The start_time of this ResignAttemptResponse.  # noqa: E501
        :rtype: number
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ResignAttemptResponse.

        The time that the resign operation was started.  # noqa: E501

        :param start_time: The start_time of this ResignAttemptResponse.  # noqa: E501
        :type: number
        """

        self._start_time = start_time

    @property
    def destinations(self):
        """Gets the destinations of this ResignAttemptResponse.  # noqa: E501

        List of destinations that the resign operation is being performed against.  # noqa: E501

        :return: The destinations of this ResignAttemptResponse.  # noqa: E501
        :rtype: array
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this ResignAttemptResponse.

        List of destinations that the resign operation is being performed against.  # noqa: E501

        :param destinations: The destinations of this ResignAttemptResponse.  # noqa: E501
        :type: array
        """

        self._destinations = destinations

    @property
    def error_code(self):
        """Gets the error_code of this ResignAttemptResponse.  # noqa: E501

        Error code associated with the exception.  # noqa: E501

        :return: The error_code of this ResignAttemptResponse.  # noqa: E501
        :rtype: string
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ResignAttemptResponse.

        Error code associated with the exception.  # noqa: E501

        :param error_code: The error_code of this ResignAttemptResponse.  # noqa: E501
        :type: string
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this ResignAttemptResponse.  # noqa: E501

        Error message associated with the exception.  # noqa: E501

        :return: The error_message of this ResignAttemptResponse.  # noqa: E501
        :rtype: string
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ResignAttemptResponse.

        Error message associated with the exception.  # noqa: E501

        :param error_message: The error_message of this ResignAttemptResponse.  # noqa: E501
        :type: string
        """

        self._error_message = error_message

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
        if not isinstance(other, ResignAttemptResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
