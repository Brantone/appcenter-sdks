# coding: utf-8

"""
    App Center Client

    Microsoft Visual Studio App Center API  # noqa: E501

    OpenAPI spec version: preview
    Contact: benedetto.abbenanti@gmail.com
    Project Repository: https://github.com/b3nab/appcenter-sdks
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from appcenter_sdk.api_client import ApiClient


class mbaasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def data_getResourceProvisioning(self, owner_name, app_name, **kwargs):  # noqa: E501
        """data_getResourceProvisioning  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_getResourceProvisioning(owner_name, app_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param string owner_name: The name of the owner (required)
        :param string app_name: The name of the application (required)
        :return: ErrorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.data_getResourceProvisioning_with_http_info(owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_getResourceProvisioning_with_http_info(owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def data_getResourceProvisioning_with_http_info(self, owner_name, app_name, **kwargs):  # noqa: E501
        """data_getResourceProvisioning  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_getResourceProvisioning_with_http_info(owner_name, app_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param string owner_name: The name of the owner (required)
        :param string app_name: The name of the application (required)
        :return: ErrorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_name', 'app_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_getResourceProvisioning" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `data_getResourceProvisioning`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `data_getResourceProvisioning`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'text/plain', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data', 'application/json-patch+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/data/resource_provisioning', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ErrorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_postResourceProvisioning(self, AC-Authorization-ARM, owner_name, app_name, **kwargs):  # noqa: E501
        """  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_postResourceProvisioning(AC-Authorization-ARM, owner_name, app_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param string AC-Authorization-ARM: (required)
        :param string owner_name: The name of the owner (required)
        :param string app_name: The name of the application (required)
        :param object body:(optional)
        :return: ErrorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.data_postResourceProvisioning_with_http_info(AC-Authorization-ARM, owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_postResourceProvisioning_with_http_info(AC-Authorization-ARM, owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def data_postResourceProvisioning_with_http_info(self, AC-Authorization-ARM, owner_name, app_name, **kwargs):  # noqa: E501
        """  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_postResourceProvisioning_with_http_info(AC-Authorization-ARM, owner_name, app_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param string AC-Authorization-ARM: (required)
        :param string owner_name: The name of the owner (required)
        :param string app_name: The name of the application (required)
        :param object body:(optional)
        :return: ErrorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['AC-Authorization-ARM', 'owner_name', 'app_name', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_postResourceProvisioning" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'AC-Authorization-ARM' is set
        if ('AC-Authorization-ARM' not in params or
                params['AC-Authorization-ARM'] is None):
            raise ValueError("Missing the required parameter `AC-Authorization-ARM` when calling `data_postResourceProvisioning`")  # noqa: E501
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `data_postResourceProvisioning`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `data_postResourceProvisioning`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'AC-Authorization-ARM' in params:
            header_params['AC-Authorization-ARM'] = params['AC-Authorization-ARM']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'text/plain', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/data/resource_provisioning', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ErrorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_getOverview(self, AC-Authorization-ARM, owner_name, app_name, **kwargs):  # noqa: E501
        """  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_getOverview(AC-Authorization-ARM, owner_name, app_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param string AC-Authorization-ARM: ARM token (required)
        :param string owner_name: The name of the owner (required)
        :param string app_name: The name of the application (required)
        :return: ErrorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.data_getOverview_with_http_info(AC-Authorization-ARM, owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_getOverview_with_http_info(AC-Authorization-ARM, owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def data_getOverview_with_http_info(self, AC-Authorization-ARM, owner_name, app_name, **kwargs):  # noqa: E501
        """  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_getOverview_with_http_info(AC-Authorization-ARM, owner_name, app_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param string AC-Authorization-ARM: ARM token (required)
        :param string owner_name: The name of the owner (required)
        :param string app_name: The name of the application (required)
        :return: ErrorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['AC-Authorization-ARM', 'owner_name', 'app_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_getOverview" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'AC-Authorization-ARM' is set
        if ('AC-Authorization-ARM' not in params or
                params['AC-Authorization-ARM'] is None):
            raise ValueError("Missing the required parameter `AC-Authorization-ARM` when calling `data_getOverview`")  # noqa: E501
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `data_getOverview`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `data_getOverview`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'AC-Authorization-ARM' in params:
            header_params['AC-Authorization-ARM'] = params['AC-Authorization-ARM']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data', 'application/json-patch+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/data/overview', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ErrorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_checkNameExists(self, accountName, owner_name, app_name, **kwargs):  # noqa: E501
        """  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_checkNameExists(accountName, owner_name, app_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param string accountName: (required)
        :param string owner_name: The name of the owner (required)
        :param string app_name: The name of the application (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.data_checkNameExists_with_http_info(accountName, owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_checkNameExists_with_http_info(accountName, owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def data_checkNameExists_with_http_info(self, accountName, owner_name, app_name, **kwargs):  # noqa: E501
        """  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.data_checkNameExists_with_http_info(accountName, owner_name, app_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param string accountName: (required)
        :param string owner_name: The name of the owner (required)
        :param string app_name: The name of the application (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['accountName', 'owner_name', 'app_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_checkNameExists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'accountName' is set
        if ('accountName' not in params or
                params['accountName'] is None):
            raise ValueError("Missing the required parameter `accountName` when calling `data_checkNameExists`")  # noqa: E501
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `data_checkNameExists`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `data_checkNameExists`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'accountName' in params:
            path_params['accountName'] = params['accountName']  # noqa: E501
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/csv', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data', 'application/json-patch+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/data/database_account_names/{accountName}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def identity_getUsers(self, owner_name, app_name, **kwargs):  # noqa: E501
        """  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.identity_getUsers(owner_name, app_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param string owner_name: The name of the owner (required)
        :param string app_name: The name of the application (required)
        :param string AC-Authorization-AAD-Graph: MSGraph Auth Token(optional)
        :param string searchTerm: User search term(optional)
        :return: ErrorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.identity_getUsers_with_http_info(owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.identity_getUsers_with_http_info(owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def identity_getUsers_with_http_info(self, owner_name, app_name, **kwargs):  # noqa: E501
        """  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.identity_getUsers_with_http_info(owner_name, app_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param string owner_name: The name of the owner (required)
        :param string app_name: The name of the application (required)
        :param string AC-Authorization-AAD-Graph: MSGraph Auth Token(optional)
        :param string searchTerm: User search term(optional)
        :return: ErrorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_name', 'app_name', 'AC-Authorization-AAD-Graph', 'searchTerm']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method identity_getUsers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `identity_getUsers`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `identity_getUsers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []
        if 'searchTerm' in params:
            query_params.append(('searchTerm', params['searchTerm']))  # noqa: E501

        header_params = {}
        if 'AC-Authorization-AAD-Graph' in params:
            header_params['AC-Authorization-AAD-Graph'] = params['AC-Authorization-AAD-Graph']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'text/plain', 'text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data', 'application/json-patch+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/auth/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ErrorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
