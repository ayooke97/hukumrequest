# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys
import dotenv 
dotenv.load_dotenv()
from typing import List

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_credentials.client import Client as CredentialClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> OpenApiClient:
        """
        Initialize the Client with the credentials
        @return: Client
        @throws Exception
        """
        # It is recommended to use the default credential. For more credentials, please refer to: https://www.alibabacloud.com/help/en/alibaba-cloud-sdk-262060/latest/configure-credentials-378659.
        credential = CredentialClient()
        config = open_api_models.Config(
            credential=credential
        )
        # See https://api.alibabacloud.com/product/bailian.
        config.endpoint = f'bailian.ap-southeast-1.aliyuncs.com'
        return OpenApiClient(config)

    @staticmethod
    def create_api_info(
        category_id: str,
        workspace_id: str,
    ) -> open_api_models.Params:
        """
        API Info
        @param path: string Path parameters
        @return: OpenApi.Params
        """
        params = open_api_models.Params(
            # API Name,
            action='ApplyFileUploadLease',
            # API Version,
            version='2023-12-29',
            # Protocol,
            protocol='HTTPS',
            # HTTP Method,
            method='POST',
            auth_type='AK',
            style='ROA',
            # API PATH,
            pathname=f'/{workspace_id}/datacenter/category/{category_id}',
            # Request body content format,
            req_body_type='formData',
            # Response body content format,
            body_type='json'
        )
        return params

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        params = Sample.create_api_info('', '')
        # runtime options
        runtime = util_models.RuntimeOptions()
        request = open_api_models.OpenApiRequest()
        # Copy the code to run, please print the return value of the API by yourself.
        # The return value is of Map type, and three types of data can be obtained from Map: response body, response headers, HTTP status code.
        client.call_api(params, request, runtime)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        params = Sample.create_api_info('', '')
        # runtime options
        runtime = util_models.RuntimeOptions()
        request = open_api_models.OpenApiRequest()
        # Copy the code to run, please print the return value of the API by yourself.
        # The return value is of Map type, and three types of data can be obtained from Map: response body, response headers, HTTP status code.
        await client.call_api_async(params, request, runtime)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_credentials.client import Client as CredentialClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> OpenApiClient:
        """
        Initialize the Client with the credentials
        @return: Client
        @throws Exception
        """
        # It is recommended to use the default credential. For more credentials, please refer to: https://www.alibabacloud.com/help/en/alibaba-cloud-sdk-262060/latest/configure-credentials-378659.
        credential = CredentialClient()
        config = open_api_models.Config(
            credential=credential
        )
        # See https://api.alibabacloud.com/product/bailian.
        config.endpoint = f'bailian.ap-southeast-1.aliyuncs.com'
        return OpenApiClient(config)

    @staticmethod
    def create_api_info(
        category_id: str,
        workspace_id: str,
    ) -> open_api_models.Params:
        """
        API Info
        @param path: string Path parameters
        @return: OpenApi.Params
        """
        params = open_api_models.Params(
            # API Name,
            action='ApplyFileUploadLease',
            # API Version,
            version='2023-12-29',
            # Protocol,
            protocol='HTTPS',
            # HTTP Method,
            method='POST',
            auth_type='AK',
            style='ROA',
            # API PATH,
            pathname=f'/{workspace_id}/datacenter/category/{category_id}',
            # Request body content format,
            req_body_type='formData',
            # Response body content format,
            body_type='json'
        )
        return params

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        params = Sample.create_api_info(os.getenv('ALIBABA_CLOUD_CATEGORY_ID'), os.getenv('ALIBABA_CLOUD_WORKSPACE_ID'))
        # runtime options
        runtime = util_models.RuntimeOptions()
        request = open_api_models.OpenApiRequest(
            body=params
        )
        # Copy the code to run, please print the return value of the API by yourself.
        # The return value is of Map type, and three types of data can be obtained from Map: response body, response headers, HTTP status code.
        client.call_api(params, request, runtime)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        params = Sample.create_api_info(os.getenv('ALIBABA_CLOUD_CATEGORY_ID'), os.getenv('ALIBABA_CLOUD_WORKSPACE_ID'))
        # runtime options
        runtime = util_models.RuntimeOptions()
        request = open_api_models.OpenApiRequest()
        # Copy the code to run, please print the return value of the API by yourself.
        # The return value is of Map type, and three types of data can be obtained from Map: response body, response headers, HTTP status code.
        await client.call_api_async(params, request, runtime)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])