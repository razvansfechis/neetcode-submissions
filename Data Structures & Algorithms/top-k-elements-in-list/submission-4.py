class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # initialize an empty list of lists for the bucket sort
        lst_of_lst = []
        for idx in range(len(nums)):
            lst_of_lst.append([])

        # print(lst_of_lst)

        # get the frequency of each number in the initial list
        freq_count = {}
        for num in nums:
            freq_count[num] = 1 + freq_count.get(num, 0)

        for key, val in freq_count.items():
            lst_of_lst[val - 1].append(key)

        # print(lst_of_lst)

        final_list = []

        for lst in reversed(lst_of_lst):
            for val in lst:
                if k > 0:
                    final_list.append(val)
                else:
                    return final_list

                k -= 1

        return final_list