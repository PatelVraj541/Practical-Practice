st = 'I love doing python programming in spyder'
words = st.split()
for word in words:
    if len(word) % 2 == 0:
        print(word, "-> even!")
