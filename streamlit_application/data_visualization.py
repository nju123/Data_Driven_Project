
import plotly.express as px
import streamlit as st
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from data_preprocess import *

# 基于文本内容画出词云
def draw_wordcloud(df,title,word_num,color):

    # 将清洗后的text合成一个长字符串
    text = "".join(text for text in df['filtered_text'])

    wordcloud = WordCloud(width=800, height=600,background_color='white',max_words=word_num,colormap=color).generate(text)

    # 使用Matplotlib显示生成的词云
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")  # 不显示坐标轴

    # 保存图像到文件系统
    image_path = f'{title}.png'
    plt.savefig(image_path, format='png', bbox_inches='tight', pad_inches=0)

    # 清除当前的Matplotlib图形
    plt.close()

    # 使用Streamlit显示图像
    st.image(image_path, caption='Word Cloud')

def draw_tweets_counts_by_time(df):

    # 按日期和关键词分组并计算每天每个关键词的推文数量
    tweet_counts_per_day_keyword = df.groupby([df['date'].dt.date, 'keyword']).size()

    # 重置索引，准备绘图
    tweet_counts_per_day_keyword = tweet_counts_per_day_keyword.reset_index()
    tweet_counts_per_day_keyword.columns = ['date', 'keyword', 'tweet_count']

    # 使用Plotly Express创建时间序列图
    fig = px.line(tweet_counts_per_day_keyword, x='date', y='tweet_count', color='keyword',
                  title='Daily Tweets Count by Keyword',
                  labels={'date': 'Date', 'tweet_count': 'Number of Tweets', 'keyword': 'Keyword'})

    # 使用Streamlit展示图表
    st.plotly_chart(fig)


def show_all_charts(df):

    df_trump = data_donald_trump(df)
    df_biden = data_joe_biden(df)

    # 词云图
    draw_wordcloud(df_trump,"Trump",50,'Reds')
    draw_wordcloud(df_biden,"Biden",50,'Blues')

    # 随时间数量的tweets图
    draw_tweets_counts_by_time(df)

