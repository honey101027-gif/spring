
# testfaker.py

import qrcode
import cv2
from faker import Faker

my = Faker()
for k in range(10):
    print(my.name())

print()
for k in range(10):
    print(my.ipv4_private())


print()
for k in range(10):
    print(my.ipv4_private())

data = Faker('ko_KR')
for k in range(20):
    print(data.name())

print()
for k in range(20):
    print(data.address())

# 수작업으로 가상 실행
# C:\dongaAI\day0205cv2> cd .venv
# C:\dongaAI\day0205cv2\.venv> cd Scripts
# C:\dongaAI\day0205cv2\.venv\Scripts> activate
# (.venv) C:\dongaAI\day0205cv2\.venv\Scripts> cd..
# (.venv) C:\dongaAI\day0205cv2\.venv> cd..

# (.venv) C:\dongaAI\day0205cv2> py QRcode.py
# ModuleNotFoundError: No module named 'qrcode'
# (.venv) C:\dongaAI\day0205cv2> pip install qrcode  
# (.venv) C:\dongaAI\day0205cv2> py QRcode.py

# 에러 ModuleNotFoundError: No module named 'cv2'
# 에러 (.venv) C:\dongaAI\day0205cv2>  pip install cv2
# 정답 (.venv) C:\dongaAI\day0205cv2>  pip install opencv-python
# 에러 (.venv) C:\dongaAI\day0205cv2>  pip install  PIL
# 정답 (.venv) C:\dongaAI\day0205cv2>  pip install  pillow  

