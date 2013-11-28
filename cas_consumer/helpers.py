def get_callback_func(function):
    """
    This allows us to define callback functions `settings` module by specifying full path to the given method.

    :param mixed function: If `callable` is given, return as is. If `string` is given, try to
        extract the function from the string given and return.
    :return callable: Returns `callable` if what's extracted is callable or None otherwise.
    """
    if callable(function):
        return function
    elif isinstance(function, str):
        path = function.split('.')
        try:
            exec('from %s import %s as %s' % ('.'.join(path[0:-1]), path[-1], 'func'))
            if callable(func):
                return func
        except:
            return None
