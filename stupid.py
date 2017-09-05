'''def func(*args, **kwargs):
       pass
'''

import time

def time_show(*args, f_io: str, n_nde: int, t_prl: str, **kwargs):
    try:
        t_s = args[0].split(' ')
        t_s = t_s[4].split(':')
        t_n = time.asctime().split(' ')
        t_n = t_n[4].split(':')
        t_p = (int(t_s[2])) - (int(t_n[2]))
        t_p *= -1
    except:
        t = 1
    print('Time: %s - %ds timer passed\n' % (time.asctime(), t_p))
    time.sleep(1)
    
def counter(l_time, n):
    res = n + int(l_time)
    print(res)