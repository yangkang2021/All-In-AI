import json
import base64

import requests


def submit_post(url: str, data: dict):
    """
    Submit a POST request to the given URL with the given data.
    """
    return requests.post(url, data=json.dumps(data))


def save_encoded_image(b64_image: str, output_path: str):
    """
    Save the given image to the given output path.
    """
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))


if __name__ == '__main__':
    txt2img_url = 'http://127.0.0.1:7860/sdapi/v1/txt2img'
    data = {'prompt': 'a dog wearing a hat'}
    response = submit_post(txt2img_url, data)
    print(response)
    save_encoded_image(response.json()['images'][0], 'dog.png')
