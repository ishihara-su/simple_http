# http_requests.py - Simple HTTP client in Python using Requests module
#    Susumu Ishihara <ishihara.susumu@shizuoka.ac.jp>
#
# Comments are writtnn in Japanese for Japanese students
#
# このプログラムではRequestsライブラリを使ったHTTPクライアントを実装しています。
#
# 準備:  Requestsモジュールをインストールしておきます
#         python3 -m pip install requests
#
# 使い方 python3 http_clt.py URL
#        例: python3 http_clt.py https://doc.ishilab.net/edu/cn/
#        例: python3 http_clt.py https://doc.ishilab.net/edu/cn/apache_pb.gif > apache_pb.gif
#
import requests
import sys

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} URL', file=sys.stderr)
    sys.exit(1)

url = sys.argv[1]
r = requests.get(url)
sys.stdout.buffer.write(r.content)
