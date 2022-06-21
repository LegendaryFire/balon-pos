from django.template.loader_tags import register


@register.simple_tag
def message_to_notyf(value, x, y):
    """
    Converts message tags into a Notyf friendly notification.
    :param value: The message.
    :param x: The x position (left, center or right).
    :param y: The y position (top, center or bottom).
    :return: Returns the appropriate Notyf notification.
    """
    data = {}
    match value.tags:
        case 'success':
            data['type'] = 'success'
        case 'warning':
            data['type'] = 'warning'
        case 'error':
            data['type'] = 'error'
        case _:
            data['type'] = 'default'

    data['message'] = value.message

    data['position'] = {
        'x': x,
        'y': y,
    }

    return f'<script>window.notyf.open({str(data)})</script>'


