import time
begin = time.time()

def canbuildword(s, isoriginalword, mp):
    if s in mp and mp[s] == 0:
        return False
    if s in mp and mp[s] == 1 and isoriginalword == 0:
        return True
    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]
        if left in mp and mp[left] == 1 and canbuildword(right, 0, mp):
            return True
    mp[s] = 0
    return False
def printlongestword(listofwords):
    mp = dict()
    for i in listofwords:
        mp[i] = 1
    listofwords.sort(key=lambda x: len(x), reverse=True)
    for i in listofwords:
        if canbuildword(i, 1, mp):
            return i
    return "-1"

if __name__ == "__main__":
    my_file = open("Input_02.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    longCWord=printlongestword(content_list)
    print("Longest Compound Word:",longCWord)
    content_list.remove(longCWord)
    secondLongCWord=printlongestword(content_list)
    print("Second Longest Compound Word:",secondLongCWord)
    

    time.sleep(1)
    end = time.time()
    print(f"Time taken to process the input file: {end - begin}")
