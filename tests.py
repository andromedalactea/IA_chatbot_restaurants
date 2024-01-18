from functions.text_to_speech_class import AudioGeneratorClass


audio_generator = AudioGeneratorClass(
        text = '''おっと、紋別町でおすし食べたいんだね！すし処 鮨元ってところがおすすめだもん。海鮮料理が自慢のいい感じのお店だもん。カウンター席もあって、デートや一人でも気軽に楽しめるもん。もう一つ、勘寿司もいいところだもん。小上がりや座敷があって、宴会や家族での食事にもピッタリだもん。どっちも飲食街の殆どの店舗がクレジットカード対応してるから、安心して使えるもんよ！
AI0> おっと、紋別町でおすし食べたいんだね！すし処 鮨元ってところがおすすめだもん。海鮮料理が自慢のいい感じのお店だもん。カウンター席もあって、デートや一人でも気軽に楽しめるもん。もう一つ、勘寿司もいいところだもん。小上がりや座敷があって、宴会や家族での食事にもピッタリだもん。どっちも飲食街の殆どの店舗がクレジットカード対応してるから、安心して使えるもんよ！''',  # Text to convert
        language = 1,  # Choose the language (0: Japanese, 1: English, 2: Chinese)
        outfilename = "answer_audio.wav"  # The name of the output file
    )


audio_generator.synthesize_speech()
