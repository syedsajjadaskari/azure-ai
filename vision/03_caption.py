# Step 3: Get Image Caption (Description)
# Learn: How AI describes an image

import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["VISION_ENDPOINT"]
key = os.environ["VISION_KEY"]
client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg"

result = client.analyze_from_url(
    image_url=image_url,
    visual_features=[VisualFeatures.CAPTION]
)

print(f"Caption: {result.caption.text}")
print(f"Confidence: {result.caption.confidence}")