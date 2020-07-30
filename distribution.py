# Beta Distribution simulator.
# https://en.wikipedia.org/wiki/Beta_distribution
# https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Beta_distribution_pdf.png/1280px-Beta_distribution_pdf.png
# DONT USE TABS FOR INDENTS (ONLY SPACES)

import random

def distt(alpha, beta, samples = 1200):
  results = [0] * 50               #
  for i in range(samples):
    result = random.betavariate(alpha, beta) * 50
    if result < 50:
	    results[int(result)] += 1 
  for i in range(50):
    print(round(i/50,1), " ", "|" * results[i])
