import heapq

class MovieRentingSystem(object):
    def __init__(self, n, entries):
        self.price = {}
        self.available = {}
        self.rented = []
        self.available_set = set()
        self.rented_set = set()
        for shop, movie, price in entries:
            self.price[(shop, movie)] = price
            if movie not in self.available:
                self.available[movie] = []
            heapq.heappush(self.available[movie], (price, shop))
            self.available_set.add((shop, movie))

    def search(self, movie):
        res = []
        if movie not in self.available:
            return res
        temp = []
        seen_shops = set()
        while self.available[movie] and len(res) < 5:
            price, shop = heapq.heappop(self.available[movie])
            if (shop, movie) in self.available_set and shop not in seen_shops:
                res.append(shop)
                temp.append((price, shop))
                seen_shops.add(shop)
        for item in temp:
            heapq.heappush(self.available[movie], item)
        return res

    def rent(self, shop, movie):
        price = self.price[(shop, movie)]
        self.available_set.discard((shop, movie))
        self.rented_set.add((shop, movie))
        heapq.heappush(self.rented, (price, shop, movie))

    def drop(self, shop, movie):
        price = self.price[(shop, movie)]
        self.rented_set.discard((shop, movie))
        self.available_set.add((shop, movie))
        heapq.heappush(self.available[movie], (price, shop))

    def report(self):
        res = []
        temp = []
        seen = set()
        while self.rented and len(res) < 5:
            price, shop, movie = heapq.heappop(self.rented)
            if (shop, movie) in self.rented_set and (shop, movie) not in seen:
                res.append([shop, movie])
                temp.append((price, shop, movie))
                seen.add((shop, movie))
        for item in temp:
            heapq.heappush(self.rented, item)
        return res
