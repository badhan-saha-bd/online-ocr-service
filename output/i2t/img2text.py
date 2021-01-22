def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    import os
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\User\Desktop\cse470\output\i2t\key.json'
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.full_text_annotation

    var = texts.text
    return var
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
#print(detect_text('images/2.PNG'))
