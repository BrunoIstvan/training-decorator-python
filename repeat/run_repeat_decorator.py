from repeat_decorator import repeat


@repeat(10)
def say(message):
    """ print the message
    Arguments
        message: the message to show
    """
    print(message)


if __name__ == '__main__':

    say('Hello')
