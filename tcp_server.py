# tcp_server.py for Python 3
#    Susumu Ishihara <ishihara.susumu@shizuoka.ac.jp>
#    TCPで通信する簡単なサーバ
#    クライアントから最大1024バイト受信し、大文字に変換して送り返す。

import socket
import sys

server_port = 50000  # 接続待ち受けポート番号
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCPを使う待ち受け用のソケットを作る
server_socket.bind(('', server_port))  # ポート番号をソケットに対応づける
server_socket.listen(1)  # クライアントからの接続を待つ
print('The server is ready to receive', file=sys.stderr)

while True:
    # クライアントからの接続があったら、それを受け付け、
    # そのクライアントとの通信のためのソケットを作る
    connection_socket, addr = server_socket.accept()

    # クライアントからバイト列を最大1024バイト受信し、
    # 文字列に変換（decode()）する。
    sentence = connection_socket.recv(1024).decode()

    # 受け取った文字列を大文字に変換する
    capitalized_sentence = sentence.upper()

    # 大文字になった文字列をバイト列に変換して送信する。
    connection_socket.send(capitalized_sentence.encode())
    connection_socket.close()
