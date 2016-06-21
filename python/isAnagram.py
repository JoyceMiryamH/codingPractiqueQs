def isAnagram (str1, str2):
    a = ''.join(sorted(str1.lower()))
    b = ''.join(sorted(str2.lower()))
    if a == b:
        print("anagram")
    else:
        print("not anagram")
        
# test
isAnagram("hello", "ol4hel");
