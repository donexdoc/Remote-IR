# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['remote_ir_gui.py'],
             pathex=['D:\\Users\\donex\\PycharmProjects\\Remote-IR'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('app-icon.svg','D:\\Users\\donex\\PycharmProjects\\Remote-IR\\assets\\icons\\app-icon.svg', "DATA")]
a.datas += [('info-solid.svg','D:\\Users\\donex\\PycharmProjects\\Remote-IR\\assets\\icons\\info-solid.svg', "DATA")]
a.datas += [('pause-solid.svg','D:\\Users\\donex\\PycharmProjects\\Remote-IR\\assets\\icons\\pause-solid.svg', "DATA")]
a.datas += [('play-solid.svg','D:\\Users\\donex\\PycharmProjects\\Remote-IR\\assets\\icons\\play-solid.svg', "DATA")]
a.datas += [('sync-solid.svg','D:\\Users\\donex\\PycharmProjects\\Remote-IR\\assets\\icons\\sync-solid.svg', "DATA")]
a.datas += [('save-solid.svg','D:\\Users\\donex\\PycharmProjects\\Remote-IR\\assets\\icons\\save-solid.svg', "DATA")]
a.datas += [('plus-solid.svg','D:\\Users\\donex\\PycharmProjects\\Remote-IR\\assets\\icons\\plus-solid.svg', "DATA")]
a.datas += [('trash-solid.svg','D:\\Users\\donex\\PycharmProjects\\Remote-IR\\assets\\icons\\trash-solid.svg', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='remote_ir_gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='assets\\icons\\app-icon.ico')
