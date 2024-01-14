from functions.function8 import LangJudgeClass
from functions.function6 import AnsBotClass
from functions.function9 import ConnectorClass
from functions.function7 import  DBsearchClass

# Simulation of a simple Connector Class

# Flux of the platform
def main_flux(message):

    # Searching in the database
    PKL_TOT='functions/tot_monbetsu31.pkl' 
    PKL_VEC='functions/vec_monbetsu31.pkl'
    
    DBsearch = DBsearchClass(PKL_TOT, PKL_VEC)
    # Creating the conection
    connector = ConnectorClass(message)
    
    # Detect the language Object
    lang_judge = LangJudgeClass()

    # Language detected
    lang_detected = lang_judge(connector.input()) 
    print('Llego hasta aqui')

    # Initial answer
    answer = ''
    candidate_txt = DBsearch.get_info(connector.input() + ' ' + answer)
    
    # Object of the bot 
    ans_bot = AnsBotClass(language_type=lang_detected) # Initialized the object in a specific language

    # Answer of the bot
    response = ans_bot.response('問合せ：'+ connector.input() + candidate_txt)

    # Transforming the response to an AudioFile
    # Here is the logic to transform the reponse to an audio in .wav format

    return connector.output(answer)


user_input = "東京で最高のレストランを教えてください"
response = main_flux(user_input)
print(response)