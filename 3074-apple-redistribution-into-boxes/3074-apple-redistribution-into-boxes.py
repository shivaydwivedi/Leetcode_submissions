class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        # Total apples that need to be stored
        total_apples = sum(apple)

        # Sort capacities in descending order
        capacity.sort(reverse=True)

        curr_capacity = 0
        boxes_used = 0

        # Pick boxes until capacity covers all apples
        for cap in capacity:
            curr_capacity += cap
            boxes_used += 1
            if curr_capacity >= total_apples:
                return boxes_used
