#문제2_1~200 사이의 정수 중 3의 배수 또는 5의 배수 출력하기
count=0

for i in range(1,201):
  if i%3==0 or i%5==0:
    print(i,end=' ')
    count+=1

print("\n200 이하의 양의 정수 중 3의 배수 또는 5의 배수의 개수는",count,"개 입니다.")
