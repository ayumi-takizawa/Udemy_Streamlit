import os
from google.cloud import texttospeech

import io
import streamlit as st

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'

def synthesize_talk(talk_text, lang='日本語', type='ニュートラル'):
    g_type = v_type = type
    
    lang_code = {
        '英語' : 'en-US',
        '日本語' : 'ja-JP'
    }
    
    gender_type = {
        '男性' : texttospeech.SsmlVoiceGender.MALE,
        '女性' : texttospeech.SsmlVoiceGender.FEMALE,
        'ニュートラル' : texttospeech.SsmlVoiceGender.NEUTRAL
    }
    
    if lang == '日本語':
        voice_type = {
            '男性' : "ja-JP-Neural2-C",
            '女性' : "ja-JP-Neural2-B",
            'ニュートラル' : ""
        }
    else:
        voice_type = {
            '男性' : "en-US-Neural2-J",
            '女性' : "en-US-Neural2-F",
            'ニュートラル' : ""
        }
    
    client = texttospeech.TextToSpeechClient()
    
    synthesis_input = texttospeech.SynthesisInput(text = talk_text)
    
    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code[lang],
        name=voice_type[v_type],
        ssml_gender=gender_type[g_type]
    )
    
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice,
        audio_config=audio_config
    )
    return response

# Streamlit出力用
st.title('音声出力アプリ')

st.markdown('### データ準備')

input_option = st.selectbox(
    '入力データの選択',
    ('直接入力', 'テキストファイル')
)

input_data = None

if input_option == '直接入力':
    input_data = st.text_area('こちらにテキストを入力してください', 'Cloud Speech-to-Text用のサンプルになります。')
else:
    uploaded_file = st.file_uploader('テキストファイルをアップロードしてください', ['txt'])
    if uploaded_file is not None:
        content = uploaded_file.read()
        input_data = content.decode()

if input_data is not None:
    st.markdown('入力データ')
    st.write(input_data)
    st.markdown('### パラメータ設定')
    st.subheader('言語と話者の性別選択')

    lang = st.selectbox(
        '言語を選択して下さい',
        ('日本語', '英語')
    )
    type = st.selectbox(
        '話者の性別を選択して下さい',
        ('男性', '女性', 'ニュートラル')
    )

    st.markdown('### 音声合成')
    st.write('こちらの文章で音声ファイルの生成を行いますか？')

    if st.button('開始'):
        comment = st.empty()
        comment.write('音声出力を開始します')
        response = synthesize_talk(input_data, lang, type)
        st.audio(response.audio_content)
        comment.write('完了しました')