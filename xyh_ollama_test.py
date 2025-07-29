import requests, base64

# 图片转Base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# 请求参数
image_base64 = image_to_base64(r"J:\LLM-TT\多模态测试\屏幕截图 2025-07-29 164644.jpg")
payload = {
    "model": "qwen2.5vl:7b",
    "prompt": "描述图片内容并指出主要物体",
    "stream": False,
    "images": [image_base64]
}

# 发送请求
response = requests.post(
    "http://localhost:11434/api/generate",
    json=payload
)
print(response.json()["response"])