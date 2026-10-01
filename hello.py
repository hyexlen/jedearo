"""kakao = ["가나", "다라", "마바", "사아", "자차"]
print(kakao)
kakao.append(None)
print(kakao)
kakao[5] = kakao[4]
kakao[4] = None
print(kakao)
kakao[4] = kakao[3]
kakao[3] = None
print(kakao)
kakao[3] = "삽입"
print(kakao)
"""
#index    0        1     2        3       4
kakao = ["가나", "다라", "마바", "사아", "자차"]
print(kakao)
#step 1
kakao[2] = None
print(kakao)
#step 2
kakao[2] = kakao[3]
kakao[3] = None
print(kakao)
# step 3
kakao[3] = kakao[4]
kakao[4] = None
print(kakao)