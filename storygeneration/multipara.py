# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 19:31:05 2019

@author: Pratik
"""
import os 
import subprocess
from subprocess import call

#print("First Paragraph")
ip1='Watson was scared that someone was following him into the dark alleyway.'
print("1st para prompt:", ip1)
print()
bad_chars = ['  ', '\n', '\r'] 
out = subprocess.check_output(['python', 'sample.py', '--prime',str(ip1), '--quiet'])
out=str(out)
out=out.replace("\\n", "")
out=out.replace("\\r", " ")
out=out.replace("'", "")
out=out.replace("\\", "")
out=out.replace("b", "", 1)
out=out.strip()
print(out)

out1=str(out).split('.')
ip2=out1[-1]
ip2=ip2.strip('"')
ip2=ip2.strip()
len1=len(ip2)
if ip2[len1-1]!='.':
    ip2 = out1[-2]
    ip2=ip2.strip('"')
    ip2=ip2.strip()
    len1=len(ip2)
    if ip2[len1-1]!='.':
        ip2=ip2 + '.'
print()
print("2nd para prompt:", ip2)
print()
#print("Second Paragraph")
out2= subprocess.check_output(['python', 'sample.py', '--prime',str(ip2), '--quiet'])
out2=str(out2)
out2=out2.replace("\\n", "")
out2=out2.replace("\\r", " ")
out2=out2.replace("\\", "")
out2=out2.replace("'", "")
out2=out2.replace("b", "", 1)
# out2.replace(ip1, '', 1)
out2=out2.replace(ip2, '')
out2=out2.strip()
print(out2)





# with open('firstoutput.txt', 'w') as f:
#     f.write(str(out))
    

#os.system('python sample.py --prime="I was scared"')

# Sample output:
# 1st para prompt: As he walked into the street he was afraid of what might happen to him.

# As he walked into the street he was afraid of what might happen to him. That was our own danger? But I think that I broke it down upon my breast. I could only saw my hair and a sharp chuckle in the room which he is, however, unpaid, so because he might break his house, but he was an old doctor, but I know with them at the beginning of the French Museum down with seven thousand wolves all the use of insects, an quarry. A night chirrup or word, you would be glad to put up up. And what do you hesitate?" "There is only local subjects coming from the woods," said he,

# 2nd para prompt: A night chirrup or word, you would be glad to put up up.

# There are decidedly parties at the moment this morning--a cheerful, a connoisseur as Captain William began to conclude nothing of our worthy of humours, and I observed that my horror was afar. "By my soul! they have not encouraged me ill?" I kept my girth to the house and to eat and let me be welcome to both," said he. Inscribed round in a brisker chair, and slamming his plate from the table beside him. He was dressed than that mind shown that a luckless evening, and in no muscle of anger had been lopped off from them.