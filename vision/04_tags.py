# Step 4: Get Image Tags
# Learn: AI automatically tags what it sees

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
    visual_features=[VisualFeatures.TAGS]
)

print("Tags found:")
for tag in result.tags.list:
    print(f"  {tag.name} - {tag.confidence:.2f}")