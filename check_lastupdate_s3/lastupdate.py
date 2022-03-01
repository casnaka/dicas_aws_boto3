from importlib.resources import contents
import boto3

s3 = boto3.client('s3')
bucket_name = 'bucket_name'
remote_path = 'folder_name/other_folder_name/'

paginator = s3.get_paginator('list_objects_v2')
page_interator = paginator.paginate(Bucket=bucket_name, Prefix= remote_path, StartAfter= remote_path)

for page in page_interator:
    ContentsList = page['Contents']
    for contents in ContentsList:
        print(contents['LastModified']) #Data da ultima vez que o(s) arquivo(s) foi/foram modificado(s)
        print(contents['Keys']) #Nome(s) do(s) arquivo(s)