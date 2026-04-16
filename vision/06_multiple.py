# Step 8: Multiple Features Together
# Learn: Get caption, tags, and objects in one call

import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["VISION_ENDPOINT"]
key = os.environ["VISION_KEY"]
client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg"
image_path = "image.jpeg"

with open(image_path, "rb") as f:
    image_data = f.read()

result = client.analyze(
    image_data=image_data,
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS, VisualFeatures.OBJECTS]
)

print(f"Caption: {result.caption.text}")
print(f"Tags: {', '.join([tag.name for tag in result.tags.list[:5]])}")
print(f"Objects: {len(result.objects.list)} found")