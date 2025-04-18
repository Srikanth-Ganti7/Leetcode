class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        output = []
        a = 0
        b = 0

        while a < len(nums1) and b < len(nums2):
            if nums1[a][0] == nums2[b][0]:
                output.append([nums1[a][0], (nums1[a][1] + nums2[b][1])])
                a += 1
                b += 1
            
            elif nums1[a][0] < nums2[b][0]:
                output.append([nums1[a][0], nums1[a][1]])
                a += 1
            
            elif nums1[a][0] > nums2[b][0]:
                output.append([nums2[b][0], nums2[b][1]])
                b+= 1
        
        while b < len(nums2):
            output.append([nums2[b][0], nums2[b][1]])
            b+=1
        
        while a < len(nums1):
            output.append([nums1[a][0], nums1[a][1]])
            a+=1
        
        print(output)
        return output

            
             
        