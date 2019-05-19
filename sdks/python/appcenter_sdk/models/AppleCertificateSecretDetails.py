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


class AppleCertificateSecretDetails(object):
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
        'base64_certificate': 'string',
        'password': 'string',
        'display_name': 'string',
        'certificate_validity_start_date': 'string',
        'certificate_validity_end_date': 'string'
    }

    attribute_map = {
        'base64_certificate': 'base64_certificate',
        'password': 'password',
        'display_name': 'display_name',
        'certificate_validity_start_date': 'certificate_validity_start_date',
        'certificate_validity_end_date': 'certificate_validity_end_date'
    }

    def __init__(self, base64_certificate=None, password=None, display_name=None, certificate_validity_start_date=None, certificate_validity_end_date=None):  # noqa: E501
        """AppleCertificateSecretDetails - a model defined in Swagger"""  # noqa: E501
        self._base64_certificate = None
        self._password = None
        self._display_name = None
        self._certificate_validity_start_date = None
        self._certificate_validity_end_date = None
        self.discriminator = None
        if base64_certificate is not None:
            self.base64_certificate = base64_certificate
        self.password = password
        if display_name is not None:
            self.display_name = display_name
        if certificate_validity_start_date is not None:
            self.certificate_validity_start_date = certificate_validity_start_date
        if certificate_validity_end_date is not None:
            self.certificate_validity_end_date = certificate_validity_end_date

    @property
    def base64_certificate(self):
        """Gets the base64_certificate of this AppleCertificateSecretDetails.  # noqa: E501

        The certificate contents in base 64 encoded string  # noqa: E501

        :return: The base64_certificate of this AppleCertificateSecretDetails.  # noqa: E501
        :rtype: string
        """
        return self._base64_certificate

    @base64_certificate.setter
    def base64_certificate(self, base64_certificate):
        """Sets the base64_certificate of this AppleCertificateSecretDetails.

        The certificate contents in base 64 encoded string  # noqa: E501

        :param base64_certificate: The base64_certificate of this AppleCertificateSecretDetails.  # noqa: E501
        :type: string
        """

        self._base64_certificate = base64_certificate

    @property
    def password(self):
        """Gets the password of this AppleCertificateSecretDetails.  # noqa: E501

        The password for the certificate  # noqa: E501

        :return: The password of this AppleCertificateSecretDetails.  # noqa: E501
        :rtype: string
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AppleCertificateSecretDetails.

        The password for the certificate  # noqa: E501

        :param password: The password of this AppleCertificateSecretDetails.  # noqa: E501
        :type: string
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def display_name(self):
        """Gets the display_name of this AppleCertificateSecretDetails.  # noqa: E501

        The display name (CN) of the certificate  # noqa: E501

        :return: The display_name of this AppleCertificateSecretDetails.  # noqa: E501
        :rtype: string
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AppleCertificateSecretDetails.

        The display name (CN) of the certificate  # noqa: E501

        :param display_name: The display_name of this AppleCertificateSecretDetails.  # noqa: E501
        :type: string
        """

        self._display_name = display_name

    @property
    def certificate_validity_start_date(self):
        """Gets the certificate_validity_start_date of this AppleCertificateSecretDetails.  # noqa: E501

        The date-time from which the certificate is valid  # noqa: E501

        :return: The certificate_validity_start_date of this AppleCertificateSecretDetails.  # noqa: E501
        :rtype: string
        """
        return self._certificate_validity_start_date

    @certificate_validity_start_date.setter
    def certificate_validity_start_date(self, certificate_validity_start_date):
        """Sets the certificate_validity_start_date of this AppleCertificateSecretDetails.

        The date-time from which the certificate is valid  # noqa: E501

        :param certificate_validity_start_date: The certificate_validity_start_date of this AppleCertificateSecretDetails.  # noqa: E501
        :type: string
        """

        self._certificate_validity_start_date = certificate_validity_start_date

    @property
    def certificate_validity_end_date(self):
        """Gets the certificate_validity_end_date of this AppleCertificateSecretDetails.  # noqa: E501

        The date-time till which the certificate is valid  # noqa: E501

        :return: The certificate_validity_end_date of this AppleCertificateSecretDetails.  # noqa: E501
        :rtype: string
        """
        return self._certificate_validity_end_date

    @certificate_validity_end_date.setter
    def certificate_validity_end_date(self, certificate_validity_end_date):
        """Sets the certificate_validity_end_date of this AppleCertificateSecretDetails.

        The date-time till which the certificate is valid  # noqa: E501

        :param certificate_validity_end_date: The certificate_validity_end_date of this AppleCertificateSecretDetails.  # noqa: E501
        :type: string
        """

        self._certificate_validity_end_date = certificate_validity_end_date

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
        if not isinstance(other, AppleCertificateSecretDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
