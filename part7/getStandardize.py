#! /usr/bin/env python3

import re, pyperclip

date_formats = re.compile(r'''(
                         (\d{4})
                         (/|-|年|)?
                         ([01][0-9])
                         (/|-|月|)?
                         ([0123][0-9])
                         (/|-|日|)?
                         )''', re.VERBOSE)

text = """
       2018-10-27
       2018/02/30
       2019年8月20日
       2018/2/30
       2019/10/2
       2019年10/20
       2018-10/11
       18/10/27
       20180606
       201866
       3000-08-10
       """
#text = str(pyperclip.paste())
matches = []

for groups in date_formats.findall(text):
  print(groups)
  matches.append((groups[1] + "/" + groups[3] + "/" + groups[5]))

print('\n'.join(matches))
#print(text)

