a='aiyeouAIYEOUbkxznhdcwgpvjqtsrlmfBKXZNHDCWGPVJQTSRLMF'
b='eouaiyEOUAIYpvjqtsrlmfbkxznhdcwgPVJQTSRLMFBKXZNHDCWG'
t=str.maketrans(a,b)
for i in open(0):print(i.strip('\n').translate(t))