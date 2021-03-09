def maximumProduct(nums):        
        first_max = max(nums)
        nums.remove(first_max)
        second_max = max(nums)
        nums.remove(second_max)
        third_max = max(nums)
        
        first_min = min(nums)
        nums.remove(first_min)

        top3product = first_max * second_max * third_max

        if nums:
            second_min = min(nums)
            product_of_two_min_and_max_value = first_max * first_min * second_min
            return max(top3product, product_of_two_min_and_max_value)
        else:
            return top3product
