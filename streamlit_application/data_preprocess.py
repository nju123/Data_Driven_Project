import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


# 只保留英语文本
def clean_language(df):
    return df.query("language=='en'")

# 清洗链接
def clean_link(df):
    df.loc[:, 'text'] = df['text'].str.replace(r'http\S+|www.\S+', '', case=False, regex=True)
    return df

# 去除缺失值（text列）
def clean_delete_missing_data(df):
    df = df.dropna(subset=['text'])
    return df


# 去除文本停用词函数
def remove_stopwords(text):
    words = text.split()
    filtered_text = ' '.join([word for word in words if word not in stop_words])
    return filtered_text

# 应用到df中
def clean_remove_stopwords(df):
    df["filtered_text"] = df['text'].apply(remove_stopwords)
    return df


def data_preprocessing():
    df = pd.read_csv('current_data.csv')
    # 选择可能用到的列
    df = df[['id', 'author_id', 'follower_counts', 'text', 'date',
             'likes', 'views', 'retweet_counts', 'reply_counts', 'keyword', 'language']]
    df = clean_language(df)
    df = clean_link(df)
    df = clean_delete_missing_data(df)

    # 将文本转换为小写
    df['text'] = df['text'].str.lower()
    df = clean_remove_stopwords(df)

    # 将前两列转换为字符串型
    df['id'] = df['id'].astype(str)
    df['author_id'] = df['author_id'].astype(str)
    # 将date转换为时间类型
    df['date'] = pd.to_datetime(df['date'])
    return df


# 有必要将数据分开
def data_donald_trump(df):
    return df[df['keyword'] == 'Donald Trump']

def data_joe_biden(df):
    return df[df['keyword'] == 'Joe Biden']
