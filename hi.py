import openai
from dotenv.main import load_dotenv
import os
load_dotenv()
favorite_language = os.environ['key']
print(favorite_language)

# response = openai.Completion.create(
#                 model = 'text-davinci-003' ,
#                 prompt= 'Give 10 lines information about karnataka' ,
#                 max_tokens = 300)
# print(response['choices'][0]['text'])