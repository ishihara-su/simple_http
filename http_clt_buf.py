
# http_clt_buf.py - Simple HTTP client with BufferedI/O
#   Susumu Ishihara <ishihara.susumu@shizuoka.ac.jp>
#
# Comments are writtnn in Japanese for Japanese students
#
# バッファドI/Oを使ったHTTPのクライアントプログラム
# http_clt.pyの改造版
#
# このプログラムではHTTPのための高度なモジュールを使っていません。
# 低水準のソケット通信用ライブラリのみを使って、
# HTTP/1.1 での通信を行います。
# ポート番号は80であることを前提としています。
# 受信したデータは標準出力に書き出されます。
#
# http_clt.py との違い。
#   http_clt.pyではヘッダ部分を読み込む時に、1バイトずつrecv()をしていました。
#   この実装では、1バイト読むたびに毎回システムコールが呼ばれることになり、効率が
#   悪かったのですが、このプログラムではできるだけ大きなまとまりでrecv()するように
#   行うようにしているので、効率が良くなっています。
#
# 使い方 python3 http_clt.py ホスト名/パス
#        例: python3 http_clt_buf.py doc.ishilab.net/edu/cn/
#        例: python3 http_clt_buf.py doc.ishilab.net/edu/cn/apache_pb.gif > apache_pb.gif
#
# Requestsライブラリを使うと、もっと簡単にpythonでWebアクセスを扱うことができます。
#    https://requests-docs-ja.readthedocs.io/en/latest/
#

import socket
import sys

# バッファ付きでのソケットからの読み出し用クラス
class BufReader:
    DEFAULT_READBUF_LENGTH = 8192
    def __init__(self, sock, buffer_size=DEFAULT_READBUF_LENGTH):
        self.sock = sock
        self.buf = b''
        self.buffer_size = buffer_size

    def readline(self):
        buffering = True
        while buffering:
            if b'\r\n' in self.buf:
                (line, self.buf) = self.buf.split(b'\r\n', 1)
                return line
            more = self.sock.recv(self.buffer_size)
            if not more:
               buffering = False
            else:
               self.buf += more
        line = self.buf
        self.buf = b''
        return line

    def read(self, read_length):
        remained_bytes = read_length
        data = b''
        while remained_bytes > 0:
            if len(self.buf) >= remained_bytes:
                data += self.buf[:remained_bytes]
                self.buf = self.buf[remained_bytes:]
                break
            data += self.buf
            remained_bytes -= len(self.buf)
            self.buf = self.sock.recv(min(remained_bytes, self.buffer_size))
            if not self.buf:
                break
        return data

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
    # 読み出し用のファイルオブジェクトを作る
    rf = BufReader(s)

    # ヘッダを受信して解析・・・Content-Lengthを得る
    while True:
        line = rf.readline()
        chunks = line.split(b':', 1)
        if len(chunks) == 2 and chunks[0] == b'Content-Length':
            content_length = int(chunks[1])
        if len(line) == 0:
            break

    # データを受信
    received_data = rf.read(content_length)

# 受信したデータを標準出力に出力
sys.stdout.buffer.write(received_data)
