#1. longest substring without repeating characters
s = input().strip()
l=0
ans=0
uni=set()
for i in range(len(s)):
    ch=s[i]
    if ch not in uni:
        uni.add(ch)
    else:
        while ch in uni:
            uni.remove(s[l])
            l+=1
        uni.add(ch)
    ans=max(ans,i-l+1)
print(ans)

#2. longest repeating character replacement
s = input().strip()
k = int(input())

count = {}
left = 0
max_freq = 0
answer = 0

for right, ch in enumerate(s):
    count[ch] = count.get(ch, 0) + 1
    max_freq = max(max_freq, count[ch])

    while (right - left + 1) - max_freq > k:
        count[s[left]] -= 1
        left += 1

    answer = max(answer, right - left + 1)

print(answer)

#3. minimum window substring
from collections import Counter

s = input().strip()
t = input().strip()

need = Counter(t)
window = {}

required = len(need)
formed = 0

left = 0
best_len = float('inf')
best_start = 0

for right, ch in enumerate(s):
    window[ch] = window.get(ch, 0) + 1

    if ch in need and window[ch] == need[ch]:
        formed += 1

    while formed == required:
        if right - left + 1 < best_len:
            best_len = right - left + 1
            best_start = left

        left_char = s[left]
        window[left_char] -= 1

        if left_char in need and window[left_char] < need[left_char]:
            formed -= 1

        left += 1

if best_len == float('inf'):
    print(-1)
else:
    print(s[best_start:best_start + best_len])

#4. valid anagram
s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("NO")
else:
    count = [0] * 26

    for ch in s1:
        count[ord(ch) - ord('a')] += 1

    for ch in s2:
        count[ord(ch) - ord('a')] -= 1

    if all(x == 0 for x in count):
        print("YES")
    else:
        print("NO")

#5. group anagrams
from collections import defaultdict

n = int(input())
words = input().split()

groups = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    groups[key].append(word)

for group in groups.values():
    print(*group)

#6. Find the Index of the First Occurrence in a String
haystack = "sadbutsad"
needle = "sad"
lps = [0] * len(needle)
pre = 0
for i in range(1, len(needle)):
    while pre > 0 and needle[i] != needle[pre]:
        pre = lps[pre-1]
    if needle[pre] == needle[i]:
        pre += 1
        lps[i] = pre
n=0
for h in range(len(haystack)):
    while n > 0 and needle[n] != haystack[h]:
        n = lps[n-1]
    if needle[n] == haystack[h]:
        n += 1
    if n == len(needle):
        print(h - n + 1)
print(-1)

#7. longest palindromic substring
s = "babad"
if not s:
    print("")
start, end = 0, 0
def expand_around_center(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
for i in range(len(s)):
    len1 = expand_around_center(i, i)
    len2 = expand_around_center(i, i + 1)
    max_len = max(len1, len2)
    if max_len > end - start:
        start = i - (max_len - 1) // 2
        end = i + max_len // 2
print(s[start:end + 1])


#8. reverse words in a string
s = "the sky is blue"
def word_generator(text):
    n = len(text)
    right = n - 1
    
    while right >= 0:
        while right >= 0 and text[right].isspace():
            right -= 1
        if right < 0:
            break
            
        left = right
        while left >= 0 and not text[left].isspace():
            left -= 1
            
        yield text[left + 1 : right + 1]
        right = left
s = "the sky is blue"
print(" ".join(word_generator(s)))

#9. sort characters by frequency
s="tree"
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
sorted_chars = sorted(dic.items(), key=lambda item: item[1], reverse=True)

result = []
for char, freq in sorted_chars:
    result.append(char * freq)
    
print("".join(result))

#10. isomorhphic strings
s = "egg"
t = "add"
dic={}
rev={}
iso=True
for i in range(len(s)):
    ch1=s[i]
    ch2=t[i]
    if ch1 not in dic and ch2 not in rev:
        dic[ch1]=ch2
        rev[ch2]=ch1
    elif (ch1 in dic and dic[ch1]!=ch2):
        iso=False
        break
    elif (ch2 in rev and rev[ch2]!=ch1):
        iso=False
        break
print(iso)

#11. Longest common prefix
strs = ["flower","flow","flight"]
if not strs:
   print(" ")
prefix = strs[0]
for i in range(1, len(strs)):
    while not strs[i].startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            print("")
print(prefix)