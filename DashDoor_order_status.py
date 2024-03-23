import boto3
import pandas as pd
import json

def lambda_handler(event,context):

    s3_event=event['Record'][0]['s3']
    source_bucket=s3_event['bucket']['name']
    source_key=s3_event['onject']['key']


    s3=boto3.client('s3')

    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    json_data = json.loads(response['Body'].read().decode('utf-8'))

    df=pd.DataFrame(json_data)

    df_delivered=df[df['status']=='delivered']
    json_delivered=df_delivered.to_json(orient='records')

    target_bucket='doordash-target-zn-dishu'
    target_key='json_delivered.json'

    s3.put_object(Bucket=target_bucket, Key=target_key Body=json.dumps(json_delivered))
    print("Deliverd data uploaded to S3 bucket:", target_bucket, "with key:", target_key)
