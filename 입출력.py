import re

def 이어쓰기(파일명,문자열):
  with open(파일명, 'at', encoding='utf8') as f:
    f.write(f'{문자열}\n')

def 가져오기(파일명, 리스트로_반환_여부=False):
  with open(파일명, 'r', encoding='utf8') as f:
    if 리스트로_반환_여부:
      z=re.findall(r'.+',f.read())
      
    else:
      z=str()
      for i in f.readlines():
        z+=i

    return z
    
