# Thực hành lập trình mạng nâng cao

AI Contest

# Hướng dẫn cài đặt

<h3>Cài đặt virtualenv trên máy</h3>
<h4>Sau khi cài đặt chỉ cần dùng 'pip freeze > requirements.txt' để ghi những thư viện đã cài đặt trong Venv vào file txt. Khi cần install chạy 'pip install -r requirements.txt' để cài đặt những packages cho dự án</h4>
<h2><u>Lưu ý:</u> nếu không dùng Venv thì lệnh 'pip freeze > requirements.txt' thì sẽ ghi tất cả các packages mà máy các đồng chí đang dùng trên máy thật</h2>
<ul>
Cách cài trên Window, Ubuntu tự kiếm nha:
<li>Tại thư mục dự án</li>
<li>pip install virtualenv </li>
<li>Tao môi trường: " vvirtualenv -p python . " //hình như vậy</li>
<li>Chạy env: source scripts/activate (Ubuntu source bin/activate)</li>
<li>Cài các file cần thiết: 'pip install -r requirements.txt'</li>
<li>Ghi ra các file mới đã cài: 'pip freeze > requirements.txt'</li>
<li>Tắt môi trường: deactivate</li>
</ul>
