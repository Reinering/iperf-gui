#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com
"""

import subprocess
import datetime
import os
import re
import sys
import platform
os_platform = platform.system()

Version = "v0.0.01"
Computer_Digits = 'x86'
TypeNum = 2
pyVer = "3.10.2"
FileList = [
    {
        'name': "iperf-dev.py",
        'settingFile': "manage.py",
        'outName': "iperf-dev",
    }
]
isclean = True

Type = {
    1: 'Alpha',
    2: 'Beta',
    3: 'RC',
    4: 'Release'
}

PackageArgs = {
    'console': True,  # [True, False] -w 关闭， -c(默认) 开启 开启或关闭显示控制台 (只对Windows有效)
    'debug': False,  # [True, False] -d [{all,imports,bootloader,noarchive} 产生debug版本的可执行文件
    'specPath': '',
    # --specpath 指定spec文件的生成目录,如果没有指定,而且当前目录是PyInstaller的根目录,会自动创建一个用于输出(spec和生成的可执行文件)的目录.如果没有指定,而当前目录不是PyInstaller的根目录,则会输出到当前的目录下.
    'importPath': '',
    # -p, -–path=DIR 设置导入路径(和使用PYTHONPATH效果相似).可以用路径分割符(Windows使用分号,Linux使用冒号)分割,指定多个目录.也可以使用多个-p参数来设置多个导入路径
    'excludeModule': '',  # –exclude-module 需要排除的module
    'hiddenImport': [],  # –hidden-import 打包额外py库
    'iconPath': '',
    # -i 指定程序图标 –icon=<FILE.ICO> 将file.ico添加为可执行文件的资源 –icon=<FILE.EXE,N> 将file.exe的第n个图标添加为可执行文件的资源  (只对Windows系统有效)
    'workpath': '',  # --workpath WORKPATH 生成过程中的中间文件存放目录，默认：当前目录的build文件夹内
    'logLevel': 'INFO',
    # --log-level LEVEL 控制编译时pyi打印的信息，一共有6个等级，由低到高分别为TRACE DEBUG INFO(默认) WARN ERROR CRITICAL。也就是默认清空下，不打印TRACE和DEBUG信息
    'outType': 'FILE',  # ['FOLDER', 'FILE'] 打包的文件类型：-F 产生一个文件用于部署；-D 产生一个目录用于部署 (默认)
    'outName': '',  # -n NAME 打包的文件名 可选的项目(产生的spec的)名字.如果省略,第一个脚本的主文件名将作为spec的名字
    'distpath': '',  # --distpath DIR 生成文件存放目录，当前目录的dist文件夹内
    'addData': [],  # -add-data <SRC;DEST or SRC:DEST> 打包额外资源
    'addBinary': [],  # --add-binary <SRC;DEST or SRC:DEST> 打包额外的代码
    'isClean': False,  # [True, False] --clean 在本次编译开始时，清空上一次编译生成的各种文件,默认：不清除
    'encode': '',  # -a, --ascii 不包含unicode支持,默认：尽可能支持unicode
    'isCover': False,  # [True, False] -y, --noconfirm 如果dist文件夹内已经存在生成文件，则不询问用户，直接覆盖, 默认：询问是否覆盖
    'upxDir': '',  # --upx-dir UPX_DIR UPX实用程序的路径（默认值：搜索执行路径）
    'versionFile': '',  # --version-file FILE 添加版本信息文件
    'manifest': '',  # -m, --manifest <FILE or XML> 添加manifest文件
    'additionalHooksDir': '',  # --additional-hooks-dir HOOKSPATH 指定用户的hook目录
    'runtimeHook': '',  # --runtime-hook RUNTIME_HOOKS 指定用户runtime-hook,如果设置了此参数，则runtime-hook会在运行main.py之前被运行
    'runtimeTmpdir': '',  # --runtime-tmpdir PATH 指定运行时的临时目录, 默认：使用系统临时目录
    'resource': '',  # -r, --resource RESOURCE
    'key': '',  # --key KEY pyi会存储字节码，指定加密字节码的key, 16位的字符串
    'pyinstallerEXEList': {  # pyinstaller 各环境
        'x86': [
            {
                'version': '3.6.7',
                "path": r"D:\ProgramData\Anaconda3\envs\py32",
            },
            {
                'version': '3.8.8',
                "path": r"D:\ProgramData\Anaconda3\envs\py38_32",
            },
            {
                'version': '3.10.2',
                "path": r"D:\Program Files\anaconda3\envs\py310_32",
            }

        ],
        'x64': [
            {
                'version': '3.8.3',
                "path": r"D:\ProgramData\Anaconda3",
            },
            {
                'version': '3.6.9',
                "path": r"D:\ProgramData\Anaconda3\envs\py36_64",
            },
            {
                'version': '3.8.5',
                "path": r"D:\ProgramData\Anaconda3\envs\py38_64",
            },
            {
                'version': '3.10.2',
                "path": r'D:\Program Files\anaconda3\envs\py310_64',
            }

        ]
    }
}

def overrideSetting(file, now):

    if not os.path.exists(file['settingFile']):
        return

    with open(file['settingFile'], 'r', encoding='utf-8') as f:
        lines = f.readlines()
        with open(file['settingFile'], 'w', encoding='utf-8') as f_w:
            for line in lines:
                if "version: " in line:
                    line = "version: " + Version + '\r'
                elif "VERSION = " in line:
                    line = "VERSION = \"" + Version + '\"\r'
                elif "Computer_Digits = " in line:
                    line = "Computer_Digits = \"" + str(Computer_Digits) + '\"\r'
                elif "Package_Time = " in line:
                    line = "Package_Time = \"" + now + '\"\r'
                elif "TYPENUM = " in line:
                    line = "TYPENUM = " + str(TypeNum) + '\r'
                elif "CURRENT_DB = " in line:
                    if TypeNum < 4:
                        line = "CURRENT_DB = \"test\"" + '\r'
                    else:
                        line = "CURRENT_DB = \"deploy\"" + '\r'
                else:
                    pass
                f_w.write(line)


def packaging():
    global PackageArgs
    os_ver = platform.win32_ver()
    print("操作系统：", os_ver[0])

    current_path = os.getcwd()


    cmd = ''
    for py in PackageArgs['pyinstallerEXEList'][Computer_Digits]:
        if "WINDOWS" in os_platform.upper():
            if py['version'] == pyVer:
                cmd = '"' + py['path'] + '\Scripts\pyinstaller.exe' + '"'
                break
        elif "LINUX" in os_platform.upper():
            cmd = "~/.local/bin/pyinstaller"
            break

    if not PackageArgs['console'] or TypeNum == 4:
        cmd = cmd + ' -w'

    if PackageArgs['debug']:
        cmd = cmd + ' -d'

    if PackageArgs['specPath']:
        cmd = cmd + ' --specpath ' + PackageArgs['specPath']

    if PackageArgs['importPath']:
        cmd = cmd + ' -p ' + PackageArgs['importPath']

    if PackageArgs['excludeModule']:
        cmd = cmd + ' –exclude-module ' + PackageArgs['excludeModule']

    if PackageArgs['hiddenImport']:
        for tmp in PackageArgs['hiddenImport']:
            cmd = cmd + ' --hiddenimport ' + tmp

    if PackageArgs['iconPath']:
        cmd = cmd + ' -i ' + current_path + '\\' + PackageArgs['iconPath']

    if PackageArgs['workpath']:
        cmd = cmd + ' --workpath ' + PackageArgs['workpath']

    if PackageArgs['logLevel'] != 'INFO':
        cmd = cmd + ' --log-level ' + PackageArgs['logLevel']

    if PackageArgs['outType'] == 'FILE':
        cmd = cmd + ' -F'

    if PackageArgs['outName']:
        cmd = cmd + ' -n ' + PackageArgs['outName']

    if PackageArgs['distpath']:
        cmd = cmd + ' --distpath ' + PackageArgs['distpath']

    if PackageArgs['addData']:
        for tmp in PackageArgs['addData']:
            cmd = cmd + ' --add-data ' + '"' + tmp + '"'

    if PackageArgs['addBinary']:
        pass

    if PackageArgs['isClean']:
        cmd = cmd + ' --clean'

    if PackageArgs['encode']:
        cmd = cmd + ' -a'

    if PackageArgs['isCover']:
        cmd = cmd + ' -y'

    if PackageArgs['upxDir']:
        cmd = cmd + ' --upx-dir ' + PackageArgs['upxDir']

    if PackageArgs['versionFile']:
        cmd = cmd + ' --version-file ' + PackageArgs['versionFile']

    if PackageArgs['manifest']:
        cmd = cmd + ' -m ' + PackageArgs['manifest']

    if PackageArgs['additionalHooksDir']:
        pass

    if PackageArgs['runtimeHook']:
        pass

    if PackageArgs['runtimeTmpdir']:
        pass

    for file in FileList:
        now = datetime.datetime.now().strftime("%Y%m%d%H%M")
        cmd = cmd + ' ' + file['name']
        print(cmd)

        overrideSetting(file, now)

        if "LINUX" in os_platform.upper():
            tmp = PackageArgs['distpath'] + '/' + file['name'].replace('.py', '')
            if TypeNum == 4:
                renameCMD = 'mv ' + tmp + ' ' + PackageArgs['distpath'] + '/' + file['outName'] + '_' + Computer_Digits + '_' + now
            else:
                renameCMD = 'mv ' + tmp + ' ' + PackageArgs['distpath'] + '/' + file['outName'] + '_' + Type[TypeNum] + Computer_Digits + '_' + now
            cleanCMD = "rm -rf " + "build/" + file['name'].replace('.py', '')
        elif "WINDOWS" in os_platform.upper():
            tmp = PackageArgs['distpath'] + '\\' + file['name'].replace('.py', '.exe')
            if TypeNum == 4:
                renameCMD = 'move ' + tmp + ' ' + PackageArgs['distpath'] + '\\"' + file['outName'] + '_' + Computer_Digits + '_' + now + '.exe"'
            else:
                renameCMD = 'move ' + tmp + ' ' + PackageArgs['distpath'] + '\\"' + file['outName'] + '_' + Type[TypeNum] + Computer_Digits + '_' + now + '.exe"'
            cleanCMD = "RD /Q /S " + "build\\" + file['name'].replace('.py', '')

        subprocess.run(cmd, shell=True)
        if os.path.exists(tmp):
            subprocess.run(renameCMD, shell=True)

        if isclean:
            # subprocess.run("DEL /F /Q /S " + name + '.spec', shell=True)
            subprocess.run(cleanCMD, shell=True)



if __name__ == "__main__":
    if "LINUX" in os_platform.upper():
        PackageArgs['distpath'] = os.path.join(os.getcwd(), 'dist')
    else:
        PackageArgs['distpath'] = r'W:\work_2\PythonApp_Package\iperf-gui'

    PackageArgs['isClean'] = True
    PackageArgs['hiddenImport'] = [

    ]

    PackageArgs['addData'] = [
        # windows以;分割，linux以:分割
        # "default:default",
        # "pic;pic",
        # "ui/style;ui/style"
        "iperf\\*;iperf"
    ]

    PackageArgs['iconPath'] = r'pic\favicon.ico'

    Computer_Digits = 'x64'

    TypeNum = 2
    packaging()
