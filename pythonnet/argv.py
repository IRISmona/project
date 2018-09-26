#!/usr/bin/env python3
import sys
print(sys.argv)

# tarena@tedu:~/计算机/pythonnet$ python3 argv.py
# ['argv.py']
# tarena@tedu:~/计算机/pythonnet$ python3 argv.py hello
# ['argv.py', 'hello']
# tarena@tedu:~/计算机/pythonnet$ python3 argv.py hello 1 2 3
# ['argv.py', 'hello', '1', '2', '3']
# tarena@tedu:~/计算机/pythonnet$ python3 argv.py 'hello 1 2 3'
# ['argv.py', 'hello 1 2 3']

# tarena@tedu:~/计算机/pythonnet$ ls -l argv.py
# -rw-rw-r-- 1 tarena tarena 36 9月   6 11:13 argv.py
# tarena@tedu:~/计算机/pythonnet$ chmod 766 argv.py
# tarena@tedu:~/计算机/pythonnet$ ls
# argv.py  tcp_client.py  tcp_server.py  udp_client.py  udp_server.py  wang.py


# tarena@tedu:~/计算机/pythonnet$ ./argv.py
# ['./argv.py']
