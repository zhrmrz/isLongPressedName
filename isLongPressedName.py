class Sol(object):
    def isLongPressedName(self,name,typed):
        j=0
        for i in range(len(name)-1):
            c=name[i]
            if c != typed[j]:
                return False
            elif c==typed[j] and c==typed[j+1]:
                j+=2
            else:
                j+=1
        return True

if __name__ == '__main__':
    p = Sol()
    print(p.isLongPressedName(name="alex",typed='aleex'))
