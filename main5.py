import os

from Tea.exceptions import UnretryableException, TeaException
from alibabacloud_bailian20231229.models import CreateIndexRequest
from alibabacloud_bailian20231229.client import Client
from alibabacloud_tea_openapi.models import Config
import os

'''云服务器示例'''
# 初始化Config
config = Config(
    access_key_id=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'),
    access_key_secret=os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
    region_id=os.getenv('ALIBABA_CLOUD_REGION_ID')
)
client = Client(config)
# 初始化Requestq
request = CreateIndexRequest(image_id='<image-id>', region_id='<regionId>')
try:
    response = client.create_index(request)
except UnretryableException as e:
    # 网络异常
    print(e)
except TeaException as e:
    # 业务异常
    print(e)
except Exception as e:
    # 其他异常
    print(e)