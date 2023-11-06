import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('DataFrame')

st.write('Display Image')

img = Image.open('よくわからんが、まぁ動いているからヨシ！.png')
st.image(img, caption = '現場ねこ' , use_column_width=True)

#df = pd.DataFrame({
#    '1列目':[1, 2, 3, 4],
#    '2列目':[10, 20, 30, 40]
#})

# 出力可能だが、引数を与えることは出来ない
#st.dataframe(df.style.highlight_max(axis=0))

# パンダスの関数を利用。高さや幅の指定可能。axis=1にすると列の指定になる
#st.dataframe(df.style.highlight_max(axis=0), width = 500, height = 200)

# Static(静的)なテーブルができる（並び替えとかできない）
# st.table(df.style.highlight_max(axis=0))

'''
# 章

## 節

### 項
```Python
a = 10
b = 20
print(a + b)
```
'''

# ランダムで生成
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns = ['lat','lon']
)
# マップの表示
st.map(df)
#折れ線と中塗った折れ線
#st.line_chart(df)
#st.area_chart(df)