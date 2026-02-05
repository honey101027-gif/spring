# workscore.py

# 해결순서0] 변수초기화 선언=declare
kor,eng,hap,avg = 0,0,0,0
info = ''
message = ''

kor = 30
eng = 95
hap = kor + eng
avg = hap//2
# 파이썬 초간단 연산처리 
# 해결순서1] 국어,영어 점수 input()데이터입력받기, 형변환
# 해결순서2] 총계, 평균 연산처리 
# 해결순서3] 평균점수 70점부터 축합격 0~69점까지 재시험  if~else제어문 사용
# 해결순서4] 국어, 영어, 총계, 평균, 합격여부 출력
print()
print(f'국어={kor}')
print(f'영어={eng}')
print(f'합계={hap}')
print(f'평균={avg}')
print('오늘은 2월 05일 목요일')
print('내일은 2월 06일 금요일')



