
# Import thư viện Flask
from flask import Flask, render_template

# Khởi tạo Flask
app = Flask(__name__)

# Hàm xử lý request
@app.route("/", methods=['GET'])
def home_page():
    # Đi đến thư mục chứa file index
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)