import csv
import boto3
from datetime import datetime
from botocore.exceptions import NoCredentialsError

bucket_name = 'price-lake'
file_name = 'dinner-cruise' + "-" + datetime.now().strftime("%Y-%m-%d-%H")
directory_output = "/Users/sarojdongol/Desktop/webscrapper/"
upload_data = directory_output + file_name + ".csv"


"""Creating s3 client to upload data"""
sts_client = boto3.client('sts')
role_to_assume_arn = 'arn:aws:iam::796852360460:role/s3uploader'
role_session_name = 'crawler-uploader'

response = sts_client.assume_role(RoleArn=role_to_assume_arn,RoleSessionName=role_session_name)

creds = response['Credentials']

s3_resource = boto3.client('s3',
                                aws_access_key_id=creds['AccessKeyId'],
                                aws_secret_access_key=creds['SecretAccessKey'],
                                aws_session_token=creds['SessionToken'],
                                )


def CsvWriter(product_id, description, full_price, actual_price, other_price, save_price):
        with open(file_name + ".csv", mode='a') as daily_price_file:
            pricewriter = csv.writer(daily_price_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            pricewriter.writerow([product_id, description, full_price, actual_price, other_price, save_price])


def S3_Uploader():
    print("uploading files...")
    response = s3_resource.upload_file(upload_data, "avro-data", file_name + ".csv" )
    print(response)
    





