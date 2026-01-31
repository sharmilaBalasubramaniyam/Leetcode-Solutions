class Solution:
    def reverseByType(self, s: str) -> str:
        arr=list(s)
        n=len(s)

        l,r=0,n-1

        while l<r:
            if not ('a' <= arr[l] <= 'z'):
                l+=1
            elif not ('a' <= arr[r] <= 'z'):
                r-=1
            else:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        l,r=0,n-1
        while l<r:
            if 'a' <= arr[l] <= 'z':
                l+=1
            elif 'a' <= arr[r] <= 'z':
                r-=1
            else:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        return "".join(arr)
