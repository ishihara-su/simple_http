# simple_http

Simple HTTP in Python3 - Susumu Ishihara <ishihara.susumu@shizuoka.ac.jp>

- http_clt.py
  - This program etrieves a resource of a given hostname and path, e.g. www.sample.com/sample.html
  - The obtained data is output to the standard output.
  - Example:
    - `python3 http_clt.py doc.ishilab.net/edu/cn/`
    - `python3 http_clt.py doc.ishilab.net/edu/cn/apache_pb.gif > img.gif`

- tcp_server.py
  - Simple TCP server program.
  - This program receives text data (up to 1024 bytes) and converts the text to uppercase,
    then sends it back to the client.
    - Example: `python3 tcp_server.py`
      - Press Ctrl+C to stop.

- tcp_client.py
  - Simple TCP client program.
  - This program gets a text line from the keyboard and sent it to the server, then
    receives data up to 1024 bytes from the server.
    - Example: `python3 tcp_client.py localhost`
      - You will be asked to type some text. Type something and hit Enter.

- http_clt_buf.py
  - Modified version of http_clt.py to use buffered I/O.
  - Example:
    - `python3 http_clt_buf.py doc.ishilab.net/edu/cn/`
    - `python3 http_clt_buf.py doc.ishilab.net/edu/cn/apache_pb.gif > img.gif`

- http_clt_requests.py
  - HTTP client based on Requests library.
  - Example:
    - `python3 http_clt_requests.py https://doc.ishilab.net/edu/cn/`
    - `python3 http_clt_requests.py http://doc.ishilab.net/edu/cn/apache_pb.gif > img.gif`
