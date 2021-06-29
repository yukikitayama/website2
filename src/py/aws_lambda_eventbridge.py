from datetime import datetime


def lambda_handler(event, context):
    """
    This Lambda just returns a string of UTC current time 
    in a format like 2021-06-28 22:30:01. You can check the
    output in the log of AWS CloudWatch. If EventBridge
    triggers this Lambda every hour, you can see the Lambda 
    output changes every hour by adding 1 hour.
    """
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')