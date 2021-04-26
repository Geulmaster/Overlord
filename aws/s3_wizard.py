import boto3

s3 = boto3.resource('s3')

def get_all_buckets():
    for bucket in s3.buckets.all():
        yield bucket.name


def get_objects_list():
    for obj in s3.Bucket('geul-public').objects.all():
        yield obj

# obj = s3.Bucket('geul-public').Object('access_logs.txt').get()
# print(obj)

#down = s3.Bucket('geul-public').download_file(Key='access_logs.txt', Filename='access_logs.txt')