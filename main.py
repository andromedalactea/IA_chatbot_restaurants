from functions.function8 import LangJudgeClass
from functions.function6 import AnsBotClass
# Simulation of a simple Connector Class
class ConnectorClass:
    def __init__(self, user_message):

        self.user_message = user_message

    # The final 
    def return_messages(text_message, audio_message): pass
    '''
    Here you should put the logiuc to return the message to LINE adjust the parámeters
    '''

# Flux of the platform
def main_flux(message):
    
    # Message of the user
    Connector = ConnectorClass(message)

    # Detect the language Object
    lang_judge = LangJudgeClass()

    # Language detected
    lang_detected = lang_judge(Connector.user_message) 

    # Object of the bot 
    ans_bot = AnsBotClass(language_type=lang_detected) # Initialized the object in a specific language

    # Answer of the bot
    response = ans_bot.response(Connector.user_message)

    
    return response

ans_bot = AnsBotClass(language_type='en')
user_input = "How can I learn Python?"
response = ans_bot.response(user_input)
print(response)