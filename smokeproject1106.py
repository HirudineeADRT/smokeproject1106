import boto3
s3 = boto3.client("s3")
ddb = boto3.client("dynamodb")

def handler(request):
    
    try:
        data = s3.list_objects(
            Bucket="btbucket.images",
            MaxKeys=10
        )
        print(data)
    except BaseException as e:
        print(e)
        raise(e)

    
    return "Successfully executed"
