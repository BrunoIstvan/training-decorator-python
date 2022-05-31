from unittest import TestCase

from validate.run_validate_decorator import get_authorization, get_app, get_nested_fields_value


def generate_event(auth=None, app=None, update=None, field1=None):
    event = {
        'headers': {
            'Authorization': auth  # 'Bearer Token'
        },
        'queryStringParameters': {
            'app': app,  # None,
            'update': update  # None
        },
        'nested1': {
            'nested2': {
                'nested3': {
                    'field1': field1  # 'value field 1'
                }
            }
        }
    }
    return event


class TestValidateDecorator(TestCase):

    def test_get_authorization_success(self):
        expected = 'Bearer Token'
        event = generate_event(auth=expected)
        result = get_authorization(event)
        assert expected == result

    def test_get_authorization_exception(self):
        event = generate_event(auth='')
        with self.assertRaises(RuntimeError):
            get_authorization(event)

    def test_get_app_success(self):
        expected = 'app'
        event = generate_event(app=expected)
        result = get_app(event)
        assert expected == result

    def test_get_app_exception(self):
        event = generate_event(app='')
        with self.assertRaises(RuntimeError):
            get_app(event)

    def test_get_nested_fields_value_success(self):
        expected = 'value field1'
        event = generate_event(field1=expected)
        result = get_nested_fields_value(event)
        assert expected == result

    def test_get_nested_fields_value_empty_not_raises_exception(self):
        event = generate_event(field1=None)
        result = get_nested_fields_value(event)
        self.assertIsNone(result)
