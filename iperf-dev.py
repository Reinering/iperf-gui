#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com
"""


import sys
import os
import time
import datetime
import argparse
import subprocess
import platform


os_platform = platform.system()

if 'windows' in os_platform.lower():
    ROOT_PATH = ''
else:
    ROOT_PATH = './'

LOG_PATH = os.path.join(ROOT_PATH, 'logs')

if os.path.exists("iperf3.exe"):
    IPERF_PATH = ROOT_PATH
elif os.path.exists(os.path.join(ROOT_PATH, 'iperf3/iperf3.exe')):
    IPERF_PATH = os.path.join(ROOT_PATH, 'iperf3')
else:
    IPERF_PATH = ''

def create_file():
    """
    创建日志文件夹和日志文件
    """

    if not os.path.isdir(LOG_PATH):
        os.mkdir(LOG_PATH)


def iperf(params):
    if not params:
        print('iperf3 param not found')
        return

    now = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    filePath = os.path.join(LOG_PATH, now + '.log')

    cmd = [os.path.join(IPERF_PATH, 'iperf3')]
    cmd.extend(['-c', '192.168.15.2', '-t', '60'])
    print("cmd", cmd)
    p = subprocess.Popen(' '.join(cmd),
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     shell=True)

    with open(filePath, 'w') as f:
        while p.returncode == None:

            # err = str(p.stderr.readline(), encoding="gb2312", errors="ignore")
            # print(err)
            # if err:
            #     f.write(err)
            #     if "'iperf3' 不是内部或外部命令，也不是可运行的程序" in err:
            #         return
            #     elif "iperf3: error" in err:
            #         return

            out = p.stdout.readlines()
            # out = str(p.stdout.read(), encoding="gb2312", errors="ignore")
            for line in out:
                print(line)
                if isinstance(line, bytes):
                    line = line.decode(encoding="gb2312")
                f.write(line)

                if "iperf Done." in line:
                    return


def main(*argv,  **kwargs):
    if not argv:
        argv = sys.argv

    # print(argv)

    create_file()

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-lt',
                            default=-1,
                            type=int,
                            help="loop times -1: off 0: always 1-: time")
        parser.add_argument('-li',
                            default=0,
                            type=int,
                            help="loop interval")

        args, unknown = parser.parse_known_args()
        print(args, unknown)

        # print("args.lt", args.lt, getattr(args, "lt"))
        # if getattr(args, "lt") and args.lt:
        #     print("args.lt", args.lt)
        #     lt = args.lt
        #
        # if getattr(args, "li") and args.li:
        #     li = args.li

    except Exception as e:
        print(e)

    lt = args.lt
    li = args.li

    if lt == -1:
        print("iperf3 start......")
        iperf(unknown)
    elif lt == 0:
        while True:
            print("iperf3 start......")
            iperf(unknown)
            print("next loop wait......")
            time.sleep(li)
    else:
        i = 0
        while i < lt:
            print("iperf3 start......")
            iperf(unknown)
            print("next loop wait......")
            time.sleep(li)
            i += 1

    print("iperf3 loop end......")






if __name__ == "__main__":
    sys.exit(main())

