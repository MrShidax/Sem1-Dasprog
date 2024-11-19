class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        prev_clr = image[sr][sc]
        if prev_clr == newColor:
            return image
        
        def dfs(img, x, y, prev_clr, new_clr):
            if img[x][y] != prev_clr:
                return
            
            img[x][y] = new_clr
            
            n = len(img)
            m = len(img[0])
            
            if x - 1 >= 0:
                dfs(img, x - 1, y, prev_clr, new_clr)
            if y + 1 < m:
                dfs(img, x, y + 1, prev_clr, new_clr)
            if x + 1 < n:
                dfs(img, x + 1, y, prev_clr, new_clr)
            if y - 1 >= 0:
                dfs(img, x, y - 1, prev_clr, new_clr)
        
        dfs(image, sr, sc, prev_clr, newColor)
        
        return image