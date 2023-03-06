import json
import boto3


def lambda_handler(event, context):

  method = event['context']['http-method']

  if method == 'GET':
      dynamo_client = boto3.client('dynamodb')
      im_customerID = event['params']['querystring']['CustomerID']
      response = dynamo_client.get_item(TableName='Customers', Key={'CustomerID':{'N': im_customerID}})

      return {
          'statusCode': 200,
          'body': json.dumps(response['Item'])
      }

  elif method == 'POST':
      record = event['body-json']
      record_string = json.dumps(record)

      kinesis_client = boto3.client('kinesis')
      response = kinesis_client.put_record(
          StreamName='APIData',
          Data=record_string,
          PartitionKey='string'
      )

      return {
          'statusCode': 200,
          'body': json.dumps(record)
      }

  else:
      return {
          'statusCode': 501,
          'body': json.dumps('Server Error')
      }
