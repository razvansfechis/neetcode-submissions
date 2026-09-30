class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        position_array = defaultdict(list)

        max_val, min_val = -1, 101

        for idx, price in enumerate(prices):
            position_array[price].append(idx)
            max_val = max(max_val, price)
            min_val = min(min_val, price)

        max_dif = 0

        for lf in range(min_val, max_val):
            for rt in range(max_val, lf, -1):
                if position_array[lf] and position_array[rt]:
                    current_min_pos_lf = 101
                    current_max_pos_rt = -1

                    for pos in position_array[lf]:
                        current_min_pos_lf = min(current_min_pos_lf, pos)

                    for pos in position_array[rt]:
                        current_max_pos_rt = max(current_max_pos_rt, pos)

                    if current_max_pos_rt > current_min_pos_lf:
                        max_dif = max(max_dif, rt - lf)


        return max_dif