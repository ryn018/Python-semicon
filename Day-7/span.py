# Upgrade the getSpan(s, ss) function to raise an exception if ss = '' or s = '', test it

string = "mississippi"
ss = ''
 
def getSpan(str1, ss):
    if str1 == "" or ss == "":
        raise Exception()
    spans = []
    start = 0
    while start < len(str1):
        index = str1.find(ss, start)
        if index == -1:
            break
 
        spans.append((index, index + len(ss) - 1))
        start = index + 1
    return spans



try:
    span = getSpan(string,ss)
    print(span)
except Exception as e:
    print(f"should not put empty string {e}")