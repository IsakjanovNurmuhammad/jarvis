from speechs.voice_record import run_all
from funcs import speech_to_text, text_generating, text_to_speech

while True:
    voice_name = run_all()
    request = speech_to_text(voice_name)
    print(request)
    response = text_generating(request)
    print(response)
    text_to_speech(response)
