import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()

bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ココは右カラム')

expander1 = st.expander('問い合わせ１')
expander1.write('回答１')
expander2 = st.expander('問い合わせ２')
expander2.write('回答２')
expander3 = st.expander('問い合わせ３')
expander3.write('回答３')