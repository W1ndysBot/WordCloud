from datetime import datetime
import os
import sqlite3
import logging
import jieba
from wordcloud import WordCloud
import base64

DATA_DIR = r"app\data\WordCloud"


# 获取数据库中的数据
def get_wordcloud_data(group_id):
    try:
        date_str = datetime.now().strftime("%Y_%m_%d")
        db_path = os.path.join(DATA_DIR, f"{date_str}_{group_id}.db")
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT word FROM wordcloud")
            return cursor.fetchall()
    except Exception as e:
        logging.error(f"获取词云数据失败: {e}")
        return []


# 绘制词云图片
def draw_wordcloud(group_id):
    try:
        data = get_wordcloud_data(group_id)

        # logging.info(f"词云数据: {data}")

        # 合并所有文本
        combined_text = " ".join(word_tuple[0] for word_tuple in data)

        logging.info(f"合并后文本: {combined_text}")

        # 使用jieba分词
        combined_text = " ".join(jieba.lcut(combined_text))

        logging.info(f"分词后文本: {combined_text}")

        # 生成词云
        wordcloud = WordCloud(
            # font_path="/usr/local/lib/python3.10/dist-packages/matplotlib/mpl-data/fonts/ttf/SIMHEI.TTF",
            font_path="SIMHEI.TTF",
            width=900,
            height=900,
            background_color="white",
        ).generate(combined_text)

        # 将词云图像保存到字节流
        from io import BytesIO

        image_stream = BytesIO()
        wordcloud.to_image().save(image_stream, format="PNG")
        image_stream.seek(0)

        # 将字节流转换为base64编码
        encoded_string = base64.b64encode(image_stream.read()).decode("utf-8")
        # logging.info(f"词云图像base64: {encoded_string}")
        encoded_string = f"base64://{encoded_string}"
        return encoded_string
    except Exception as e:
        logging.error(f"绘制词云失败: {e}")
        return ""


def test():
    today = datetime.now().strftime("%Y_%m_%d")
    for file in os.listdir(DATA_DIR):
        if file.startswith(today):
            group_id = file.split("_")[3].replace(".db", "")
            encoded_string = draw_wordcloud(group_id)
            message = f"叮咚~这是群{group_id}在{today}的词云图[CQ:image,file={encoded_string}]"
            print(message)


test()
