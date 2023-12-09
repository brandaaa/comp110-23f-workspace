def free_biscuits(input: dict[str, list[int]]) -> dict[str,bool]:
    result: dict[str, bool] = {}
    for key in input
        sum_list: list[int] = input[key]
        sum: int = 0
        for elems in sum_list:
            sum += elems
        if sum >= 100:
                result[key] = 100
        else:
            result[key] = False
    return result 

def max_key(input: dict[str, list[int]]) -> str:
    sum_list: str = ""
    max_sum: int = 0
        for key in input:
            val_sum: int = 0
            for value in input[key]:
                val_sum += value
            if val sum > max_val_sum:
                max_val_sum = val_sum
                max_key = key
        return max_key

def multiples(input: list[int]) -> list[bool]:
    output: list[bool] = []
    output.append(input[0] % input[len(input) - 1] == 0)
    idx: int = 1
    while idx < len(input)
        output.append(input[idx] % input[idx-1] == 0)
        idx += 1
    return output 

def merge_list(input: list[str], input2: list[int]) -> dict[str, int]:
    combined: dict[str, int] = {}
        if len(input) != len(input2)
            return combined
        
        i: int = 0
        while i < len(input):
            combined[input[i] = input2[i]]
            i += 1

        return combined

def reverse_multiply(nums: list[int]) -> list[int]:
    new_list: list[int] = []

    i: int = len(nums) - 1
        while i>=0:
            new_list.append(nums[i]*2)
            i -=1
        return new_list


    
