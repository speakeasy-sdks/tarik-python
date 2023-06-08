"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from lk import utils
from lk.models import operations, shared
from typing import Optional

class Order:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def order_schema_api_v1_orders_schema_get(self) -> operations.OrderSchemaAPIV1OrdersSchemaGetResponse:
        r"""Get JSON schema for order"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/v1/orders/schema'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.OrderSchemaAPIV1OrdersSchemaGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out
        elif http_res.status_code == 401:
            pass

        return res

    
    def order_validated_api_v1_orders_post(self, request: shared.Order, security: operations.OrderValidatedAPIV1OrdersPostSecurity) -> operations.OrderValidatedAPIV1OrdersPostResponse:
        r"""Add new order
        Checks if JSON has valid schema and adds request to create new order. No multiple orders will be created for the same **order_id**, even if request is accepted. Only first order request for **order_id** is created.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api/v1/orders'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.OrderValidatedAPIV1OrdersPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out
        elif http_res.status_code == 401:
            pass
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    