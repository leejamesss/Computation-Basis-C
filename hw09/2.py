import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for b in buildings:
            # 将每个建筑物的左右端点作为标记点，并将高度作为标记类型（负数表示左端点，正数表示右端点）
            points.append((b[0], -b[2]))
            points.append((b[1], b[2]))
        points.sort()

        heap = [0]  # 使用一个最大堆来维护当前可见的建筑物的高度
        res = []
        prev_max = 0
        for p in points:
            if p[1] < 0:  # 如果是左端点，将其对应的高度加入最大堆中
                heapq.heappush(heap, p[1])
            else:  # 如果是右端点，将其对应的负高度从最大堆中删除
                heap.remove(-p[1])
                heapq.heapify(heap)
            cur_max = -heap[0]  # 当前可见建筑物的最大高度
            if cur_max != prev_max:  # 如果最大高度变化了，说明发生了轮廓点转折
                res.append([p[0], cur_max])
                prev_max = cur_max
        return res
# https://leetcode.cn/problems/the-skyline-problem/submissions/
