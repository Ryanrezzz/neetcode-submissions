class Solution:

    def encode(self, strs: List[str]) -> str:
        str1=''
        for word in strs:
            str1+=str(len(word))+"#"+word
        return str1

    def decode(self, s: str) -> List[str]:
        str2=''
        lenght=''
        lst=[]
        i=0
        start=i
        while i < len(s):
          
            if s[i]=='#':
                length=int(s[start:i])
                str2+=s[i+1:i+length+1]
                lst.append(str2)
                i=i+length+1
                start=i
            length=''
            str2=''
            i=i+1
            
        return lst