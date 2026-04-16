# Just 8 lines!
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["VISION_ENDPOINT"]
key = os.environ["VISION_KEY"]
client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

print("✅ Connected!")