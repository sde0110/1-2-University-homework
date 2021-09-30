import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#문제1_몫과 나머지 구하기

a = int(input("정수 a를 입력하시오: "))
b = int(input("정수 b를 입력하시오: "))
print('%d / %d의 몫은 %d 입니다.' %(a,b,a/b))
print('%d / %d의 나머지는 %d 입니다.' %(a,b,a%b))
