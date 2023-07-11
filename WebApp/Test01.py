import numpy as np
import pandas as pd
import streamlit as st

st.title('測試首頁')
st.write('owq')

st.write('-----------------------------\n')
st.write('核取方塊')
cb=st.checkbox('是否?')
if cb:
    st.info('是')

st.write('-----------------------------------\n')
st.write('選項按鈕')
gender = st.radio('性別:',('M','F','N'))
st.write(gender)
st.success(gender)

st.write('-----------------------\n')
st.write('下拉選單')
option = st.selectbox('最喜歡的水果:',['apple','pineapple','banana'])
st.success(option) #方法一
'你的答案:',option #方法二

# st.write('-------------\n')
# st.write('進度條')
# import time
# aa=st.empty()
# bar = st.progress(0)
# for i in range(100):
#     aa.text(f'目前進度:{i+1}%')
#     bar.progress(i+1)
#     time.sleep(0.1)

st.write('-------------\n')
def AA():
    st.text("function")
st.write('按鈕')
btn=st.button('確定')
if btn:
    st.info('已確認')
    AA()

st.write('-------------\n')
st.write('滑桿')
num=st.slider('請選擇數項:',1,20)
'num=',num
st.info(num)

st.write('-------------\n')
st.write('檔案上傳')
loader = st.file_uploader('請選擇csv檔:')
if loader is not None:
  df2 = pd.read_csv(loader,header=None)
  st.dataframe(df2)
  st.table(df2.iloc[:2])

st.write('-------------\n')
st.write('隱藏欄位(文字)')
hidden = st.expander('按下後展開')
hidden.write('sasfas')

st.write('-------------\n')
st.write('圖片上傳+展示')
img = st.file_uploader('請選擇圖檔:',type=['png','jpg','jpeg'] )
if img is not None:
    st.image(img)


st.sidebar.write('側邊欄')
side01=st.sidebar.button('click me')
side02=st.sidebar.checkbox('ok?')     


st.write('-------------\n')
st.write('分欄')
left,right = st.columns(2)
left.write('AAAAA')
right.write('BBBBBBBBB')