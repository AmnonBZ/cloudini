import boto3
from .clientApply import *
from botocore.exceptions import ClientError
from .clientApply import *


def deleteme(resource_id, resource_type):
    if resource_type == "instance":
        client = resourceHandler("ec2", "us-east-1")
        client.instances.filter(InstanceIds=[resource_id]).terminate()

    if resource_type == "volume":
        client = resourceHandler("ec2", "us-east-1")
        client.delete_volume(VolumeId=resource_id)

def sms(resource_id, resource_type):
#'+972543070292','+972508725393'
    sns_client = clientHandler('sns', "us-east-1")
    response = sns_client.publish(
        PhoneNumber='+972543070292',
        Message='CLOSE YOUR AWS INSTANCES YOU KLUMNICK!!!!!!!!',
        # TopicArn='string', (Optional - can't be used with PhoneNumer)
        # TargetArn='string', (Optional - can't be used with PhoneNumer)
        # Subject='string', (Optional - not used with PhoneNumer)
        # MessageStructure='string' (Optional)
    )
    print(response)

def email(resource_id, resource_type):
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "<cs05@cs.colman.ac.il>"

    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = "yos709237@gmail.com"

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    #CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-1"

    # The subject line for the email.
    SUBJECT = "Amazon SES Test (SDK for Python)"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto)."
                 )

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Amazon SES Test (SDK for Python)</h1>
      <p>This email was sent with
        <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
        <a href='https://aws.amazon.com/sdk-for-python/'>
          AWS SDK for Python (Boto)</a>.</p>
    </body>
    </html>
                """

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = clientHandler('ses', AWS_REGION)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


    # sns_client = clientHandler('sns', "us-east-1")
    # topic_arn = "<my sns arn>"
    # msg = "blah"
    # sub = "tal"
    # response = sns_client.publish(
    #     TopicArn=topic_arn,
    #     Message=msg,
    #     Subject=sub,
    # )
    # print(response)