"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="こんにちは、私は滝澤です")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
# 英語：US / 日本語：ja-JP
voice = texttospeech.VoiceSelectionParams(
    language_code="ja-JP", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
# filename = "output.mp3"
# with open(filename, "wb") as out:
#     # Write the response to the output file.
#     out.write(response.audio_content)
#     print(f'音声データは{filename}ファイルに書き出しました')


from IPython.display import Audio
Audio(response.audio_content)