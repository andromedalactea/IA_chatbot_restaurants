from functions.function6 import AnsBotClass
from functions.function7 import  DBsearchClass
from functions.function8 import LangJudgeClass
from functions.function9 import ConnectorClass
from functions.text_to_speech_class import AudioGeneratorClass


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
    print(lang_detected)
    ans_bot = AnsBotClass(lang_detected) # Initialized the object in a specific language

    # Answer of the bot
    answer = ans_bot.response( message + candidate_txt)

    # Transforming the response to an AudioFile
    # Create a class to convert audio
    audio_generator = AudioGeneratorClass(
        text = answer,  # Text to convert
        language = lang_detected,  # Choose the language (0: Japanese, 1: English, 2: Chinese)
        outfilename = "answer_audio.wav"  # The name of the output file
    )

    # Call the method to generate the audio
    audio_generator.synthesize_speech()

    print(answer)
    return connector.output(answer)


user_input = "給我推薦在紋別吃的東西"
response = main_flux(user_input)
print(response)