from flask import make_response, jsonify

#TODO: Understand and create error codes - assign to endpoints 
SUCCESS_200 = {
    'http_code': 200,
    'code': 'success'
}

SUCCESS_201 = {
    'http_code': 201,
    'code': 'success'
}

ERROR_400 = {
    'http_code': 400,
    'code': 'error'
}



def response_with(response, value=None, message=None, error=None, headers={}, pagination=None):
    result = {}
    #TODO: Externalize into JSON serializer
    if value is not None:
        if type(value) is dict:
            value = {key:val.__json__() for (key,val) in value.items() if callable(val.__tojson__)}
        elif type(value) is list:
            value = [val.__json__() for val in value if callable(val.__json__) ]
        elif callable(value.__json__):
            value = value.__json__()
        result.update({"value": value})

    if response.get('message', None) is not None:
        result.update({'message': response['message']})

    result.update({'code': response['code']})

    if error is not None:
        result.update({'errors': error})

    if pagination is not None:
        result.update({'pagination': pagination})

    headers.update({'Access-Control-Allow-Origin': '*'})
    headers.update({'server': 'Flask REST API'})

    return make_response(jsonify(result), response['http_code'], headers)