class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        dpa,dpb=0,0
        for a,b in zip(energyDrinkA,energyDrinkB):
            dpa,dpb=max(dpb,dpa+a),max(dpa,dpb+b)

        return max(dpa,dpb)