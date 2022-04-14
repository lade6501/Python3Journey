'''
    Trying to implement Naive pattern matching algorithm.
'''

def searchPattern(text,pat):
    n = len(text)
    m = len(pat)
    i = 0

    for i in range(n-m+1):
        j = 0

        while j < m :
            if text[i+j]!= pat[j]:
                break
            j += 1
        
        if (j == m):
            print("Pattern found at index ",i)

if __name__ == '__main__':
    text = 'ABCEABCDABCEABCD'
    pat = 'ABCD'
    searchPattern(text,pat)