# Step 7: Analyze Your Own Local Image
# Learn: Use your own photos instead of URLs

import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["VISION_ENDPOINT"]
key = os.environ["VISION_KEY"]
client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Change this to your image path
image_path = "image.jpeg"

with open(image_path, "rb") as f:
    image_data = f.read()

result = client.analyze(
    image_data=image_data,
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS]
)

print(f"Caption: {result.caption.text}")
print("Top 3 tags:")
for tag in result.tags.list[:3]:
    print(f"  {tag.name}")