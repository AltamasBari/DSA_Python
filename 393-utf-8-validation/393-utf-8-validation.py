class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        #https://www.youtube.com/watch?v=3zyxpFPKkEU&list=TLGGWESoMR4Sa-MxMzA5MjAyMg&t=404s
        remBytes = 0
        
        for num in data:
            if not remBytes:
                if num >> 7 == 0b0:
                    remBytes = 0
                elif num >> 5 == 0b110:
                    remBytes = 1
                elif num >> 4 == 0b1110:
                    remBytes = 2
                elif num >> 3 == 0b11110:
                    remBytes = 3
                else:
                    return False
            else:
                if num >> 6 != 0b10:
                    return False
                remBytes -= 1
        
        return remBytes == 0