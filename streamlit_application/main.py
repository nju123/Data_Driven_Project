import streamlit as st
import pandas as pd
from fetch_data import *
from data_preprocess import *
from data_visualization import *

def show_data():
    st.session_state['show_data'] = True


if __name__ == '__main__':
    st.header("大选舆情检测系统")


    if 'show_data' not in st.session_state:
        st.session_state['show_data'] = False

    if st.button("开始监测", on_click=show_data):
        pass

    if st.session_state['show_data']:
        # 使用fetch_data：csv文件以自动保存为：'current_data.csv'中
        # fetch_data()

        # 已经自动进行了一系列文本清洗预处理，将current_data.csv中的文件保存到了df中
        df_current = data_preprocessing()

        # 展示爬取的数据
        st.markdown("""
        ### 所得数据表
        """)
        st.write(df_current)

        st.markdown("""
        ### 情感倾向展示
        """)

        show_all_charts(df_current)