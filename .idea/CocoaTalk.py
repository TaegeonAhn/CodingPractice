import socket
import argparse
import threading
import time

host = "127.0.0.1"
port = 4000
user_list = {}
notice_flag = 0

def handle_receive(client_socket, addr, user):
    while 1:
        data = client_socket.recv(1024)
        string = data.decode()

        if string == "/종료" :
            break

        string = f'({user} : {string})'
        print(string)

        for con in user_list.values():
            try:
                con.sendall(string.encode())
            except:
                print("연결이 비 정상적으로 종료된 소켓")

    del user_list[user]
    client_socket.close()

def handle_notice(client_socket, addr, user):
    pass

def accept_func():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #IPv4 체계. TCP 타입의 소켓 객체를 생성
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #포트가 사용 중인 경우 에러를 해결하기 위한 구문
    server_socket.bind(host, port)
    #ip 주소와 port번호를 함께 socket 에 바인드한다. 포트의 범위는 1-65535 사이의 숫자를 사용할 수 있다.
    server_socket.listen(5)
    #서버가 최대 5개의 클라이언트 접속을 허용한다.

    while 1:
        try:
            client_socket, addr = server_socket.accept()
            #클라이언트 함수가 접속하면 새로운 소켓을 반환한다.
        except KeyboardInterrupt:
            for user, con in user_list:
                con.close()
            server_socket.close()
            print("Keyboard Interrupt")
            break
        user = client_socket.recv(1024)
        user_list[user] = client_socket

        # accept() 함수로 입력만 받아주고 이후 알고리즘은 핸들러에게 맡긴다.
        notice_thread = threading.Thread(target=handle_notice, args=(client_socket, addr, user))
        notice_thread.daemon = True
        notice_thread.start()








