class Solution:

    def encode(self, strs: List[str]) -> str:

        str = ""

        for val in strs:
            str += val
            str += "µ"

        return str


    def decode(self, s: str) -> List[str]:

        lst = []

        aux = ""
        for val in s:
            if val != "µ":
                aux += val
            else:
                lst.append(aux)
                aux = ""

        # print(lst)

        return lst
