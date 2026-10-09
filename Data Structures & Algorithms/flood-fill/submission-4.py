class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()

        row = len(image)
        col = len(image[0])

        stack = [(sr, sc)]
        visited.add(stack[0])

        start_color = image[sr][sc]

        while stack:
            c = stack.pop()

            visited.add(c)

            

            if image[c[0]][c[1]] == start_color :
                image[c[0]][c[1]] = color
            
            neighbors = [(c[0], c[1] - 1), (c[0], c[1] + 1), (c[0] - 1, c[1]), (c[0] + 1, c[1])] # UP DOWN RIGHT LEFT

            for coords in neighbors:
                if 0 <= coords[0] < row and 0 <= coords[1] < col and coords not in visited and image[coords[0]][coords[1]] == start_color:
                    stack.append(coords)
            
        return image
            





        