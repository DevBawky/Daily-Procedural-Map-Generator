import random
from datetime import datetime

WIDTH = 40
HEIGHT = 15
WALL = '⬛'
FLOOR = '⬜'
FILL_PROBABILITY = 0.45

def initialize_map():
    return [[WALL if random.random() < FILL_PROBABILITY else FLOOR 
             for _ in range(WIDTH)] for _ in range(HEIGHT)]

def count_walls(map_data, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx, ny = x + i, y + j
            if i == 0 and j == 0:
                continue
            if nx < 0 or ny < 0 or nx >= WIDTH or ny >= HEIGHT:
                count += 1
            elif map_data[ny][nx] == WALL:
                count += 1
    return count

def smooth_map(map_data):
    new_map = [[FLOOR for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_walls(map_data, x, y)
            if neighbors > 4:
                new_map[y][x] = WALL
            elif neighbors < 4:
                new_map[y][x] = FLOOR
            else:
                new_map[y][x] = map_data[y][x]
    return new_map

def map_to_string(map_data):
    return '\n'.join([''.join(row) for row in map_data])

def update_readme(map_str):
    readme_path = "README.md"

    start_marker = "<" + "!-- DAILY_MAP_START --" + ">"
    end_marker = "<" + "!-- DAILY_MAP_END --" + ">"
    
    date_str = datetime.now().strftime('%Y/%m/%d')
    new_content = f"{start_marker}\n### Today's Generated Map ({date_str})\n```\n{map_str}\n```\n_By DevBawky_\n{end_marker}"

    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if start_marker in content and end_marker in content:
            pre = content.split(start_marker)[0]
            post = content.split(end_marker)[1]
            final_content = pre + new_content + post
        else:
            final_content = content + "\n" + new_content

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(final_content)
            
    except FileNotFoundError:
        print("README.md not found. Creating new one.")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)

if __name__ == "__main__":
    dungeon = initialize_map()
    
    for _ in range(5):
        dungeon = smooth_map(dungeon)
        
    map_str = map_to_string(dungeon)
    update_readme(map_str)
    print("Daily map generated")