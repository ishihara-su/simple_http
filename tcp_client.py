# tcp_client.py for Python 3
#    Susumu Ishihara <ishihara.susumu@shizuoka.ac.jp>
#
#    TCPを使う簡単なクライアント
#    1行分のデータを標準入力から受け取って、サーバに送信し、
#    最大1024バイトをサーバから受け取って、標準出力に表示する。

import socket
import sys

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} server_name', file=sys.stderr)
    sys.exit(1)

server_name = sys.argv[1]
server_port = 50000  # サーバのポート

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ソケットを作る
client_socket.connect((server_name, server_port))  # サーバのソケットに接続する
sentence = input('Input lowercase sentence: ')   # キーボードから入力された文字列を受け取る
client_socket.send(sentence.encode())  # 文字列をバイト配列に変換後、送信する。
modified_sentence = client_socket.recv(1024)  # 最大1024バイトを受け取る。受け取った内容はバイト配列として格納される。
print('From Server: {0}'.format(modified_sentence.decode()))  # バイト配列を文字列に変換して表示する
client_socket.close()  # ソケットを閉じる
