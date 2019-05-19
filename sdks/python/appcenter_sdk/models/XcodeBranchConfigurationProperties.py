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


class XcodeBranchConfigurationProperties(object):
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
        'project_or_workspace_path': 'string',
        'podfile_path': 'string',
        'cartfile_path': 'string',
        'provisioning_profile_encoded': 'string',
        'certificate_encoded': 'string',
        'provisioning_profile_file_id': 'string',
        'certificate_file_id': 'string',
        'provisioning_profile_upload_id': 'string',
        'app_extension_provisioning_profile_files': 'array',
        'certificate_upload_id': 'string',
        'certificate_password': 'string',
        'scheme': 'string',
        'xcode_version': 'string',
        'provisioning_profile_filename': 'string',
        'certificate_filename': 'string',
        'team_id': 'string',
        'automatic_signing': 'boolean',
        'xcode_project_sha': 'string',
        'archive_configuration': 'string',
        'target_to_archive': 'string',
        'force_legacy_build_system': 'boolean'
    }

    attribute_map = {
        'project_or_workspace_path': 'project_or_workspace_path',
        'podfile_path': 'podfile_path',
        'cartfile_path': 'cartfile_path',
        'provisioning_profile_encoded': 'provisioning_profile_encoded',
        'certificate_encoded': 'certificate_encoded',
        'provisioning_profile_file_id': 'provisioning_profile_file_id',
        'certificate_file_id': 'certificate_file_id',
        'provisioning_profile_upload_id': 'provisioning_profile_upload_id',
        'app_extension_provisioning_profile_files': 'app_extension_provisioning_profile_files',
        'certificate_upload_id': 'certificate_upload_id',
        'certificate_password': 'certificate_password',
        'scheme': 'scheme',
        'xcode_version': 'xcode_version',
        'provisioning_profile_filename': 'provisioning_profile_filename',
        'certificate_filename': 'certificate_filename',
        'team_id': 'team_id',
        'automatic_signing': 'automatic_signing',
        'xcode_project_sha': 'xcode_project_sha',
        'archive_configuration': 'archive_configuration',
        'target_to_archive': 'target_to_archive',
        'force_legacy_build_system': 'force_legacy_build_system'
    }

    def __init__(self, project_or_workspace_path=None, podfile_path=None, cartfile_path=None, provisioning_profile_encoded=None, certificate_encoded=None, provisioning_profile_file_id=None, certificate_file_id=None, provisioning_profile_upload_id=None, app_extension_provisioning_profile_files=None, certificate_upload_id=None, certificate_password=None, scheme=None, xcode_version=None, provisioning_profile_filename=None, certificate_filename=None, team_id=None, automatic_signing=None, xcode_project_sha=None, archive_configuration=None, target_to_archive=None, force_legacy_build_system=None):  # noqa: E501
        """XcodeBranchConfigurationProperties - a model defined in Swagger"""  # noqa: E501
        self._project_or_workspace_path = None
        self._podfile_path = None
        self._cartfile_path = None
        self._provisioning_profile_encoded = None
        self._certificate_encoded = None
        self._provisioning_profile_file_id = None
        self._certificate_file_id = None
        self._provisioning_profile_upload_id = None
        self._app_extension_provisioning_profile_files = None
        self._certificate_upload_id = None
        self._certificate_password = None
        self._scheme = None
        self._xcode_version = None
        self._provisioning_profile_filename = None
        self._certificate_filename = None
        self._team_id = None
        self._automatic_signing = None
        self._xcode_project_sha = None
        self._archive_configuration = None
        self._target_to_archive = None
        self._force_legacy_build_system = None
        self.discriminator = None
        if project_or_workspace_path is not None:
            self.project_or_workspace_path = project_or_workspace_path
        if podfile_path is not None:
            self.podfile_path = podfile_path
        if cartfile_path is not None:
            self.cartfile_path = cartfile_path
        if provisioning_profile_encoded is not None:
            self.provisioning_profile_encoded = provisioning_profile_encoded
        if certificate_encoded is not None:
            self.certificate_encoded = certificate_encoded
        if provisioning_profile_file_id is not None:
            self.provisioning_profile_file_id = provisioning_profile_file_id
        if certificate_file_id is not None:
            self.certificate_file_id = certificate_file_id
        if provisioning_profile_upload_id is not None:
            self.provisioning_profile_upload_id = provisioning_profile_upload_id
        if app_extension_provisioning_profile_files is not None:
            self.app_extension_provisioning_profile_files = app_extension_provisioning_profile_files
        if certificate_upload_id is not None:
            self.certificate_upload_id = certificate_upload_id
        if certificate_password is not None:
            self.certificate_password = certificate_password
        self.scheme = scheme
        if xcode_version is not None:
            self.xcode_version = xcode_version
        if provisioning_profile_filename is not None:
            self.provisioning_profile_filename = provisioning_profile_filename
        if certificate_filename is not None:
            self.certificate_filename = certificate_filename
        if team_id is not None:
            self.team_id = team_id
        if automatic_signing is not None:
            self.automatic_signing = automatic_signing
        if xcode_project_sha is not None:
            self.xcode_project_sha = xcode_project_sha
        if archive_configuration is not None:
            self.archive_configuration = archive_configuration
        if target_to_archive is not None:
            self.target_to_archive = target_to_archive
        if force_legacy_build_system is not None:
            self.force_legacy_build_system = force_legacy_build_system

    @property
    def project_or_workspace_path(self):
        """Gets the project_or_workspace_path of this XcodeBranchConfigurationProperties.  # noqa: E501

        Xcode project/workspace path  # noqa: E501

        :return: The project_or_workspace_path of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._project_or_workspace_path

    @project_or_workspace_path.setter
    def project_or_workspace_path(self, project_or_workspace_path):
        """Sets the project_or_workspace_path of this XcodeBranchConfigurationProperties.

        Xcode project/workspace path  # noqa: E501

        :param project_or_workspace_path: The project_or_workspace_path of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._project_or_workspace_path = project_or_workspace_path

    @property
    def podfile_path(self):
        """Gets the podfile_path of this XcodeBranchConfigurationProperties.  # noqa: E501

        Path to CococaPods file, if present  # noqa: E501

        :return: The podfile_path of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._podfile_path

    @podfile_path.setter
    def podfile_path(self, podfile_path):
        """Sets the podfile_path of this XcodeBranchConfigurationProperties.

        Path to CococaPods file, if present  # noqa: E501

        :param podfile_path: The podfile_path of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._podfile_path = podfile_path

    @property
    def cartfile_path(self):
        """Gets the cartfile_path of this XcodeBranchConfigurationProperties.  # noqa: E501

        Path to Carthage file, if present  # noqa: E501

        :return: The cartfile_path of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._cartfile_path

    @cartfile_path.setter
    def cartfile_path(self, cartfile_path):
        """Sets the cartfile_path of this XcodeBranchConfigurationProperties.

        Path to Carthage file, if present  # noqa: E501

        :param cartfile_path: The cartfile_path of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._cartfile_path = cartfile_path

    @property
    def provisioning_profile_encoded(self):
        """Gets the provisioning_profile_encoded of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The provisioning_profile_encoded of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._provisioning_profile_encoded

    @provisioning_profile_encoded.setter
    def provisioning_profile_encoded(self, provisioning_profile_encoded):
        """Sets the provisioning_profile_encoded of this XcodeBranchConfigurationProperties.


        :param provisioning_profile_encoded: The provisioning_profile_encoded of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._provisioning_profile_encoded = provisioning_profile_encoded

    @property
    def certificate_encoded(self):
        """Gets the certificate_encoded of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The certificate_encoded of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._certificate_encoded

    @certificate_encoded.setter
    def certificate_encoded(self, certificate_encoded):
        """Sets the certificate_encoded of this XcodeBranchConfigurationProperties.


        :param certificate_encoded: The certificate_encoded of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._certificate_encoded = certificate_encoded

    @property
    def provisioning_profile_file_id(self):
        """Gets the provisioning_profile_file_id of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The provisioning_profile_file_id of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._provisioning_profile_file_id

    @provisioning_profile_file_id.setter
    def provisioning_profile_file_id(self, provisioning_profile_file_id):
        """Sets the provisioning_profile_file_id of this XcodeBranchConfigurationProperties.


        :param provisioning_profile_file_id: The provisioning_profile_file_id of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._provisioning_profile_file_id = provisioning_profile_file_id

    @property
    def certificate_file_id(self):
        """Gets the certificate_file_id of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The certificate_file_id of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._certificate_file_id

    @certificate_file_id.setter
    def certificate_file_id(self, certificate_file_id):
        """Sets the certificate_file_id of this XcodeBranchConfigurationProperties.


        :param certificate_file_id: The certificate_file_id of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._certificate_file_id = certificate_file_id

    @property
    def provisioning_profile_upload_id(self):
        """Gets the provisioning_profile_upload_id of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The provisioning_profile_upload_id of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._provisioning_profile_upload_id

    @provisioning_profile_upload_id.setter
    def provisioning_profile_upload_id(self, provisioning_profile_upload_id):
        """Sets the provisioning_profile_upload_id of this XcodeBranchConfigurationProperties.


        :param provisioning_profile_upload_id: The provisioning_profile_upload_id of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._provisioning_profile_upload_id = provisioning_profile_upload_id

    @property
    def app_extension_provisioning_profile_files(self):
        """Gets the app_extension_provisioning_profile_files of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The app_extension_provisioning_profile_files of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: array
        """
        return self._app_extension_provisioning_profile_files

    @app_extension_provisioning_profile_files.setter
    def app_extension_provisioning_profile_files(self, app_extension_provisioning_profile_files):
        """Sets the app_extension_provisioning_profile_files of this XcodeBranchConfigurationProperties.


        :param app_extension_provisioning_profile_files: The app_extension_provisioning_profile_files of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: array
        """

        self._app_extension_provisioning_profile_files = app_extension_provisioning_profile_files

    @property
    def certificate_upload_id(self):
        """Gets the certificate_upload_id of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The certificate_upload_id of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._certificate_upload_id

    @certificate_upload_id.setter
    def certificate_upload_id(self, certificate_upload_id):
        """Sets the certificate_upload_id of this XcodeBranchConfigurationProperties.


        :param certificate_upload_id: The certificate_upload_id of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._certificate_upload_id = certificate_upload_id

    @property
    def certificate_password(self):
        """Gets the certificate_password of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The certificate_password of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._certificate_password

    @certificate_password.setter
    def certificate_password(self, certificate_password):
        """Sets the certificate_password of this XcodeBranchConfigurationProperties.


        :param certificate_password: The certificate_password of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._certificate_password = certificate_password

    @property
    def scheme(self):
        """Gets the scheme of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The scheme of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this XcodeBranchConfigurationProperties.


        :param scheme: The scheme of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """
        if scheme is None:
            raise ValueError("Invalid value for `scheme`, must not be `None`")  # noqa: E501

        self._scheme = scheme

    @property
    def xcode_version(self):
        """Gets the xcode_version of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The xcode_version of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._xcode_version

    @xcode_version.setter
    def xcode_version(self, xcode_version):
        """Sets the xcode_version of this XcodeBranchConfigurationProperties.


        :param xcode_version: The xcode_version of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._xcode_version = xcode_version

    @property
    def provisioning_profile_filename(self):
        """Gets the provisioning_profile_filename of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The provisioning_profile_filename of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._provisioning_profile_filename

    @provisioning_profile_filename.setter
    def provisioning_profile_filename(self, provisioning_profile_filename):
        """Sets the provisioning_profile_filename of this XcodeBranchConfigurationProperties.


        :param provisioning_profile_filename: The provisioning_profile_filename of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._provisioning_profile_filename = provisioning_profile_filename

    @property
    def certificate_filename(self):
        """Gets the certificate_filename of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The certificate_filename of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._certificate_filename

    @certificate_filename.setter
    def certificate_filename(self, certificate_filename):
        """Sets the certificate_filename of this XcodeBranchConfigurationProperties.


        :param certificate_filename: The certificate_filename of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._certificate_filename = certificate_filename

    @property
    def team_id(self):
        """Gets the team_id of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The team_id of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this XcodeBranchConfigurationProperties.


        :param team_id: The team_id of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._team_id = team_id

    @property
    def automatic_signing(self):
        """Gets the automatic_signing of this XcodeBranchConfigurationProperties.  # noqa: E501


        :return: The automatic_signing of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: boolean
        """
        return self._automatic_signing

    @automatic_signing.setter
    def automatic_signing(self, automatic_signing):
        """Sets the automatic_signing of this XcodeBranchConfigurationProperties.


        :param automatic_signing: The automatic_signing of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: boolean
        """

        self._automatic_signing = automatic_signing

    @property
    def xcode_project_sha(self):
        """Gets the xcode_project_sha of this XcodeBranchConfigurationProperties.  # noqa: E501

        The selected pbxproject hash to the repositroy  # noqa: E501

        :return: The xcode_project_sha of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._xcode_project_sha

    @xcode_project_sha.setter
    def xcode_project_sha(self, xcode_project_sha):
        """Sets the xcode_project_sha of this XcodeBranchConfigurationProperties.

        The selected pbxproject hash to the repositroy  # noqa: E501

        :param xcode_project_sha: The xcode_project_sha of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._xcode_project_sha = xcode_project_sha

    @property
    def archive_configuration(self):
        """Gets the archive_configuration of this XcodeBranchConfigurationProperties.  # noqa: E501

        The build configuration of the target to archive  # noqa: E501

        :return: The archive_configuration of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._archive_configuration

    @archive_configuration.setter
    def archive_configuration(self, archive_configuration):
        """Sets the archive_configuration of this XcodeBranchConfigurationProperties.

        The build configuration of the target to archive  # noqa: E501

        :param archive_configuration: The archive_configuration of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._archive_configuration = archive_configuration

    @property
    def target_to_archive(self):
        """Gets the target_to_archive of this XcodeBranchConfigurationProperties.  # noqa: E501

        The target id of the selected scheme to archive  # noqa: E501

        :return: The target_to_archive of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: string
        """
        return self._target_to_archive

    @target_to_archive.setter
    def target_to_archive(self, target_to_archive):
        """Sets the target_to_archive of this XcodeBranchConfigurationProperties.

        The target id of the selected scheme to archive  # noqa: E501

        :param target_to_archive: The target_to_archive of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: string
        """

        self._target_to_archive = target_to_archive

    @property
    def force_legacy_build_system(self):
        """Gets the force_legacy_build_system of this XcodeBranchConfigurationProperties.  # noqa: E501

        Setting this to true forces the build to use Xcode legacy build system. Otherwise, the setting from workspace settings is used.
By default new build system is used if workspace setting is not committed to the repository. Only used for iOS React Native app, with Xcode 10.
  # noqa: E501

        :return: The force_legacy_build_system of this XcodeBranchConfigurationProperties.  # noqa: E501
        :rtype: boolean
        """
        return self._force_legacy_build_system

    @force_legacy_build_system.setter
    def force_legacy_build_system(self, force_legacy_build_system):
        """Sets the force_legacy_build_system of this XcodeBranchConfigurationProperties.

        Setting this to true forces the build to use Xcode legacy build system. Otherwise, the setting from workspace settings is used.
By default new build system is used if workspace setting is not committed to the repository. Only used for iOS React Native app, with Xcode 10.
  # noqa: E501

        :param force_legacy_build_system: The force_legacy_build_system of this XcodeBranchConfigurationProperties.  # noqa: E501
        :type: boolean
        """

        self._force_legacy_build_system = force_legacy_build_system

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
        if not isinstance(other, XcodeBranchConfigurationProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
