# -*- coding: utf-8 -*-

"""
Module implementing MaintenanceWindow.
"""
import subprocess
import os
import datetime
import re
import platform



Version = "v2.2.3"
Computer_Digits = 'x64'
TypeNum = 2
pyVer = "3.6.9"
FileList = [
    {
        'name': "main.py",
        'outName': "iperf_client",
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
    'console': False,                           # [True, False] -w 关闭， -c(默认) 开启 开启或关闭显示控制台 (只对Windows有效)
    'debug': False,                             # [True, False] -d [{all,imports,bootloader,noarchive} 产生debug版本的可执行文件
    'specPath': '',                             # --specpath 指定spec文件的生成目录,如果没有指定,而且当前目录是PyInstaller的根目录,会自动创建一个用于输出(spec和生成的可执行文件)的目录.如果没有指定,而当前目录不是PyInstaller的根目录,则会输出到当前的目录下.
    'importPath': '',                           # -p, -–path=DIR 设置导入路径(和使用PYTHONPATH效果相似).可以用路径分割符(Windows使用分号,Linux使用冒号)分割,指定多个目录.也可以使用多个-p参数来设置多个导入路径
    'excludeModule': '',                        # –exclude-module 需要排除的module
    'hiddenImport': '',                         # –hidden-import 打包额外py库
    'iconPath': '',                             # -i 指定程序图标 –icon=<FILE.ICO> 将file.ico添加为可执行文件的资源 –icon=<FILE.EXE,N> 将file.exe的第n个图标添加为可执行文件的资源  (只对Windows系统有效)
    'workpath': '',                             # --workpath WORKPATH 生成过程中的中间文件存放目录，默认：当前目录的build文件夹内
    'logLevel': 'INFO',                         # --log-level LEVEL 控制编译时pyi打印的信息，一共有6个等级，由低到高分别为TRACE DEBUG INFO(默认) WARN ERROR CRITICAL。也就是默认清空下，不打印TRACE和DEBUG信息
    'outType': 'FILE',                          # ['FOLDER', 'FILE'] 打包的文件类型：-F 产生一个文件用于部署；-D 产生一个目录用于部署 (默认)
    'outName': '',                              # -n NAME 打包的文件名 可选的项目(产生的spec的)名字.如果省略,第一个脚本的主文件名将作为spec的名字
    'distpath': '',                             # --distpath DIR 生成文件存放目录，当前目录的dist文件夹内
    'addData': [],                              # -add-data <SRC;DEST or SRC:DEST> 打包额外资源
    'addBinary': [],                            # --add-binary <SRC;DEST or SRC:DEST> 打包额外的代码
    'isClean': False,                           # [True, False] --clean 在本次编译开始时，清空上一次编译生成的各种文件,默认：不清除
    'encode': '',                               # -a, --ascii 不包含unicode支持,默认：尽可能支持unicode
    'isCover': False,                           # [True, False] -y, --noconfirm 如果dist文件夹内已经存在生成文件，则不询问用户，直接覆盖, 默认：询问是否覆盖
    'upxDir': '',                               # --upx-dir UPX_DIR UPX实用程序的路径（默认值：搜索执行路径）
    'versionFile': '',                          # --version-file FILE 添加版本信息文件
    'manifest': '',                             # -m, --manifest <FILE or XML> 添加manifest文件
    'additionalHooksDir': '',                   # --additional-hooks-dir HOOKSPATH 指定用户的hook目录
    'runtimeHook': '',                          # --runtime-hook RUNTIME_HOOKS 指定用户runtime-hook,如果设置了此参数，则runtime-hook会在运行main.py之前被运行
    'runtimeTmpdir': '',                        # --runtime-tmpdir PATH 指定运行时的临时目录, 默认：使用系统临时目录
    'resource': '',                             # -r, --resource RESOURCE
    'key': '',                                  # --key KEY pyi会存储字节码，指定加密字节码的key, 16位的字符串
    'pyinstallerEXEList': {                     # pyinstaller 各环境
        'x86': [
            {
                'version': '3.6.7',
                "path": r"D:\ProgramData\Anaconda3\envs\py32",
            }
        ],
        'x64': [
            {
                'version': '3.6.3',
                "path": r"D:\ProgramData\Anaconda3",
            },
            {
                'version': '3.5.4',
                "path": r"D:\ProgramData\Anaconda3\envs\Py35"
            },
            {
                'version': '3.6.9',
                "path": r"D:\ProgramData\Anaconda3\envs\py36_64",
            },
        ]
    }

}


def packaging():
    global PackageArgs
    os_ver = platform.win32_ver()
    print("操作系统：", os_ver[0])

    current_path = os.getcwd()

    cmd = ''
    for py in PackageArgs['pyinstallerEXEList'][Computer_Digits]:
        if py['version'] == pyVer:
            cmd = py['path'] + '\Scripts\pyinstaller.exe'
            break

    if not PackageArgs['console']:
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
        cmd = cmd + ' –hidden-import ' + PackageArgs['hiddenImport']

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
        pass

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

        with open(file['name'], 'r', encoding='utf-8') as f:
            lines = f.readlines()
            with open(file['name'], 'w', encoding='utf-8') as f_w:
                for line in lines:
                    # print(line)
                    if "version: " in line:
                        line = "version: " + Version + '\r'
                    elif "Version = " in line:
                        line = "Version = \"" + Version + '\"\r'
                    elif "Computer_Digits = " in line:
                        line = "Computer_Digits = \"" + str(Computer_Digits) + '\"\r'
                    elif "Package_Time = " in line:
                        line = "Package_Time = \"" + now + '\"\r'
                    f_w.write(line)

        subprocess.run(cmd, shell=True)
        if PackageArgs['distpath']:
            tmp = PackageArgs['distpath'] + '\\' + file['name'].replace('.py', '.exe')
            if os.path.exists(tmp):
                if TypeNum == 4:
                    subprocess.run('mv ' + tmp + ' ' + PackageArgs['distpath'] + '\\' + file['outName'] + '_' + Computer_Digits + '_' + now + '.exe', shell=True)
                else:
                    subprocess.run('mv ' + tmp + ' ' + PackageArgs['distpath'] + '\\' + file['outName'] + '_' + Type[TypeNum] + Computer_Digits + '_' + now + '.exe', shell=True)

    if isclean:
        # subprocess.run("DEL /F /Q /S " + name + '.spec', shell=True)
        subprocess.run("RD /Q /S " + "build\\" + file['name'].replace('.py', ''), shell=True)



if __name__ == "__main__":
    PackageArgs['console'] = True
    PackageArgs['isClean'] = True
    PackageArgs['distpath'] = r'F:\PythonAPP_Package\Iperf_GUI'

    packaging()
