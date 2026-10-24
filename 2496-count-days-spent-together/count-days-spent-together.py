# class Solution:
#     def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

#         ans = 0
#         if arriveAlice[:3] != arriveBob[:3]:
#             return 0

#         else:
#             if arriveAlice[3:] <= arriveBob[3:]:
#                 if leaveBob[3:]>=leaveAlice[3:]:
#                     ans = abs(int(arriveBob[3:]) - int(leaveAlice[3:]) + 1)
#                     return ans 
#                 else:
#                     return 0


#             else:
#                 if leaveAlice[3:]>=leaveBob[3:]:
#                     ans = abs(int(arriveAlice[3:]) - int(leaveBob[3:]) + 1)
#                     return ans 
#                 else:
#                     return 0    


#         return ans 









class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        a1 = int(arriveAlice[:2])
        d1 = int(arriveAlice[3:])
        a2 = int(leaveAlice[:2])
        d2 = int(leaveAlice[3:])

        b1 = int(arriveBob[:2])
        e1 = int(arriveBob[3:])
        b2 = int(leaveBob[:2])
        e2 = int(leaveBob[3:])

        startA = d1
        for i in range(a1 - 1):
            startA += months[i]

        endA = d2
        for i in range(a2 - 1):
            endA += months[i]

        startB = e1
        for i in range(b1 - 1):
            startB += months[i]

        endB = e2
        for i in range(b2 - 1):
            endB += months[i]

        start = max(startA, startB)
        end = min(endA, endB)

        if start <= end:
            return end - start + 1
        else:
            return 0
