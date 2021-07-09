#REST datan hakeminen
import requests
def sortFunction(value):
    return value["forks"]
response = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")
dataframe = response.json()
items_data = dataframe["items"]

with open('checkpoint.txt', 'w') as f:
    for i in items_data:
        f.write(i['parameter'])
        f.write('\n')

def bucket(bucket_name):
    from google.cloud import storage

    client = storage.Client()

    bucket1 = client.create_bucket(bucket_name)

    print(bucket1)
bucket("antti-super-bucket")

#upload a file to a bucket
from google.cloud import storage
storage_client = storage.Client()

def upload_to_bucket(blob_name, path_to_file, bucket_name):

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)#    blob.upload_from_filename(path_to_file)

    #returns a public url
    return blob.public_url



upload_to_bucket("checkpoint.txt", r"C:\Users\AnttiLecklin\VSCPython\Checkpoint3\vko3-1", "antti-super-bucket")


 