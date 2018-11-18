#! /usr/bin/env python3

import re
import pyperclip

phone_regexp = re.compile(r'''(
                          (\d{2,3}|\(\d{2,4}\))?
                          (\s|-|\.)?
                          (\d{3,4})
                          (\s|-|\.)?
                          (\d{3,4})
                          (\s*(ext|x|ext.)\s*(\d{2,5}))?
                          )''', re.VERBOSE)

email_regexp = re.compile(r'''(
                          [0-9a-zA-Z._%+-]+
                          @
                          [0-9a-zA-Z.-]+
                          (\.[a-zA-Z]{2,4})
                           )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phone_regexp.findall(text):
  phone_num = '-'.join([groups[1], groups[3], groups[5]])
  print(phone_num)
  if groups[8] != '':
    phone_num != ' x' + groups[8]
  matches.append(phone_num)

for groups in email_regexp.findall(text):
  print(groups)
  matches.append(groups[0])

if len(matches) > 0:
  pyperclip.copy("\n".join(matches))
  print('クリップボードにコピーしました。')
else:
  print('電話番号とメールアドレスは見つかりませんでした。')

