class Solution:
    def findParent(self,v,parents):
        if v==parents[v]:
            return v
        parents[v]=self.findParent(parents[v],parents)
        return parents[v]
        

    def equationsPossible(self, equations: List[str]) -> bool:
        parents=[i for i in range(26)]
        for eq in equations:
            if eq[1]=="=":
                U=self.findParent(ord(eq[0])-ord('z'),parents)
                V=self.findParent(ord(eq[3])-ord('z'),parents)
                parents[U]=V
        for eq in equations:
            if eq[1]=="!":
                U=self.findParent(ord(eq[0])-ord('z'),parents)
                V=self.findParent(ord(eq[3])-ord('z'),parents)
                if U==V:
                    return False
        return True