import random
def random_str(digits=True, lowercase=True, uppercase=True, symbol=True, slen=10):
    seed = ''
    seed = seed + '1234567890' if digits else seed+''
    seed = seed + 'abcdefghijklmnopqrstuvwxyz' if lowercase else seed + ''
    seed = seed + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if uppercase else seed + ''
    seed = seed + '!@#$%^&*()_+=-' if symbol else seed + ''
    if len(seed)==0:
        return None
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)

print(random_str())