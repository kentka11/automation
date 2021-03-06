#! /usr/bin/env python3

"""

# pw.py - パスワード管理プログラム(脆弱性あり)

"""

PASSWORDS = {'gmail': 'mkBil2020',
             'accenture': 'mkBil2019',
             'github': 'Effort22'}
import sys
import pyperclip

if len(sys.argv) < 2:
  print('使い方: python pw.py [アカウント名]')
  print('パスワードをクリップボードにコピーします')
  sys.exit()

account = sys.argv[1] #最初のコマンドライン引数がアカウント名

if account in PASSWORDS:
  pyperclip.copy(PASSWORDS[account])
  print(account + 'のパスワードをクリップボードにコピーしました。')
else:
  print(account + 'というアカウント名はありません。')

