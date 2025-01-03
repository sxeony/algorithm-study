def recursive(n, depth=0):  # depth 기본값을 0으로 설정
    print('____' * depth + '"재귀함수가 뭔가요?"')
    
    if n == 0:  
        print('____' * depth + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print('____' * depth + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이 세상 모든 지식을 통달한 선인이 있었어.')
        print('____' * depth + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('____' * depth + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        recursive(n - 1, depth + 1)  # depth를 증가시켜 재귀 호출
    
    print('____' * depth + '라고 답변하였지.')

# 메인 함수
N = int(input("N을 입력하세요: "))  # 사용자로부터 입력 받기
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursive(N)  # depth는 기본값(0)으로 시작
