class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # base case for empty string
        if s == '':
            return 0
        # get length and list
        str_arr = list(s)
        str_len = len(str_arr)
        # base case of length 1
        if str_len == 1:
            return 1
        
        largest_len = 0
        for i in range(0,str_len):
            
            #set default params
            largest_temp = 1
            unique_set = set(str_arr[i])
            
            #iterate over next elems
            for j in range(i+1, str_len):
                
                if str_arr[j] in unique_set:
                    break
                else:
                    largest_temp +=1
                    unique_set.add(str_arr[j])
            
            if largest_temp > largest_len:
                largest_len = largest_temp
            unique_set.clear()
        
        return largest_len
        
        