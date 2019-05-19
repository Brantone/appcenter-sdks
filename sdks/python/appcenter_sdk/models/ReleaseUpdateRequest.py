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


class ReleaseUpdateRequest(object):
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
        'distribution_group_name': 'string',
        'distribution_group_id': 'string',
        'destination_name': 'string',
        'destination_id': 'string',
        'destination_type': 'string',
        'release_notes': 'string',
        'mandatory_update': 'boolean',
        'destinations': 'array',
        'build': 'object',
        'notify_testers': 'boolean'
    }

    attribute_map = {
        'distribution_group_name': 'distribution_group_name',
        'distribution_group_id': 'distribution_group_id',
        'destination_name': 'destination_name',
        'destination_id': 'destination_id',
        'destination_type': 'destination_type',
        'release_notes': 'release_notes',
        'mandatory_update': 'mandatory_update',
        'destinations': 'destinations',
        'build': 'build',
        'notify_testers': 'notify_testers'
    }

    def __init__(self, distribution_group_name=None, distribution_group_id=None, destination_name=None, destination_id=None, destination_type=None, release_notes=None, mandatory_update=None, destinations=None, build=None, notify_testers=None):  # noqa: E501
        """ReleaseUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._distribution_group_name = None
        self._distribution_group_id = None
        self._destination_name = None
        self._destination_id = None
        self._destination_type = None
        self._release_notes = None
        self._mandatory_update = None
        self._destinations = None
        self._build = None
        self._notify_testers = None
        self.discriminator = None
        if distribution_group_name is not None:
            self.distribution_group_name = distribution_group_name
        if distribution_group_id is not None:
            self.distribution_group_id = distribution_group_id
        if destination_name is not None:
            self.destination_name = destination_name
        if destination_id is not None:
            self.destination_id = destination_id
        if destination_type is not None:
            self.destination_type = destination_type
        if release_notes is not None:
            self.release_notes = release_notes
        if mandatory_update is not None:
            self.mandatory_update = mandatory_update
        if destinations is not None:
            self.destinations = destinations
        if build is not None:
            self.build = build
        if notify_testers is not None:
            self.notify_testers = notify_testers

    @property
    def distribution_group_name(self):
        """Gets the distribution_group_name of this ReleaseUpdateRequest.  # noqa: E501

        OBSOLETE. Will be removed in future releases - use destinations instead. Name of a distribution group. The release will be associated with this distribution group. If the distribution group doesn't exist a 400 is returned. If both distribution group name and id are passed, the id is taking precedence.
  # noqa: E501

        :return: The distribution_group_name of this ReleaseUpdateRequest.  # noqa: E501
        :rtype: string
        """
        return self._distribution_group_name

    @distribution_group_name.setter
    def distribution_group_name(self, distribution_group_name):
        """Sets the distribution_group_name of this ReleaseUpdateRequest.

        OBSOLETE. Will be removed in future releases - use destinations instead. Name of a distribution group. The release will be associated with this distribution group. If the distribution group doesn't exist a 400 is returned. If both distribution group name and id are passed, the id is taking precedence.
  # noqa: E501

        :param distribution_group_name: The distribution_group_name of this ReleaseUpdateRequest.  # noqa: E501
        :type: string
        """

        self._distribution_group_name = distribution_group_name

    @property
    def distribution_group_id(self):
        """Gets the distribution_group_id of this ReleaseUpdateRequest.  # noqa: E501

        OBSOLETE. Will be removed in future releases - use destinations instead. Id of a distribution group. The release will be associated with this distribution group. If the distribution group doesn't exist a 400 is returned. If both distribution group name and id are passed, the id is taking precedence.
  # noqa: E501

        :return: The distribution_group_id of this ReleaseUpdateRequest.  # noqa: E501
        :rtype: string
        """
        return self._distribution_group_id

    @distribution_group_id.setter
    def distribution_group_id(self, distribution_group_id):
        """Sets the distribution_group_id of this ReleaseUpdateRequest.

        OBSOLETE. Will be removed in future releases - use destinations instead. Id of a distribution group. The release will be associated with this distribution group. If the distribution group doesn't exist a 400 is returned. If both distribution group name and id are passed, the id is taking precedence.
  # noqa: E501

        :param distribution_group_id: The distribution_group_id of this ReleaseUpdateRequest.  # noqa: E501
        :type: string
        """

        self._distribution_group_id = distribution_group_id

    @property
    def destination_name(self):
        """Gets the destination_name of this ReleaseUpdateRequest.  # noqa: E501

        OBSOLETE. Will be removed in future releases - use destinations instead. Name of a destination. The release will be associated with this destination. If the destination doesn't exist a 400 is returned. If both distribution group name and id are passed, the id is taking precedence.
  # noqa: E501

        :return: The destination_name of this ReleaseUpdateRequest.  # noqa: E501
        :rtype: string
        """
        return self._destination_name

    @destination_name.setter
    def destination_name(self, destination_name):
        """Sets the destination_name of this ReleaseUpdateRequest.

        OBSOLETE. Will be removed in future releases - use destinations instead. Name of a destination. The release will be associated with this destination. If the destination doesn't exist a 400 is returned. If both distribution group name and id are passed, the id is taking precedence.
  # noqa: E501

        :param destination_name: The destination_name of this ReleaseUpdateRequest.  # noqa: E501
        :type: string
        """

        self._destination_name = destination_name

    @property
    def destination_id(self):
        """Gets the destination_id of this ReleaseUpdateRequest.  # noqa: E501

        OBSOLETE. Will be removed in future releases - use destinations instead. Id of a destination. The release will be associated with this destination. If the destination doesn't exist a 400 is returned. If both destination name and id are passed, the id is taking precedence.
  # noqa: E501

        :return: The destination_id of this ReleaseUpdateRequest.  # noqa: E501
        :rtype: string
        """
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        """Sets the destination_id of this ReleaseUpdateRequest.

        OBSOLETE. Will be removed in future releases - use destinations instead. Id of a destination. The release will be associated with this destination. If the destination doesn't exist a 400 is returned. If both destination name and id are passed, the id is taking precedence.
  # noqa: E501

        :param destination_id: The destination_id of this ReleaseUpdateRequest.  # noqa: E501
        :type: string
        """

        self._destination_id = destination_id

    @property
    def destination_type(self):
        """Gets the destination_type of this ReleaseUpdateRequest.  # noqa: E501

        Not used anymore.  # noqa: E501

        :return: The destination_type of this ReleaseUpdateRequest.  # noqa: E501
        :rtype: string
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this ReleaseUpdateRequest.

        Not used anymore.  # noqa: E501

        :param destination_type: The destination_type of this ReleaseUpdateRequest.  # noqa: E501
        :type: string
        """

        self._destination_type = destination_type

    @property
    def release_notes(self):
        """Gets the release_notes of this ReleaseUpdateRequest.  # noqa: E501

        Release notes for this release.  # noqa: E501

        :return: The release_notes of this ReleaseUpdateRequest.  # noqa: E501
        :rtype: string
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this ReleaseUpdateRequest.

        Release notes for this release.  # noqa: E501

        :param release_notes: The release_notes of this ReleaseUpdateRequest.  # noqa: E501
        :type: string
        """

        self._release_notes = release_notes

    @property
    def mandatory_update(self):
        """Gets the mandatory_update of this ReleaseUpdateRequest.  # noqa: E501

        A boolean which determines whether this version should be a mandatory update or not.  # noqa: E501

        :return: The mandatory_update of this ReleaseUpdateRequest.  # noqa: E501
        :rtype: boolean
        """
        return self._mandatory_update

    @mandatory_update.setter
    def mandatory_update(self, mandatory_update):
        """Sets the mandatory_update of this ReleaseUpdateRequest.

        A boolean which determines whether this version should be a mandatory update or not.  # noqa: E501

        :param mandatory_update: The mandatory_update of this ReleaseUpdateRequest.  # noqa: E501
        :type: boolean
        """

        self._mandatory_update = mandatory_update

    @property
    def destinations(self):
        """Gets the destinations of this ReleaseUpdateRequest.  # noqa: E501

        Distribute this release under the following list of destinations (store groups or distribution groups).  # noqa: E501

        :return: The destinations of this ReleaseUpdateRequest.  # noqa: E501
        :rtype: array
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this ReleaseUpdateRequest.

        Distribute this release under the following list of destinations (store groups or distribution groups).  # noqa: E501

        :param destinations: The destinations of this ReleaseUpdateRequest.  # noqa: E501
        :type: array
        """

        self._destinations = destinations

    @property
    def build(self):
        """Gets the build of this ReleaseUpdateRequest.  # noqa: E501

        Contains metadata about the build that produced the release being uploaded  # noqa: E501

        :return: The build of this ReleaseUpdateRequest.  # noqa: E501
        :rtype: object
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ReleaseUpdateRequest.

        Contains metadata about the build that produced the release being uploaded  # noqa: E501

        :param build: The build of this ReleaseUpdateRequest.  # noqa: E501
        :type: object
        """

        self._build = build

    @property
    def notify_testers(self):
        """Gets the notify_testers of this ReleaseUpdateRequest.  # noqa: E501

        A boolean which determines whether to notify testers of a new release, default to false.  # noqa: E501

        :return: The notify_testers of this ReleaseUpdateRequest.  # noqa: E501
        :rtype: boolean
        """
        return self._notify_testers

    @notify_testers.setter
    def notify_testers(self, notify_testers):
        """Sets the notify_testers of this ReleaseUpdateRequest.

        A boolean which determines whether to notify testers of a new release, default to false.  # noqa: E501

        :param notify_testers: The notify_testers of this ReleaseUpdateRequest.  # noqa: E501
        :type: boolean
        """

        self._notify_testers = notify_testers

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
        if not isinstance(other, ReleaseUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
