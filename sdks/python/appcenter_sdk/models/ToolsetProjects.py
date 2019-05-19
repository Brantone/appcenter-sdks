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


class ToolsetProjects(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    Appium = "Appium"
    Calabash = "Calabash"
    Espresso = "Espresso"
    UITest = "UITest"
    Generated = "Generated"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'commit': 'string',
        'xcode': '',
        'javascript': '',
        'xamarin': '',
        'android': '',
        'buildscripts': '',
        'uwp': '',
        'testcloud': ''
    }

    attribute_map = {
        'commit': 'commit',
        'xcode': 'xcode',
        'javascript': 'javascript',
        'xamarin': 'xamarin',
        'android': 'android',
        'buildscripts': 'buildscripts',
        'uwp': 'uwp',
        'testcloud': 'testcloud'
    }

    def __init__(self, commit=None, xcode=None, javascript=None, xamarin=None, android=None, buildscripts=None, uwp=None, testcloud=None):  # noqa: E501
        """ToolsetProjects - a model defined in Swagger"""  # noqa: E501
        self._commit = None
        self._xcode = None
        self._javascript = None
        self._xamarin = None
        self._android = None
        self._buildscripts = None
        self._uwp = None
        self._testcloud = None
        self.discriminator = None
        if commit is not None:
            self.commit = commit
        if xcode is not None:
            self.xcode = xcode
        if javascript is not None:
            self.javascript = javascript
        if xamarin is not None:
            self.xamarin = xamarin
        if android is not None:
            self.android = android
        if buildscripts is not None:
            self.buildscripts = buildscripts
        if uwp is not None:
            self.uwp = uwp
        if testcloud is not None:
            self.testcloud = testcloud

    @property
    def commit(self):
        """Gets the commit of this ToolsetProjects.  # noqa: E501

        The commit hash of the analyzed commit  # noqa: E501

        :return: The commit of this ToolsetProjects.  # noqa: E501
        :rtype: string
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this ToolsetProjects.

        The commit hash of the analyzed commit  # noqa: E501

        :param commit: The commit of this ToolsetProjects.  # noqa: E501
        :type: string
        """

        self._commit = commit

    @property
    def xcode(self):
        """Gets the xcode of this ToolsetProjects.  # noqa: E501


        :return: The xcode of this ToolsetProjects.  # noqa: E501
        :rtype: 
        """
        return self._xcode

    @xcode.setter
    def xcode(self, xcode):
        """Sets the xcode of this ToolsetProjects.


        :param xcode: The xcode of this ToolsetProjects.  # noqa: E501
        :type: 
        """

        self._xcode = xcode

    @property
    def javascript(self):
        """Gets the javascript of this ToolsetProjects.  # noqa: E501


        :return: The javascript of this ToolsetProjects.  # noqa: E501
        :rtype: 
        """
        return self._javascript

    @javascript.setter
    def javascript(self, javascript):
        """Sets the javascript of this ToolsetProjects.


        :param javascript: The javascript of this ToolsetProjects.  # noqa: E501
        :type: 
        """

        self._javascript = javascript

    @property
    def xamarin(self):
        """Gets the xamarin of this ToolsetProjects.  # noqa: E501


        :return: The xamarin of this ToolsetProjects.  # noqa: E501
        :rtype: 
        """
        return self._xamarin

    @xamarin.setter
    def xamarin(self, xamarin):
        """Sets the xamarin of this ToolsetProjects.


        :param xamarin: The xamarin of this ToolsetProjects.  # noqa: E501
        :type: 
        """

        self._xamarin = xamarin

    @property
    def android(self):
        """Gets the android of this ToolsetProjects.  # noqa: E501


        :return: The android of this ToolsetProjects.  # noqa: E501
        :rtype: 
        """
        return self._android

    @android.setter
    def android(self, android):
        """Sets the android of this ToolsetProjects.


        :param android: The android of this ToolsetProjects.  # noqa: E501
        :type: 
        """

        self._android = android

    @property
    def buildscripts(self):
        """Gets the buildscripts of this ToolsetProjects.  # noqa: E501

        A collection of detected pre/post buildscripts for current platform toolset  # noqa: E501

        :return: The buildscripts of this ToolsetProjects.  # noqa: E501
        :rtype: 
        """
        return self._buildscripts

    @buildscripts.setter
    def buildscripts(self, buildscripts):
        """Sets the buildscripts of this ToolsetProjects.

        A collection of detected pre/post buildscripts for current platform toolset  # noqa: E501

        :param buildscripts: The buildscripts of this ToolsetProjects.  # noqa: E501
        :type: 
        """

        self._buildscripts = buildscripts

    @property
    def uwp(self):
        """Gets the uwp of this ToolsetProjects.  # noqa: E501


        :return: The uwp of this ToolsetProjects.  # noqa: E501
        :rtype: 
        """
        return self._uwp

    @uwp.setter
    def uwp(self, uwp):
        """Sets the uwp of this ToolsetProjects.


        :param uwp: The uwp of this ToolsetProjects.  # noqa: E501
        :type: 
        """

        self._uwp = uwp

    @property
    def testcloud(self):
        """Gets the testcloud of this ToolsetProjects.  # noqa: E501


        :return: The testcloud of this ToolsetProjects.  # noqa: E501
        :rtype: 
        """
        return self._testcloud

    @testcloud.setter
    def testcloud(self, testcloud):
        """Sets the testcloud of this ToolsetProjects.


        :param testcloud: The testcloud of this ToolsetProjects.  # noqa: E501
        :type: 
        """

        self._testcloud = testcloud

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
        if not isinstance(other, ToolsetProjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
