from functools import wraps


def validate(*fields, required: bool):
    """ validate required fields before call function """
    def decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            struct = None
            for field in fields:
                if struct is None:
                    struct = dict(args[0])
                if field not in struct:
                    raise RuntimeError(f'{field} not found in {args}')
                struct = struct[field]
            result = fn(*args, **kwargs)
            if required and (result is None or result == ''):
                raise RuntimeError(f'{fields} has empty value in {args}')
            return result
        return wrapper
    return decorate
