#Q1. Find the Frequency of Each Word in a Sentence
from solutions import word_frequency
print(word_frequency("python is easy and python is powerful"))

#Additional Test Case
print(word_frequency("data analytics and data engineering"))

#------------------------------------------------------------------
#Q2. Find the Frequency of Each Character in a Word
from solutions import character_count
print(character_count("banana"))

#Additional Test Case
print(character_count("apple"))    

#--------------------------------------------------------------------
#Q3. Find the First Non-Repeating Character in a Word
from solutions import first_non_repeating
print(first_non_repeating("swiss"))

#Additional Test case
print(first_non_repeating("aabbb"))

#--------------------------------------------------------------------
#Q4. Check Whether Two Strings Are Anagrams
from solutions import anagram
print(anagram("listen","silent"))  

#Additional Test Case:
print(anagram("secure","rescue"))

#--------------------------------------------------------------------
#Q5. Find the First Repeating Character in a String
from solutions import first_repeating
print(first_repeating("programming")) 

#Additional Test Case
print(first_repeating("Advanced"))

#--------------------------------------------------------------------
#Q6. Move All Zeros to the End of a List
from solutions import list_of_numbers
print(list_of_numbers([0, 3, 0, 1, 2, 0, 4] ))

#Additional Test Case
print(list_of_numbers([0, 0, 0, 1, 2, 0, 4,8,2,0] ))

#-----------------------------------------------------------------------
#Q7. Find the Second Highest Distinct Number in a List
from solutions import second_largest_distinct_num
print(second_largest_distinct_num([10, 20, 40, 30, 40, 20]))

#Additional Test Case
print(second_largest_distinct_num([100, 200, 400, 300, 400, 200]))

#-----------------------------------------------------------------------
#Q8.Remove Duplicates Without Changing the Original Order
from solutions import remove_duplicates
print(remove_duplicates([4, 2, 4, 5, 2, 7, 5]))

#Additional Test Case
print(remove_duplicates([1,4, 1, 4, 5, 2, 6,2, 5]))

#-----------------------------------------------------------------------
#Q9. Find the Missing Number from 1 to N
from solutions import missing_number
print(missing_number([1, 2, 4, 5, 6], 6))

#Additional Test Case
print(missing_number([1, 2,3, 4, 5, 6,8,9], 9))

#------------------------------------------------------------------------
#Q10. Find Two Numbers Whose Sum Equals a Target
from solutions import two_sum
print(two_sum([2, 7, 11, 15], 9))

#Additional Test Case
print(two_sum([1, 4, 6], 20))

#-------------------------------------------------------------------------
#Q11. Find the Number Closest to Zero
from solutions import closest_to_zero
print(closest_to_zero([-8, -3, 2, 5, -2]))

#Additional Test Case
print(closest_to_zero([-4, -1, 1, 6]))

#-----------------------------------------------------------------------
#Q12. Find Common Elements Between Two Lists
from solutions import common_elements
print(common_elements([1, 2, 3, 4, 5],[3, 4, 5, 6, 7] ))

#Additional Test Case
print(common_elements([2,4,5,6],[2,4,7,8]))

#-----------------------------------------------------------------------
#Q13. Rotate a List to the Right by K Positions
from solutions import rotate
print(rotate([1, 2, 3, 4, 5], 2))

#Additional Test Case
print(rotate([11, 21, 34], 1))

#-----------------------------------------------------------------------
#Q14. Find the Maximum Sum of Two Consecutive Elements
from solutions import max_consecutive_sum
print(max_consecutive_sum([4, 7, 2, 9, 5]))

#Additional Test Case
print(max_consecutive_sum([-5, -2, -8]))

#-----------------------------------------------------------------------
#Q15. Find All Pairs of Numbers Whose Sum Equals a Target
from solutions import all_pairs
print(all_pairs([2, 4, 3, 5, 7, 8, 1], 9))

#Additional Test Case
print(all_pairs([1,1,2, 2,3, 3], 5))