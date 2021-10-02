#문제1_사칙연산 수행 프로그램

num1 = int(input("첫번째 숫자를 입력하시오: "))
num2 = int(input("두번째 숫자를 입력하시오: "))

print("\n1)덧셈, 2)뺄셈, 3)곱셈, 4)나눗셈")
op = int(input("어떤 연산을 원하는지 번호를 입력하세요: "))

if op==1 :
  res = num1+num2
  print('\n결과는 다음과 같습니다 : ',num1,'+',num2,'=',res)

elif op==2 :
  res = num1-num2
  print('\n결과는 다음과 같습니다 : ',num1,'-',num2,'=',res)

elif op==3 :
  res = num1*num2
  print('\n결과는 다음과 같습니다 : ',num1,'*',num2,'=',res)

elif op==4 :
  res = num1/num2
  print('\n결과는 다음과 같습니다 : ',num1,'/',num2,'=',res)

else :
  print('\n잘못 입력하였습니다.')
