import unittest
# 分析空位情况：1,首位有人；2，尾位有人；3中间占人
# 输入：空位列表 输出：结果位置和最大距离
# 1.输入：list=[1,0,0,0] 输出：[3],3
# 2.输入：list=[0,0,0,1] 输出：[0],3
# 3.输入：list=[1,0,0,0,1,0,1] 输出：[2],2
# 4.输入：list=[1,0,0,1,0] 输出:[1,2,4],1

class Testlist(unittest.TestCase):

    def test_case1(self):
        list=[1,0,0,0]
        self.assertEqual(solution(list),([3], 3))
    
    def test_case2(self):
        list=[0,0,0,1]
        self.assertEqual(solution(list), ([0], 3))

    def test_case3(self):
        list=[1,0,0,0,1,0,1]
        self.assertEqual(solution(list), ([2], 2))

    def test_case4(self):
        list=[1,0,0,1,0]
        self.assertEqual(solution(list), ([1,2,4], 1))

def solution(seats):
    """
    seats: List[int]
    return: ans[int],int
    """
    persons = [p for p, seat in enumerate(seats) if seat == 1]
    nullseat = [p for p, seat in enumerate(seats) if seat == 0]
    maxdict = max(persons[0], 
              len(seats)-1-persons[-1], 
              max([(persons[r]-persons[r-1])//2 for r in range(1, len(persons))]+[0]))
    ans=[]
    for i in nullseat:
        if min([abs(i-j) for j in persons])==maxdict:
           ans.append(i) 
    return ans,maxdict

if __name__ == '__main__':
    unittest.main()