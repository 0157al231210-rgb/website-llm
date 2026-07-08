from collections import deque

class URLFrontier:
    def __init__(self):
        self.queue = deque()
        self.enqueued = set()
    
    def add(self,url,depth):
        
        if url in self.enqueued:
            return
        
        self.queue.append((url,depth))
        self.enqueued.add(url)
        
    def get(self):
        
        url, depth = self.queue.popleft()
        self.enqueued.remove(url)
        return url, depth
    
    def is_empty(self):
        return len(self.queue) == 0