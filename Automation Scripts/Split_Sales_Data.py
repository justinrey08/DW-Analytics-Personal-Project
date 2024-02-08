# from pyspark.sql import SparkSession

# spark = SparkSession.builder \
#         .appName('Sales Table') \
#         .getOrCreate()

import boto3
from cryptography.fernet import Fernet
import json

# Obtain Creds
with open("enccreds.json", "r") as json_file:
    data = json.load(json_file)
    enc_aws_access_key_id = data['aaki'].encode('ascii')
    enc_aws_secret_access_key = data['asaki'].encode('ascii')

# decrypt creds
key = b'vDBN24vpiFChWjZvIJX7kGDeL-NadR4GSNDjn1AltyM='
fernet = Fernet(key)

aaki_bytes_data = fernet.decrypt(enc_aws_access_key_id)
asak_bytes_data = fernet.decrypt(enc_aws_secret_access_key)
aws_access_key_id = aaki_bytes_data.decode('ascii')
aws_secret_access_key = asak_bytes_data.decode('ascii')

#print(aws_access_key_id)
#print(aws_secret_access_key)

# Declare necessary arguments for S3 bucket access
region = 'ap-east-1'
bucket_name = 'dw-analytics-personal-project'
file_key = 'dataset/201904 sales reciepts.csv'


# Create session
session = boto3.Session(aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=region)
s3 = session.client('s3')
# s3.download_file(bucket_name, file_key, 'Sales Data.csv')
# print('Download Successful')

# #spark.stop()