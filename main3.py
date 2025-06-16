# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys
import dotenv
dotenv.load_dotenv()
from typing import List

from alibabacloud_bailian20231229.client import Client as BailianClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_bailian20231229 import models as bailian_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> BailianClient:
        """
        Initialize the Client with the credentials
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # Your AccessKey ID
            access_key_id=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
            # Your AccessKey Secret
            access_key_secret=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET')
        )
        # See https://api.alibabacloud.com/product/bailian.
        config.endpoint = f'bailian.ap-southeast-1.aliyuncs.com'
        return BailianClient(config)



    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        runtime = util_models.RuntimeOptions()
        
        # Create an AddFile request
        add_file_request = bailian_models.AddFileRequest(
            lease_id=os.getenv('ALIBABA_CLOUD_FILE_UPLOAD_LEASE_ID'),
            category_id=os.getenv('ALIBABA_CLOUD_CATEGORY_ID'),
            parser='DASHSCOPE_DOCMIND'
        )
        
        # Set the workspace ID
        workspace_id = os.getenv('ALIBABA_CLOUD_WORKSPACE_ID')
        
        try:
            # Make the API call using the correct method
            response = client.add_file_with_options(workspace_id, add_file_request, {}, runtime)
            # Print response
            print(f"File added successfully.")
            print(f"Response body: {response.body}")
            # Print response data structure to see available fields
            print(f"Response structure: {dir(response.body)}")
            # Try to access data if it exists
            if hasattr(response.body, 'data'):
                print(f"Data: {response.body.data}")
                if hasattr(response.body.data, 'file_id'):
                    print(f"File ID: {response.body.data.file_id}")
        except Exception as err:
            print(f"Error: {err}")
            if hasattr(err, 'data') and err.data:
                print(f"Error details: {err.data}")

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        runtime = util_models.RuntimeOptions()
        
        # Create an AddFile request
        add_file_request = bailian_models.AddFileRequest(
            lease_id=os.getenv('ALIBABA_CLOUD_FILE_UPLOAD_LEASE_ID'),
            category_id=os.getenv('ALIBABA_CLOUD_CATEGORY_ID'),
            parser='DASHSCOPE_DOCMIND'
        )
        
        # Set the workspace ID
        workspace_id = os.getenv('ALIBABA_CLOUD_WORKSPACE_ID')
        
        try:
            # Make the API call using the correct async method
            response = await client.add_file_with_options_async(workspace_id, add_file_request, {}, runtime)
            # Print response
            print(f"File added successfully.")
            print(f"Response body: {response.body}")
            # Print response data structure to see available fields
            print(f"Response structure: {dir(response.body)}")
            # Try to access data if it exists
            if hasattr(response.body, 'data'):
                print(f"Data: {response.body.data}")
                if hasattr(response.body.data, 'file_id'):
                    print(f"File ID: {response.body.data.file_id}")
        except Exception as err:
            print(f"Error: {err}")
            if hasattr(err, 'data') and err.data:
                print(f"Error details: {err.data}")


if __name__ == '__main__':
    Sample.main(sys.argv[1:])