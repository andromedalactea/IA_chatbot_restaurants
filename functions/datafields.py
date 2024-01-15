from dataclasses import dataclass , field
from enum import Enum

from google.cloud import texttospeech


class VoiceGender(Enum):
    MALE = texttospeech.SsmlVoiceGender.MALE
    FEMALE = texttospeech.SsmlVoiceGender.FEMALE

class AutoEncodingPlayer(Enum):
    MP3 = texttospeech.AudioEncoding.MP3
    LINEAR16 = texttospeech.AudioEncoding.LINEAR16

class LanguageChosen(Enum):
    CHINESE = "cmn-CN"
    ENGLISH = "en-US"
    JAPANESE = "ja-JP"


@dataclass
class AudioConfig:
    effectsProfileID : list = field(default_factory= lambda : [
                        "small-bluetooth-speaker-class-device"
                    ])
    autoEncoding : AutoEncodingPlayer = AutoEncodingPlayer.LINEAR16.value
    pitch : int = 0
    speedRate : float = 1.0
    