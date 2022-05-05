# http_clt.py - Simple HTTP client
#   Susumu Ishihara <ishihara.susumu@shizuoka.ac.jp>
#
# Comments are writtnn in Japanese for Japanese students
#
# このプログラムではHTTPのための高度なモジュールを使っていません。
# 低水準のソケット通信用ライブラリのみを使って、
# HTTP/1.1 での通信を行います。
# ポート番号は80であることを前提としています。
# 受信したデータは標準出力に書き出されます。
#
# 使い方 python3 http_clt.py ホスト名/パス
#        例: python3 http_clt.py doc.ishilab.net/edu/cn/
#        例: python3 http_clt.py doc.ishilab.net/edu/cn/apache_pb.gif > apache_pb.gif
#
# Requestsライブラリを使うと、もっと簡単にpythonでWebアクセスを扱うことができます。
#    https://requests-docs-ja.readthedocs.io/en/latest/
#

import socket
import sys

READBUF_LENGTH = 1024

# ソケットから1行分データを読み込む関数（行末の\r\nは返さない）
def read_line_from_socket(s):
    last_byte = 0
    line_bytes = bytearray(b'')
    while True:
        b = s.recv(1)[0]
        line_bytes.append(b)
        if last_byte == 13 and b == 10: # CR: 13, LF: 10
            break
        last_byte = b
    return line_bytes[:-2]

# コマンドラインからホスト名、パス名を読み込む
if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} hostname/path', file=sys.stderr)
    sys.exit(1)
chunks = sys.argv[1].split('/', 1) # Gets hostname and path
if len(chunks) == 2:
    [hostname, path] = chunks
else:
    [hostname, path] = [chunks[0], '']
# サーバに送る要求メッセージ
req_msg = f'GET /{path} HTTP/1.1\r\nHost: {hostname}\r\n\r\n'

# ソケットを作成してサーバに接続
port = 80
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((hostname, port))  # 接続
    s.sendall(req_msg.encode())  # メッセージの文字列をバイト列に変換して送信
    header = ''
    content_length = 0
    # ヘッダを受信して解析・・・Content-Lengthを得る
    while True:
        line = read_line_from_socket(s)
        chunks = line.split(b':', 1)
        if len(chunks) == 2 and chunks[0] == b'Content-Length':
            content_length = int(chunks[1])
        if len(line) == 0:
            break

    # データを受信
    received_data = b''
    remained_bytes = content_length
    while remained_bytes > 0:
        data = s.recv(min(remained_bytes, READBUF_LENGTH))
        received_bytes = len(data)
        if received_bytes <= 0:
            break
        received_data += data
        remained_bytes -= received_bytes

# 受信したデータを標準出力に出力
sys.stdout.buffer.write(received_data)
