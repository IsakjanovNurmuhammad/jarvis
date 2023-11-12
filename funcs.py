import io
import openai
from pydub import AudioSegment
from pydub.playback import play

api_key = "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"  # Replace with your API key
openai.api_key = api_key

  # Replace with the full path to your audio files


def speech_to_text(speech):
    audio_file = open(speech, "rb")
    transcript = openai.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcript.text


def text_to_speech(text):
    response = openai.audio.speech.create(
        model="tts-1",
        voice="echo",
        input=text,
    )

    byte_stream = io.BytesIO(response.content)

    audio = AudioSegment.from_file(byte_stream, format="mp3")

    play(audio)


def text_generating(request):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "user", "content": request}
        ]
    )
    generated_text = response.choices[0].message.content
    return generated_text
