# coding: utf-8

"""
    ACES Listener API

    API Specification for ACES Listeners that read data on a blockchain and forward transaction events to registered subscribers.   # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from com.arkaces.aces_listener_api.api_client import ApiClient


class AcesListenerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def status_get(self, **kwargs):  # noqa: E501
        """Get Health of node.  # noqa: E501

        Get application health information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.status_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Health
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.status_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.status_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def status_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Health of node.  # noqa: E501

        Get application health information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.status_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Health
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method status_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Health',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscriptions_id_events_get(self, id, **kwargs):  # noqa: E501
        """List Subscription Events  # noqa: E501

        Gets a page of Subscription Events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subscriptions_id_events_get(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Subscription Identifier (required)
        :param int page_size: Number of items to return per page.
        :param int page: Zero-offset page number to return.
        :param str continuation: Continuation param for fetching next page.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.subscriptions_id_events_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.subscriptions_id_events_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def subscriptions_id_events_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Subscription Events  # noqa: E501

        Gets a page of Subscription Events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subscriptions_id_events_get_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Subscription Identifier (required)
        :param int page_size: Number of items to return per page.
        :param int page: Zero-offset page number to return.
        :param str continuation: Continuation param for fetching next page.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page_size', 'page', 'continuation']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscriptions_id_events_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `subscriptions_id_events_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'continuation' in params:
            query_params.append(('continuation', params['continuation']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/{id}/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscriptions_id_get(self, id, **kwargs):  # noqa: E501
        """Gets Subscription  # noqa: E501

        Get a Subscription by identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subscriptions_id_get(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Subscription Identifier (required)
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.subscriptions_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.subscriptions_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def subscriptions_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets Subscription  # noqa: E501

        Get a Subscription by identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subscriptions_id_get_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Subscription Identifier (required)
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscriptions_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `subscriptions_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscription',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscriptions_id_resubscribes_post(self, id, **kwargs):  # noqa: E501
        """Create a Resubscribe.  # noqa: E501

        Resubscribes an inactive subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subscriptions_id_resubscribes_post(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Subscription Identifier (required)
        :return: SubscriptionResubscribe
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.subscriptions_id_resubscribes_post_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.subscriptions_id_resubscribes_post_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def subscriptions_id_resubscribes_post_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create a Resubscribe.  # noqa: E501

        Resubscribes an inactive subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subscriptions_id_resubscribes_post_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Subscription Identifier (required)
        :return: SubscriptionResubscribe
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscriptions_id_resubscribes_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `subscriptions_id_resubscribes_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/{id}/resubscribes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubscriptionResubscribe',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscriptions_id_unsubscribes_post(self, id, **kwargs):  # noqa: E501
        """Create an Unsubscription.  # noqa: E501

        Unsubscribes an active Subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subscriptions_id_unsubscribes_post(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Subscription Identifier (required)
        :return: SubscriptionUnsubscribe
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.subscriptions_id_unsubscribes_post_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.subscriptions_id_unsubscribes_post_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def subscriptions_id_unsubscribes_post_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create an Unsubscription.  # noqa: E501

        Unsubscribes an active Subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subscriptions_id_unsubscribes_post_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: Subscription Identifier (required)
        :return: SubscriptionUnsubscribe
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscriptions_id_unsubscribes_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `subscriptions_id_unsubscribes_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/{id}/unsubscribes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubscriptionUnsubscribe',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def subscriptions_post(self, **kwargs):  # noqa: E501
        """Registers a subscriber node to receive blockchain events.  # noqa: E501

        The Subscribers endpoint allows subscriber to register their node to receive blockchain events from the Encoded Listener.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subscriptions_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param SubscriptionRequest subscription_request: The request to create a new Subscription.
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.subscriptions_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.subscriptions_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def subscriptions_post_with_http_info(self, **kwargs):  # noqa: E501
        """Registers a subscriber node to receive blockchain events.  # noqa: E501

        The Subscribers endpoint allows subscriber to register their node to receive blockchain events from the Encoded Listener.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subscriptions_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param SubscriptionRequest subscription_request: The request to create a new Subscription.
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscriptions_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subscription_request' in params:
            body_params = params['subscription_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscription',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
