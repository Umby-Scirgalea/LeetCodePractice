def maximumHappinessSum(happiness, k: int) -> int:
        maxHappinessSum = 0
        happinessSort = sorted(happiness,reverse=True)
        subVal = 0
        for i in range(k):
            if happinessSort[i] - subVal> 0:
                maxHappinessSum += happinessSort[i] - subVal
            
            subVal+=1
            
        return maxHappinessSum

