#! /usr/bin/python3
import os, sys

## 親の場合子プロセスのID、子の場合0が返る
ret = os.fork()

if ret == 0:
    print("子プロセス: pid={}、親プロセスｎpid={}".format(os.getpid(), os.getppid()))
    exit()
elif ret > 0:
    print("親プロセス: pid={}、子プロセスｎpid={}".format(os.getpid(), ret))
    exit()

sys.exit(1)
