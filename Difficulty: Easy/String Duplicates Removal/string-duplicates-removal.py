#User function Template for python3
class Solution:

	
	def removeDuplicates(self, s):
	    result = ""
	    for char in s:
	        if char not in result:
	            result += char
	    return result
	            