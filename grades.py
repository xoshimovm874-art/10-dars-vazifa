talabalar = {}

def baho_qoshish(baza, ism, baho):
  baza.setdefault(ism, []).append(baho)

def ortacha_baho(baza, ism):
  b = baza.get(ism, [])
  return sum(b) / len(b) if b else 0

def eng_yuqori_talaba(baza):
  if not baza:
    return None
  return max(baza, key=lambda x: sum(baza[x]) / len(baza[x]))

baho_qoshish(talabalar, "Ali", 5)
baho_qoshish(talabalar, "Salim", 4)
baho_qoshish(talabalar, "Vali", 5)

print("Ali o'rtachasi:", ortacha_baho(talabalar, "Ali"))
print("Eng yaxshi talaba:", eng_yuqori_talaba(talabalar))