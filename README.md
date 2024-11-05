# WordCloud

群词云功能

## 设计思路

- 使用 `jieba` 库进行分词，并使用 `wordcloud` 库生成词云
- 使用 `sqlite3` 库进行数据存储

## 主要函数

- `handle_WordCloud_group_message`：处理群消息
- `init_db`：初始化数据库
- `load_function_status`：加载功能开关状态
- `save_function_status`：保存功能开关状态
- `add_wordcloud_data`：增加词云数据
- `generate_wordcloud`：生成词云


## 更新日志

### 2024-11-05

- feat: 新增群词云功能
- feat: 新增词云定时任务
- fix: 修复定时任务词云图片绘制失败的问题
