import jieba
from wordcloud import WordCloud
import base64


# 提取消息中的文本
def extract_text_from_message(message):
    text = ""
    for item in message:
        print(f"{item}\n")
        if item.get("type") == "text":
            text += item.get("data", {}).get("text", "")
    return text


message = [
    {
        "type": "image",
        "data": {
            "summary": "",
            "file": "000001464e61704361744f6e65426f747c4d736746696c657c327c3732383037373038377c373433333735373436343430373232373336387c373433333735373436343430373232373336347c4568536652544b62786e70594532474a704863716334366d7364766a4e78695833796f675f776f6f3671713835597a4669514d794248427962325251674c326a41566f51312d776955796c4c774d6538346f7658706e37554b41.3C842840E3D44A53C8AAA1DDF2A1EFA2.jpg",
            "sub_type": 0,
            "file_id": "000001464e61704361744f6e65426f747c4d736746696c657c327c3732383037373038377c373433333735373436343430373232373336387c373433333735373436343430373232373336347c4568536652544b62786e70594532474a704863716334366d7364766a4e78695833796f675f776f6f3671713835597a4669514d794248427962325251674c326a41566f51312d776955796c4c774d6538346f7658706e37554b41.3C842840E3D44A53C8AAA1DDF2A1EFA2.jpg",
            "url": "https: //multimedia.nt.qq.com.cn/download?appid=1407&fileid=EhSfRTKbxnpYE2GJpHcqc46msdvjNxiX3yog_woo6qq85YzFiQMyBHByb2RQgL2jAVoQ1-wiUylLwMe84ovXpn7UKA&spec=0&rkey=CAMSKMa3OFokB_TlAn1p3mvU5wumOQU0O6qAEKgVuQ8nH3AGFjdsHHKKXlM",
            "file_size": "700311",
            "file_unique": "3c842840e3d44a53c8aaa1ddf2a1efa2",
        },
    },
    {"type": "text", "data": {"text": "文本测试"}},
    {"type": "at", "data": {"qq": "2769731875"}},
    {"type": "text", "data": {"text": " 文本测试2"}},
]
