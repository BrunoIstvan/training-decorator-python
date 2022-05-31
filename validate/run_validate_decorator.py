from validate.validate_dict_decorator import validate


@validate('headers', 'Authorization', required=True)
def get_authorization(event):
    """ print the message
    Arguments
        message: the message to show
    """
    return event['headers']['Authorization']


@validate('queryStringParameters', 'app', required=True)
def get_app(event):
    """ print the message
    Arguments
        message: the message to show
    """
    return event['queryStringParameters']['app']


@validate('nested1', 'nested2', 'nested3', 'field1', required=False)
def get_nested_fields_value(event):
    """ print the message
    Arguments
        message: the message to show
    """
    return event['nested1']['nested2']['nested3']['field1']

