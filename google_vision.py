# Usage: python GoogleAPI.py -i /home/images -o /home/GoogleRaw
# Outputs the GoogleAPI ocr into text files
# import the necessary packages
import io
import argparse
import os
import glob

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="vision_api.json"


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    transcripts = ""
    count = 0
    for text in texts:
        count = count + 1
        transcript= text.description
        transcripts = transcripts + transcript
        if count == 1:
            break
    return transcripts
print(detect_text('expiry_image.jpg'))
