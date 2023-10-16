from gradio_client import Client
import ast

HOST_URL = "https://4283-34-87-87-194.ngrok-free.app/"
client = Client(HOST_URL)

# string of dict for input
def submit(query):
    kwargs = dict(instruction_nochat=query)
    res = client.predict(str(dict(kwargs)), api_name='/submit_nochat_api')


    # string of dict for output
    response = ast.literal_eval(res)['response']
    return response
