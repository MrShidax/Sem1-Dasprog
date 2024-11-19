class Robot:
    def __init__(self, start, grid):
        self.position = start
        self.grid = grid
        self.time = 0
        self.speed_multiplier = 1
        self.met_mechanic = False

    def move(self, direction):
        x, y = self.position
        if direction == 'R':
            new_pos = (x, y + 1)
        elif direction == 'L':
            new_pos = (x, y - 1)
        elif direction == 'D':
            new_pos = (x + 1, y)
        elif direction == 'U':
            new_pos = (x - 1, y)
        else:
            return "Invalid direction"
        
        # Handle movement
        if self.is_valid_move(new_pos):
            self.position = new_pos
            self.time += 2 // self.speed_multiplier
            return self.check_encounter(new_pos)
        else:
            return "Robot nabrak silahkan diperbaiki"
    
    def is_valid_move(self, pos):
        x, y = pos
        if x < 0 or y < 0 or x >= len(self.grid) or y >= len(self.grid[0]):
            return False
        if self.grid[x][y] == 'x' and not self.met_mechanic:
            return False
        return True
    
    def check_encounter(self, pos):
        x, y = pos
        tile = self.grid[x][y]
        if tile == 'M':
            self.met_mechanic = True
            return "Bertemu dengan mekanik siap membasmi rintangan"
        elif tile == 'E':
            self.speed_multiplier = 2
            return "Bertemu dengan electrical kecepatan roda naik menjadi 200%"
        elif tile == 'P':
            return "Hi Programmer"
        elif tile == 'O':
            self.time *= 2
            return "Bertemu dengan official diajak ngonten bareng"
        elif tile == 'F':
            return "Robot berhasil mencapai tujuan"
        return None
    
def parse_map():
    M, N = map(int, input().split())
    grid = []
    for _ in range(M):
        grid.append(list(input().strip()))
    
    # Find the start point
    start = None
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 'S':
                start = (i, j)
                break
    return grid, start

def main():
    # Input and map setup
    grid, start = parse_map()
    robot = Robot(start, grid)
    
    P = int(input())  # Number of moves
    moves = input().split()

    result = None
    for move in moves:
        result = robot.move(move)
        if result:
            print(result)
        if result == "Robot berhasil mencapai tujuan":
            break
    
    if result != "Robot berhasil mencapai tujuan":
        print("Robot gagal dalam mencapai tujuan :(")
    
    print(f"Robot telah berjalan selama {robot.time} menit")

if __name__ == "__main__":
    main()