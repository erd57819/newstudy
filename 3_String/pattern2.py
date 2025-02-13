t = 'TTTTTATTAATA'
p = 'TZA'

def search(p, t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):  # t에서 패턴을 비교할 시작 위치 인덱스
        for j in range(M):      # p에서 비교할 위치 인덱스
            if t[i+j]!=p[j]:
                break
        else:               # break에 걸리지 않고 for가 끝난경우 실행
            return i        # 패턴이 처음 나타난 인덱스 리턴
    return -1               # t에 p패턴이 없는 경우

print(search(p, t))


def bm(t, p):
    N = len(t)  # 텍스트 길이
    M = len(p)  # 패턴 길이

    # 점프 테이블 초기화 (ASCII 범위 활용)
    jump = [M] * (ord('z') + 1)  

    # 패턴 내 문자별 이동 거리 설정
    for i in range(M):  # 패턴 길이를 기준으로 해야 함
        jump[ord(p[i])] = M - 1 - i

    # 검색 시작 (패턴 끝에서부터 비교)
    i = j = M - 1  
    while i < N:  
        if t[i] == p[j]:  # 문자 일치
            if j == 0:  # 패턴의 첫 글자까지 일치하면 찾은 것
                return i  # 매칭된 위치 반환
            i -= 1
            j -= 1
        else:  # 불일치 시 점프
            i += jump[ord(t[i])]
            j = M - 1  # 다시 패턴의 끝에서 비교

    return -1  # 패턴을 찾지 못한 경우

# 테스트 예제
t = "ABAAABCD"
p = "ABC"
print(bm(t, p))  # 기대 결과: 4


