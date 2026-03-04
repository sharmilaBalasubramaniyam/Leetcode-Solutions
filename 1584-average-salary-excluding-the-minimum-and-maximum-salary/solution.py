class Solution:
    def average(self, salary: List[int]) -> float:
        tot=sum(salary)
        mn=min(salary)
        mx=max(salary)

        return (tot-mn-mx)/(len(salary)-2)
