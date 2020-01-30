import boto3
import argparse
import logging
logging.basicConfig(level=logging.INFO)
BUCKET_NAME = "<S3 bucket name>"
session = boto3.Session(
    aws_access_key_id="<Update access keys>",
    aws_secret_access_key="<update secret keys>",
)
s3_resource = session.resource('s3')
my_bucket = s3_resource.Bucket(BUCKET_NAME)

def list_files_s3(my_bucket, file_type):
    """In this method we use boto3 to connect to aws s3 bucket and list all
    tar files present in s3 bucket
    Args:
      my_bucket: Name of s3 bucket
    Returns:
      list of tar files
    """
    logging.info("List files recursively s3 bucket")
    logging.info("Bucket Used : {}".format(BUCKET_NAME))
    logging.info("File type : {}".format(file_type))
    list_of_files_in_s3 = []
    for bucket in my_bucket.objects.all():
        list_of_files_in_s3.append(bucket.key)
    tar_video_list = [tar if tar.endswith('.tar.gz') else None for tar in list_of_files_in_s3]
    logging.info(tar_video_list)
    return tar_video_list





if __name__ == "__main__":
parser = argparse.ArgumentParser()
parser.add_argument('file_type',
	help ='file type eg- .py or .tar.gz',
	type = str)
args = parser.parse_args()	
list_files_s3(my_bucket,args.file_type)