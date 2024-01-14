from functions.function6 import AnsBotClass
from functions.function7 import  DBsearchClass
from functions.function8 import LangJudgeClass
from functions.function9 import ConnectorClass

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
    lang_detected = lang_judge(message) 

    # Initial answer
    answer = ''
    candidate_txt = DBsearch.get_info(message + ' ' + answer)
    # print(candidate_txt)
    # Object of the bot 
    ans_bot = AnsBotClass(language_type=lang_detected) # Initialized the object in a specific language

    # Answer of the bot
    answer = ans_bot.response('問合せ：'+ message + candidate_txt)

    # Transforming the response to an AudioFile
    # Here is the logic to transform the reponse to an audio in .wav format

    return connector.output(answer)


user_input = "Tell me some good restaurants in tokyo to eat sushi"
response = main_flux(user_input)
print(response)