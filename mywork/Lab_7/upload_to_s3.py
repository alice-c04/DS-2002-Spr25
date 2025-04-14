import boto3
import urllib.request

s3 = boto3.client('s3', region_name='us-east-1')

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Sea_Otter_%28Enhydra_lutris%29_%2825169790524%29_crop.jpg/500px-Sea_Otter_%28Enhydra_lutris%29_%2825169790524%29_crop.jpg'
filename = 'otter.jpg'
urllib.request.urlretrieve(url, filename)


bucket = 'ds2002-kjq7ku' 
s3.put_object(
    Bucket=bucket,
    Key=filename,
    Body=open(filename, 'rb'),
    ACL='public-read'
)

url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': filename},
    ExpiresIn=3600
)

print("Presigned URL (works for 1 hour):")
print(url)

