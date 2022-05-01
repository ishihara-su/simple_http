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
    - Example: `python3 http_server.py`
      - Press Ctrl+C to stop.

- tcp_client.py
  - Simple TCP client program.
  - This program gets a text line from the keyboard and sent it to the server, then
    receives data up to 1024 bytes from the server.
    - Example: `python3 http_clt.py localhost`
      - You will be asked to type some text. Type something and hit Enter.
