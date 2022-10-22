class Solution:

    
    def minWindow(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def found_target(target_len):
            return target_len == 0
        
        target_letter_counts = collections.Counter(t)
        start = 0
        end = 0
        min_window = ""
        target_len = len(t)        
        
        for end in range(len(s)):
			# If we see a target letter, decrease the total target letter count
            if target_letter_counts[s[end]] > 0:
                target_len -= 1
            target_letter_counts[s[end]] -= 1
            
			# If all letters in the target are found:
            while found_target(target_len):
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
					# Note the new minimum window
                    min_window = s[start : end + 1]
                    
				# Increase the letter count of the current letter
                target_letter_counts[s[start]] += 1
                
				# If all target letters have been seen and now, a target letter is seen with count > 0
				# Increase the target length to be found. This will break out of the loop
                if target_letter_counts[s[start]] > 0:
                    target_len += 1
                    
                start+=1
                
        return min_window