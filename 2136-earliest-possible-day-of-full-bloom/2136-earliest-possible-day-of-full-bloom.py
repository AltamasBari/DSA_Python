class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant = []
        n = len(plantTime)
        for i in range(n):
            plant.append([plantTime[i],growTime[i]])
        
        cur_plant_time = 0
        result = 0
        plant.sort(key=lambda x: -x[1])
        for i in range(n):
            cur_plant_time += plant[i][0]
            result = max(result, cur_plant_time + plant[i][1])
        return result
