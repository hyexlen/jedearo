#스택 초기화 함수
def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1
    return print("스택 초기화가 완료되었습니다. 스택 크기는"+str(size)+"입니다.")

#스택 full 여부 확인 함수
def is_full():
    global top
    if top == len(stack)-1:
        return print("스택이 가득 찼습니다.")#true
    else:
        return print("스택이 가득 차지 않았습니다.")#false

#스택 empty 여부 확인 함수
def is_empty():
    global top
    if top == -1:
        return True
    else:
        return False
    
#push 함수
def push(data):
    global top
    top +=1
    stack[top] = data

# pop함수
def pop():
    global top
    data = stack[top]
    stack[top] = None
    if (is_empty()):
        top -=1
        return print("스택이 비어있습니다.")
    else:
        top -=1
        return print("pop된 데이터"+str(data))

#peak함수
def peak():
    global top
    data = stack[top]
    return print("peak된 데이터" + str(data))


#스택 출력 함수
def print_stack():
    print("===스택상태===")
    for i in range(len(stack)-1, -1, -1):
        print(stack[i])
    print("=================")

init_stack(7)
is_full()
push("커피")
push("녹차")
push("꿀물")
push("콜라")
push("사이다")
print_stack()
pop()
pop()
pop()
print_stack()
peak()
