# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src\\server.py'],
             pathex=['src', 'd:\\work\\part3\\backend_demon'],
             binaries=[],
             datas=[
                 ('./src/helpers/authuser/templates','./django/contrib/admin/templates'),
                 ('./src/helpers/director/templates','./django/contrib/admin/templates'),
                 ('./src/helpers/case/jb_admin/templates','./django/contrib/admin/templates'),
             ],
             hiddenimports=['settings','wsgi','whitenoise','whitenoise.middleware'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='server',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
          
# --------------      
b = Analysis(['src\\manage.py'],
             pathex=['src', 'd:\\work\\part3\\backend_demon'],
             binaries=[],
             datas=[
                 ('./src/helpers/authuser/templates','./django/contrib/admin/templates'),
                 ('./src/helpers/director/templates','./django/contrib/admin/templates'),
                 ('./src/helpers/case/jb_admin/templates','./django/contrib/admin/templates'),
             ],
             hiddenimports=['settings','wsgi'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
b_pyz = PYZ(b.pure, b.zipped_data,
             cipher=block_cipher)

b_exe = EXE(pyz,
          b.scripts, 
          [],
          exclude_binaries=True,
          name='manage',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None ) 
          
          

          
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               
               
               b_exe,
               b.binaries,
               b.zipfiles,
               b.datas, 
               
               strip=False,
               upx=True,
               upx_exclude=[],
               name='server')