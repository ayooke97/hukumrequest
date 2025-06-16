from alibabacloud_bailian20231229.client import Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_bailian20231229.models import CreateIndexRequest
from alibabacloud_tea_util import models as util_models
import os

# Configure authentication
config = open_api_models.Config(
    access_key_id=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    access_key_secret=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
    endpoint='bailian.ap-southeast-1.aliyuncs.com'  # e.g., 'bailian.cn-shanghai.aliyuncs.com'
)

# Create client
client = Client(config)

# Create index request
create_index_request = CreateIndexRequest()
# Set required parameters
create_index_request.name = "test_index"
create_index_request.description = "My test index"
create_index_request.structure_type = "unstructured"  # Required parameter according to error message
create_index_request.sink_type = "BUILT_IN"  # Required parameter according to new error message
# Additional parameters
create_index_request.type = "VECTOR"  # Common index types: VECTOR, BM25, etc.
# Vector configuration is often required for vector indexes
create_index_request.vector_config = {
    "dimension": 1536,  # Common dimension for embeddings
    "metric_type": "COSINE"  # Similarity metric (COSINE, EUCLIDEAN, etc.)
}
# If you have document IDs to include
# create_index_request.document_ids = ["doc-123", "doc-456"]

# Make the request
# For Alibaba Cloud SDK, the method signature requires a request parameter
# response = client.create_index(workspace_id=os.getenv('ALIBABA_CLOUD_WORKSPACE_ID'), request=create_index_request)
response = client.create_index_with_options(workspace_id=os.getenv('ALIBABA_CLOUD_WORKSPACE_ID'), tmp_req=create_index_request, headers={}, runtime=util_models.RuntimeOptions())
# Process the response
print(response.body)