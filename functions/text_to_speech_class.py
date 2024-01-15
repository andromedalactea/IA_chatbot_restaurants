import os
import html
from google.cloud import texttospeech

from functions.datafields import LanguageChosen , AudioConfig , VoiceGender

language_mapping = {2 : LanguageChosen.CHINESE.value , 
                    1 : LanguageChosen.ENGLISH.value,
                    0 : LanguageChosen.JAPANESE.value}
                    
# Set your service account creditional to an enviromental variable called GOOGLE_APPLICATION_CREDENTIALS
# IT'S IMPORTANT THAT THIS IS SET BECAUSE THE TEXTTOSPEECH CLIENT WILL AUTOMATICALLY LOOK AT THIS ENVIRONMENT VARIABLE
# IF NOT FOUND IT'LL THROW AN ERROR. THE CURRENT ONE IS USED MY ME. 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "preskriber-213919-da85fff92323.json"

class GoogleAPIClient:
    
    client = texttospeech.TextToSpeechClient()

    

    def __init__(self , 
                 ssml : str ,
                 language : LanguageChosen , 
                 autoconfig : AudioConfig = AudioConfig() , 
                 gender : VoiceGender = VoiceGender.MALE.value,
                 outfilename : str = None) -> None:
        self.ssml = ssml
        self.language = language
        self.gender_voice = gender
        self.auto_config = autoconfig
        self.outfile = outfilename

    
    def ssml_to_audio(self):
        """
        The function that translates the ssml to audio by using the Text to speech good API client
        """

        #Synthesis object
        synthesis_input = texttospeech.SynthesisInput(ssml=self.ssml)

        # Builds the voice request, selects the language code and gender of the voice
        voice = texttospeech.VoiceSelectionParams(
            language_code=self.language, ssml_gender=self.gender_voice,
        )

        # Selects the type of audio file to return
        audio_config = texttospeech.AudioConfig(
            audio_encoding=self.auto_config.autoEncoding,
            effects_profile_id = self.auto_config.effectsProfileID,
            pitch = self.auto_config.pitch , 
            speaking_rate = self.auto_config.speedRate,
        )

        # Performs the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Writes the synthetic audio to the output file.
        with open(self.outfile, "wb") as out:
            out.write(response.audio_content)
            print("Audio content written to file " + self.outfile)


class AudioGeneratorClass:
    """

        A class that synthesis text to speech by leveraging on the Google cloud Text to Speech API. 

        params: text - Text to be synthesised into speech
        params: language: - Passed as an integer. 0 denotes Japanese, 1 denotes, English, 2 denotes Chinese
        params: audioconfig: Audio configuration dataclass that has been set to a default values. Check
                            datafields.AudioConfig class for more reference
        params: voice_gender: Gender of the voice speech,
        params: outfilename: the filename with extensions or not. The extensions has to be in .wav

        methods:
        audio - creates an audion file that contains the sythensize speech. 
    
    """

    allowed_fileoutput_extensions = ["wav"]

    def __init__(self , 
                 text, 
                 language ,
                 autoconfig : AudioConfig = AudioConfig() , 
                 voice_gender : VoiceGender = VoiceGender.MALE.value,
                 outfilename : str = None) -> None:
        
        self._validate_text(text)
        self._validate_language(language)

        self._text = text
        self._language = self._convert_language(language)
        self.auto_config = autoconfig
        self.voice_gender = voice_gender
        self._ssl = self.text_to_ssml(self.text)

        if not outfilename:

            self._outfile = "output.wav" 
        else:
            self._validate_file_extension(outfilename)
            self._outfile = outfilename 



    def _validate_text(self , text):
        """
            Checks if the text isn't an integer
        """
        if not isinstance(text , str):
            raise Exception("Text must be an integer")
        
    def _validate_language(self , language):
        """
            Checks if the language is an integer
        """
        if not isinstance(language , int):
            raise Exception("Language must be an integer")
        
    
    def _convert_language(self , language):
        return language_mapping[language]
    
    @property
    def outfile(self):
        return self._outfile
    
    @outfile.setter
    def outfile(self , filename):
        """
        Sets the outfile name to whatever you want. 
        """
        if not isinstance(filename , str):
            raise Exception(f"Filename needs to be off the string type not {type(filename)}")
        
        if "." in filename:
            self._validate_file_extension(filename)
            self._outfile = filename
        else:
            self._outfile = filename + ".wav"

    def _validate_file_extension(self , filename):
        extension = filename.split(".")[1]

        if extension not in self.allowed_fileoutput_extensions:
            raise Exception(f"Filename extensions should only be amongst the filename allowed extensions not {extension} extensions")
        

    @property
    def language(self):
        if isinstance(self._language , int):
            return language_mapping[self._language]
        return self._language
    
    @language.setter
    def language(self , language : int):
        self._validate_language(language)
        self._language = self._convert_language(language)

    @property
    def ssl(self):
        if not hasattr(AudioGeneratorClass , "ssl"):
            self._ssl = self.text_to_ssml(self.text)
        return self._ssl
    
    @ssl.setter
    def ssl(self , ssl):
        if "<speak>" not in ssl:
            raise Exception("Text is not in an ssl format")
        
        self._ssl = ssl

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self , text):
        self._validate_text(text)
        self._text = text
        self.ssl = self.text_to_ssml(self._text)

        
    def text_to_ssml(self , text):

        # Replace special characters with HTML Ampersand Character Codes
        # These Codes prevent the API from confusing text with
        # SSML commands
        # For example, '<' --> '&lt;' and '&' --> '&amp;'

        escaped_lines = html.escape(text)

        # Convert plaintext to SSML
        # Wait two seconds between each address
        ssml = "<speak>{}</speak>".format(
            escaped_lines.replace("\n", '\n<break time="2s"/>')
        )

        # Return the concatenated string of ssml script
        return ssml

    
    
    def synthesize_speech(self):
        """
        Method returns an auto file. from the Google Speech API client
        """

        if not hasattr(AudioGeneratorClass , "ssl") or self.ssl is None:
            raise Exception("ssl needs to be an attribute or set in order to call the Text to Speech API")
        

        self._client = GoogleAPIClient(self.ssl , self.language, 
                                       autoconfig= self.auto_config,
                                       gender= self.voice_gender,
                                       outfilename= self.outfile
                                       )
        self._client.ssml_to_audio()

