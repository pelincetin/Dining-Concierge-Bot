import json
import boto3

def lambda_handler(event, context):
    intent_name = event['currentIntent']['name']
    #print(event)
    
    sqs = boto3.client('sqs', aws_access_key_id='', aws_secret_access_key='')
    queue_url = 'https://sqs.us-east-1.amazonaws.com/695601039191/Q1'
    
    location = event['currentIntent']['slots']['Location']
    cuisine = event['currentIntent']['slots']['Cuisine']
    dining_date = event['currentIntent']['slots']['DiningDate']
    dining_time = event['currentIntent']['slots']['DiningTime']
    num_people = event['currentIntent']['slots']['NumberPeople']
    phone_num = event['currentIntent']['slots']['PhoneNumber']
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Location': {
                'DataType': 'String',
                'StringValue': location
            },
            'Cuisine': {
                'DataType': 'String',
                'StringValue': cuisine
            },
            'DiningDate': {
                'DataType': 'String',
                'StringValue': dining_date
            },
            'DiningTime': {
                'DataType': 'String',
                'StringValue': dining_time
            },
            'NumberPeople': {
                'DataType': 'String',
                'StringValue': num_people
            },
            'PhoneNumber': {
                'DataType': 'String',
                'StringValue': phone_num
            }
        },
        MessageBody=(
            'You’re all set. Expect my suggestions shortly! Have a good day.'
        )
    )
    
    response = {
        "dialogAction":
            {
               "fulfillmentState":"Fulfilled",
               "type":"Close",
               "message":
                   {
                       "contentType":"PlainText",
                       "content": "I've received your request and " 
                       + "I'll notify you over text once I've generated the list of restaurant suggestions."
                       
                   }
           }
    }
    return response