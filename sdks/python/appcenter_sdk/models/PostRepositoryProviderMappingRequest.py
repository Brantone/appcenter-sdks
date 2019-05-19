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


class PostRepositoryProviderMappingRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    github = "github"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'external_account_id': 'string',
        'provider': 'string',
        'account_id': 'string'
    }

    attribute_map = {
        'external_account_id': 'external_account_id',
        'provider': 'provider',
        'account_id': 'account_id'
    }

    def __init__(self, external_account_id=None, provider=None, account_id=None):  # noqa: E501
        """PostRepositoryProviderMappingRequest - a model defined in Swagger"""  # noqa: E501
        self._external_account_id = None
        self._provider = None
        self._account_id = None
        self.discriminator = None
        self.external_account_id = external_account_id
        self.provider = provider
        self.account_id = account_id

    @property
    def external_account_id(self):
        """Gets the external_account_id of this PostRepositoryProviderMappingRequest.  # noqa: E501

        Id of user in the external provider service  # noqa: E501

        :return: The external_account_id of this PostRepositoryProviderMappingRequest.  # noqa: E501
        :rtype: string
        """
        return self._external_account_id

    @external_account_id.setter
    def external_account_id(self, external_account_id):
        """Sets the external_account_id of this PostRepositoryProviderMappingRequest.

        Id of user in the external provider service  # noqa: E501

        :param external_account_id: The external_account_id of this PostRepositoryProviderMappingRequest.  # noqa: E501
        :type: string
        """
        if external_account_id is None:
            raise ValueError("Invalid value for `external_account_id`, must not be `None`")  # noqa: E501

        self._external_account_id = external_account_id

    @property
    def provider(self):
        """Gets the provider of this PostRepositoryProviderMappingRequest.  # noqa: E501

        Supported external providers of source control repositories  # noqa: E501

        :return: The provider of this PostRepositoryProviderMappingRequest.  # noqa: E501
        :rtype: string
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this PostRepositoryProviderMappingRequest.

        Supported external providers of source control repositories  # noqa: E501

        :param provider: The provider of this PostRepositoryProviderMappingRequest.  # noqa: E501
        :type: string
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = [undefined, ]  # noqa: E501

        self._provider = provider

    @property
    def account_id(self):
        """Gets the account_id of this PostRepositoryProviderMappingRequest.  # noqa: E501

        App Center account id to link to this provider and external id  # noqa: E501

        :return: The account_id of this PostRepositoryProviderMappingRequest.  # noqa: E501
        :rtype: string
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PostRepositoryProviderMappingRequest.

        App Center account id to link to this provider and external id  # noqa: E501

        :param account_id: The account_id of this PostRepositoryProviderMappingRequest.  # noqa: E501
        :type: string
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

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
        if not isinstance(other, PostRepositoryProviderMappingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other