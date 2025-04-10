import random

# Define the terrain types
TERRAIN_TYPES = ['fields', 'forests', 'lakes', 'mountains']

# Create a class for a Tile
class Tile:
    def __init__(self, terrain1, terrain2, crowns):
        self.terrain1 = terrain1
        self.terrain2 = terrain2
        self.crowns = crowns

    def __str__(self):
        return f"{self.terrain1}/{self.terrain2} (Crowns: {self.crowns})"

# Create a class for a Player
class Player:
    def __init__(self, name):
        self.name = name
        self.kingdom = []
        self.score = 0

    def add_tile(self, tile):
        self.kingdom.append(tile)

    def calculate_score(self):
        # Simple scoring: count tiles and crowns
        score = 0
        for tile in self.kingdom:
            score += tile.crowns  # Add crowns for scoring
        self.score = score

# Create a function to generate tiles
def generate_tiles(num_tiles):
    tiles = []
    for _ in range(num_tiles):
        terrain1 = random.choice(TERRAIN_TYPES)
        terrain2 = random.choice(TERRAIN_TYPES)
        crowns = random.randint(0, 3)  # Random crowns between 0 and 3
        tiles.append(Tile(terrain1, terrain2, crowns))
    return tiles

# Main game function
def play_game(num_players, num_tiles):
    players = [Player(f"Player {i + 1}") for i in range(num_players)]
    tiles = generate_tiles(num_tiles)

    # Game loop
    for round in range(num_tiles):
        print(f"\nRound {round + 1}:")
        for player in players:
            print(f"{player.name}'s turn. Available tiles:")
            for i, tile in enumerate(tiles):
                print(f"{i + 1}: {tile}")

            choice = int(input(f"Choose a tile (1-{len(tiles)}): ")) - 1
            player.add_tile(tiles.pop(choice))  # Remove the tile from available tiles

    # Calculate scores
    for player in players:
        player.calculate_score()
        print(f"{player.name}'s score: {player.score}")

# Example usage
if __name__ == "__main__":
    num_players = int(input("Enter number of players: "))
    num_tiles = 12  # Total number of tiles to be drawn
    play_game(num_players, num_tiles)