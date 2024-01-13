import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import (ChatPromptTemplate, MessagesPlaceholder,
                               SystemMessagePromptTemplate, HumanMessagePromptTemplate)
from functions.function1 import stop_watch
from functions.function5 import system_prompt

# Set the OpenAI API key from environment variables
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Read the credentiasl from provided file !CHANGE THIS!
# Path to credentials
credentials_file = 'functions/env.txt'

# Read credentials
with open(credentials_file, 'r') as file:
    for line in file:
        key, value = line.partition("=")[::2]
        os.environ[key.strip()] = value.strip()

secret_key = os.environ["OPENAI_API_KEY"]

class AnsBotClass():
    def __init__(self, language_type, model_name="gpt-4-1106-preview"):
        """
        Initializes the AnsBotClass with specified language and model.

        Args:
            language_type (str): The language type for the bot (e.g., 'en' for English).
            model_name (str): The name of the GPT model to use.
        """
        # Initialize the stopwatch for testing and performance measurement
        self.stop_watch = stop_watch()

        # Generate the system prompt based on the specified language
        if language_type == 'zh-cn':
            template = system_prompt('中国語', '请用中文。', '中国語以外は使わないでください。')
        elif language_type == 'en':
            template = system_prompt('英語', '', '英語以外は使わないでください。')
        else:
            template = system_prompt('', '', '')

        # Initialize the ChatOpenAI model
        llm = ChatOpenAI(model_name=model_name, openai_api_key=secret_key, temperature=0.8)

        # Set up the conversation memory with a window of the last 5 messages
        memory = ConversationBufferWindowMemory(k=5, return_messages=True)

        # Configure the chat prompt template
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(template),
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate.from_template("{input}")
        ])

        # Create the conversation chain with memory, prompt, and language model
        self.chain = ConversationChain(memory=memory, prompt=prompt, llm=llm)

    def response(self, input):
        """
        Generates a response to the given input using the conversation chain.

        Args:
            input (str): The input text to which the bot should respond.

        Returns:
            str: The generated response from the bot.
        """
        # Start the stopwatch
        self.stop_watch.start()

        # Generate the response using the conversation chain
        ret = self.chain.predict(input=input)

        # Stop the stopwatch and log the AI message
        self.stop_watch.end_start(ret, 'AI_msg=')

        return ret


