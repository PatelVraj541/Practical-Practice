st = input("Enter a string: ")
st = st.lower()
rev = st[::-1]
if st == rev:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
