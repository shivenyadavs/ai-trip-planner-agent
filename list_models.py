from google import genai
import os

client = genai.Client(api_key="AIzaSyBo3vC6vOAeEbiesBf2yEeAkUfUJArvrVw")

models = client.models.list()

for model in models:
    print(model.name)
