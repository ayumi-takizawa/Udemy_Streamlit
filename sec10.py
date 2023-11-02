import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

option = st.selectbox(
    'あなたの好きな数字を教えてください。',
    list(range(1,11))
)
'あなたの好きな数字は' ,option, 'です'
# st.write('あなたの好きな数字は {} です'.format(option))


text = st.text_input('あなたの趣味を教えてください。')
st.write('あなたの趣味： {}'.format(text))

#最大値、最小値、デフォルトの数値
text2 = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：',text2
#     img = Image.open('よくわからんが、まぁ動いているからヨシ！.png')
#     st.image(img, caption = '現場ねこ' , use_column_width=True)

