from langdetect import detect

def which_lang(txt, lang0):
    """
    Determines the language of the given text.
    
    Args:
        txt (str): The text whose language is to be determined.
        lang0 (str): The default language to consider if no specific cues are found in the text.

    Returns:
        str: The identified language code.
    """
    if lang0 != '':
        if '日本語で' in txt:
            lang = 'ja'
        elif '英語で' in txt or 'English' in txt:
            lang = 'en'
        elif '中国語で' in txt or '请用中文' in txt:
            lang = 'zh-cn'
        else:
            lang = lang0
    else:
        lang = detect(txt)
        if lang in ['zh-cn', 'ko']:
            lang = 'zh-cn'
        elif lang in ['en']:
            lang = 'en'
        else:
            lang = 'ja'
    return lang

class LangJudgeClass:
    """
    Class to judge and remember the language of texts.
    """
    def __init__(self):
        self.type_old = ''

    def __call__(self, usr_txt):
        # Import statements can be moved to the top if used elsewhere
        # from functions.function5 import which_lang
        from functions.function0 import bprint, fprint
        
        type_old = self.type_old
        language_type = which_lang(usr_txt, type_old)
        self.type_old = language_type
        
        if type_old == language_type:
            return ''  # Return an empty string if the language hasn't changed
        fprint('言語：', language_type)  # Print language type (comment in Japanese)
        return language_type

