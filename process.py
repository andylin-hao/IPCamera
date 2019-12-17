# import numpy as np
# import json
#
# addresses = np.array(json.load(open("addresses.json")))
# passwords = np.load("actual_passwords.npy", allow_pickle=True)
#
# accessible = addresses[passwords != -1]
# hackable = addresses[np.logical_and(passwords != -1, passwords != None)]
# hackable_pwd = passwords[np.logical_and(passwords != -1, passwords != None)]
# pwd_count = dict()
#
# for pwd in hackable_pwd:
#     pwd_count[pwd] = pwd_count.get(pwd, 0) + 1
#
# pwd_count = sorted(pwd_count.items(), key=lambda x: x[1], reverse=True)
#
# pwd = [pc[0] for pc in pwd_count]
# count = [pc[1] for pc in pwd_count]
#
# with open("data.txt", 'w+') as file:
#     file.write(str(pwd))
#     file.write('\n')
#     file.write(str(count))
#
#

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats
n = 20
p = 0.9
k = np.arange(0,41)
binomial = stats.binom.pmf(k,n,p)
print(binomial)
plt.plot(k, binomial, 'o-')
plt.title('binomial:n=%i,p=%.2f (www.jb51.net)'%(n,p),fontsize=15)
plt.xlabel('number of success（脚本之家测试）',fontproperties='SimHei')
plt.ylabel('probalility of success', fontsize=15)
plt.grid(True)
plt.show()