'''Escreva um programa que use a API da OpenAI para obter uma resposta do modelo ChatGP'''
import openai

def get_openai_response(api_key, prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

api_key = input("Digite sua chave de API da OpenAI: ")
prompt = input("Digite sua consulta para o modelo ChatGPT: ")
response = get_openai_response(api_key, prompt)
print("Resposta do modelo ChatGPT:")
print(response)

'''Escreva um programa que utiliza a Google Cloud Vision API para analisar uma imagem e reconhecer objeto'''
from google.cloud import vision
import io

def detect_objects(image_path):
    # Create a client
    client = vision.ImageAnnotatorClient()

    # Load the image
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform object detection
    response = client.object_localization(image=image)
    localized_object_annotations = response.localized_object_annotations

    # Print the results
    print('Objetos detectados:')
    for obj in localized_object_annotations:
        print(f'\n{obj.name} (confiança: {obj.score})')
        print('Vértices do polígono delimitador:')
        for vertex in obj.bounding_poly.normalized_vertices:
            print(f' - ({vertex.x}, {vertex.y})')

    if response.error.message:
        raise Exception(f'{response.error.message}')


image_path = 'path_to_your_image.jpg'
detect_objects(image_path)