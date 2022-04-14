# Python program for A modified Naive Pattern Searching
#With some optimization

def searchPattern(text,pat):
    n = len(text)
    m = len(pat)
    i = 0

    while i <= (n-m):
        j = 0
        for j in range(m):
            if text[i+j] != pat[j]:
                break
            j += 1
        
        if j == m:
            print ("Pattern found at index " + str(i))
            i += m
        elif j == 0:
            i += 1
        else:
            i += j

if __name__ == '__main__':
    text = 'ABCEABCDABCEABCD'
    pat = 'ABCD'
    searchPattern(text,pat)


