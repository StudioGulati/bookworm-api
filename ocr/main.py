import base64

import flask
import functions_framework
from google.cloud import vision


@functions_framework.http
def ocr(request):
    client_options = {'api_endpoint': 'eu-vision.googleapis.com'}
    client = vision.ImageAnnotatorClient(client_options=client_options)

    content = base64.b64decode(request.data)
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    if response.error.message:
        print('{}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors'.format(
            response.error.message))
        return flask.Response(status=500)

    data = {}
    texts = response.text_annotations
    if len(texts) > 0:
        data['locale'] = texts[0].locale
        data['description'] = texts[0].description

    return flask.jsonify(data)
