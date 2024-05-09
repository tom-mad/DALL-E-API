import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

client = openai.OpenAI(
  api_key=config["OPENAI_API_KEY"],
)

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)
