from flask import Flask, render_template
import os

app = Flask(__name__)

# 获取静态图片列表（仅读取文件名，避免路径问题）
def get_photo_list():
    photo_dir = os.path.join(app.static_folder, 'photos')
    if not os.path.exists(photo_dir):
        return []
    # 只保留常见图片格式
    allowed_ext = ('.jpg', '.jpeg', '.png', '.webp')
    photos = [f for f in os.listdir(photo_dir) if f.lower().endswith(allowed_ext)]
    return photos

@app.route('/')
def index():
    photos = get_photo_list()
    return render_template('index.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)
