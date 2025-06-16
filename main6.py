import os
import hashlib
import requests
from alibabacloud_bailian20231229.client import Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_bailian20231229.models import ApplyFileUploadLeaseRequest, AddFileRequest
from alibabacloud_tea_util import models as util_models

# Configure authentication
config = open_api_models.Config(
    access_key_id=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    access_key_secret=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
    endpoint='bailian.ap-southeast-1.aliyuncs.com'  # e.g., 'bailian.cn-shanghai.aliyuncs.com'
)

# Sample code is for reference only. Do not use it directly in production environments
import hashlib
def calculate_md5(file_path):
    """Calculate the MD5 value of a document.

    Args:
        file_path (str): The path of the document.

    Returns:
        str: The MD5 value of the document.
    """
    with open(file_path, "rb") as f:
        file_content = f.read()
        return hashlib.md5(file_content).hexdigest(), len(file_content)


# Example usage
if __name__ == "__main__":
    # File to upload
    file_path = "./UU Nomor 20 Tahun 1961.pdf"
    file_name = os.path.basename(file_path)
    
    # Check if file exists
    if os.path.exists(file_path):
        # Calculate MD5 and file size
        md5_value, file_size = calculate_md5(file_path)
        print(f"File: {file_name}")
        print(f"MD5: {md5_value}")
        print(f"Size: {file_size} bytes")
        
        # Configuration
        config = open_api_models.Config(
            access_key_id=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
            access_key_secret=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
            endpoint='bailian.ap-southeast-1.aliyuncs.com'
        )
        
        # Create client
        client = Client(config)
        workspace_id = os.getenv('ALIBABA_CLOUD_WORKSPACE_ID')
        category_id = 'cate_fce502e512ee4bd48f3e991d00c97222_3227'  # Your category ID
        
        try:
            # Step 1: Apply for file upload lease
            print("\nStep 1: Applying for file upload lease...")
            lease_request = ApplyFileUploadLeaseRequest(
                file_name=file_name,
                md_5=md5_value,
                size_in_bytes=str(file_size)
            )
            
            lease_response = client.apply_file_upload_lease(workspace_id=workspace_id, category_id=category_id, request=lease_request)
            
            if lease_response.body.success:
                # Get the lease ID and upload information
                lease_id = lease_response.body.data.file_upload_lease_id
                upload_url = lease_response.body.data.param.url
                upload_method = lease_response.body.data.param.method
                upload_headers = lease_response.body.data.param.headers
                
                print(f"Lease ID: {lease_id}")
                print(f"Upload URL: {upload_url}")
                
                # Step 2: Upload the file
                print("\nStep 2: Uploading file...")
                with open(file_path, 'rb') as f:
                    file_content = f.read()
                    
                    if upload_method.upper() == 'PUT':
                        upload_response = requests.put(upload_url, data=file_content, headers=upload_headers)
                    else:  # POST
                        upload_response = requests.post(upload_url, data=file_content, headers=upload_headers)
                
                print(f"Upload status: {upload_response.status_code}")
                
                if upload_response.status_code in [200, 201, 202, 204]:
                    # Step 3: Add the file to Bailian
                    print("\nStep 3: Adding file to Bailian...")
                    add_file_request = AddFileRequest(
                        lease_id=lease_id,
                        category_id=category_id,
                        parser='DASHSCOPE_DOCMIND'
                    )
                    
                    add_response = client.add_file(workspace_id, add_file_request)
                    print("Add file response:")
                    print(add_response.body)
                else:
                    print(f"File upload failed: {upload_response.text}")
            else:
                print(f"Failed to get lease: {lease_response.body}")
                
        except Exception as e:
            print(f"Error: {str(e)}")
    else:
        print(f"File not found: {file_path}")
