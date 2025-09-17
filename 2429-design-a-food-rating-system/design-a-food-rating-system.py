import heapq

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_to_heap:
                self.cuisine_to_heap[c] = []
            heapq.heappush(self.cuisine_to_heap[c], (-r, f))

    def changeRating(self, food, newRating):
        self.food_to_rating[food] = newRating
        c = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_heap[c], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_to_heap[cuisine]
        while heap:
            rating, f = heap[0]
            if -rating == self.food_to_rating[f]:
                return f
            heapq.heappop(heap)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)