# -*- mode: python ; coding: utf-8 -*-
# python -m PyInstaller .\MMD-GUI-Term.spec --noconfirm
import os

version_num = "1.0.4"
version_term = "T"
version_string = version_num+version_term
with open('version.py', 'w') as f:
    f.write(f'VERSION = "{version_string}"\n')


a = Analysis(
    ['main-tk.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('adb_tools', 'adb_tools'), 
        ('ContentFrames', 'ContentFrames'), 
        ('config.json','.'),
        ('Backup', 'Backup'), 
        ('images', 'images')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MMD-GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['images\\mmd_icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MMD-GUI-Term',
)

try:
    os.remove("version.py")
except FileNotFoundError:
    pass