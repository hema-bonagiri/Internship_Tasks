#Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    freq = {}
    
    for word in sentence.split():
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq

#------------------------------------------------------------------
#Q2. Find the Frequency of Each Character in a Word
def character_count(word):
    freq = {}
    for ch in word:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq

#--------------------------------------------------------------------
#Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating(word):
    for ch in word:
        if word.count(ch)==1:
            return ch 
    return None

#--------------------------------------------------------------------
#Q4. Check Whether Two Strings Are Anagrams
def anagram(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    if(sorted(s1)==sorted(s2)):
        return True
    else:
        return False
    
#--------------------------------------------------------------------
#Q5. Find the First Repeating Character in a String
def first_repeating(word):
    word = word.replace(" ","").lower()
    first_char = set()
    
    for ch in word:
        if ch in first_char:
            return ch
        first_char.add(ch)
    return None

#--------------------------------------------------------------------
#Q6. Move All Zeros to the End of a List
def list_of_numbers(nums):
    res = []
    
    for num in nums:
        if num!=0:
            res.append(num)
    res.extend([0]*nums.count(0))
    return res

#-----------------------------------------------------------------------
#Q7. Find the Second Highest Distinct Number in a List
def second_largest_distinct_num(nums):
    unique_nums = set(nums)
    if(len(unique_nums)<2):
        return None
    return sorted(unique_nums)[-2]

#-----------------------------------------------------------------------
#Q8.Remove Duplicates Without Changing the Original Order
def remove_duplicates(nums):
    result=[]
    
    for num in nums:
        if num not in result:
            result.append(num)
    return result

#-----------------------------------------------------------------------
#Q9. Find the Missing Number from 1 to N
def missing_number(nums,n):
    expected_sum = n*(n+1)/2
    actual_sum = sum(nums)
    
    return int(expected_sum-actual_sum)

#------------------------------------------------------------------------
#Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] + nums[i] == target:
                return [nums[j], nums[i]]
    return []

#-------------------------------------------------------------------------
#Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    return min(nums, key=lambda num: (abs(num), -num))

#-----------------------------------------------------------------------
#Q12. Find Common Elements Between Two Lists
def common_elements(list1,list2):
    result = []
    for num in list1:
        if num in list2 and num not in result:
            result.append(num)
    return result

#-----------------------------------------------------------------------
#Q13. Rotate a List to the Right by K Positions
def rotate(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    if k == 0:
        return nums[:]

    return nums[-k:] + nums[:-k]

#-----------------------------------------------------------------------
#Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

#-----------------------------------------------------------------------
#Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_pairs(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])
                if pair not in result:
                    result.append(pair)

    result.sort(key=lambda pair: pair[0])
    return result