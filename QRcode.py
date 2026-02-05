import qrcode
import cv2

url = 'https://www.google.com'
qr_img = qrcode.make(url)
qr_img.save(stream='./images/gg_QR.png')
print('QRtesting~~~ 저장성공')

img = cv2.imread('./images/gg_QR.png')
cv2.imshow('title', img)
print('QRtesting~~~ 열기성공')
cv2.waitKey(0) #키입력까지 대기 
cv2.destroyAllWindows() #메모리상에 남아있는 cv2관련 창 close()

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

# 에러 ModuleNotFoundError: No module named 'PIL'
# 에러 (.venv) C:\dongaAI\day0205cv2>  pip install  PIL
# 정답 (.venv) C:\dongaAI\day0205cv2>  pip install  pillow  