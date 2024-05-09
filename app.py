import os
import openai
import base64
import requests
from dotenv import dotenv_values

# First way
def save_image(url, image_name):
    image_directory_name = "images"
    image_directory = os.path.join(os.curdir, image_directory_name)

    if not os.path.isdir(image_directory):
      os.mkdir(image_directory)

    image_filepath = os.path.join(image_directory, image_name)
    image_content = requests.get(url).content
    with open(image_filepath, "wb") as image_file:
      image_file.write(image_content)

def get_image(openai_client, prompt, image_name):
  response = openai_client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
  )
  image_url = response.data[0].url
  save_image(image_url, image_name)


config = dotenv_values(".env")
client = openai.OpenAI(
  api_key=config["OPENAI_API_KEY"],
)


# get_image(client, "tic tac toe", "tic.png")


def get_and_save_image(openai_client, prompt, image_name):
  response = openai_client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    response_format="b64_json",
    n=1,
  )
  image_json = response.data[0].b64_json

  image_directory_name = "images"
  image_directory = os.path.join(os.curdir, image_directory_name)

  if not os.path.isdir(image_directory):
    os.mkdir(image_directory)

  image_filepath = os.path.join(image_directory, image_name)
  decoded_img = base64.b64decode(image_json)

  with open(image_filepath, "wb") as image_file:
    image_file.write(decoded_img)


# get_and_save_image(client, "playing chess", "chess.png")