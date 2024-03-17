import boto3
import json
s3=boto3.client('s3')

def lambda_handler(event,context):
    #storeing bucket name where we have file and unique key from the event 
    bucket=event['Records'][0]['s3']['bucket']['name']
    key=event['Records'][0]['s3']['object']['key']

    response= s3.head_object(Bucket=bucket, Key=key)
    file_size= response['ContentLength'] #size in bytes

    file_size_mb= file_size/(1024*1024)

    if file_size_mb >100:
        print('File is greater than 100 MB !')
    else:
        print('File is with in limit of 100 MB !')
        
    return {
        'statusCode': 200,
        'body': json.dumps('Testing completed, Good Bye !!')
    }
    
    
