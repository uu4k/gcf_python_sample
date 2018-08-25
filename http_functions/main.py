def hello_http(request):
    request_json = request.get_json()
    if request_json and 'message' in request_json:
        name = request_json['message']
    else:
        name = 'World'
    return 'Hello, {}!'.format(name)