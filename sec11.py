import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactive Widgets')

# option = st.selectbox(
#     'あなたの好きな数字を教えてください。',
#     list(range(1,11))
# )
# 'あなたの好きな数字は' ,option, 'です'
# st.write('あなたの好きな数字は {} です'.format(option))


# hobby = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# st.write('あなたの趣味： {}'.format(hobby))
# 'コンディション：',condition

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ココは右カラム')

expander = st.expander('問い合わせ')
expander.write('お問い合わせ内容を書く')

hobby = st.text_input('あなたの趣味を教えてください。')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
st.write('あなたの趣味： {}'.format(hobby))
'コンディション：',condition


#     img = Image.open('よくわからんが、まぁ動いているからヨシ！.png')
#     st.image(img, caption = '現場ねこ' , use_column_width=True)

