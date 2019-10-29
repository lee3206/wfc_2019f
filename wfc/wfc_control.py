from wfc_tiles import make_tile_catalog
from wfc_patterns import make_pattern_catalog
from wfc_adjacency import adjacency_extraction
from wfc_solver import run, makeWave, makeAdj, lexicalLocationHeuristic, lexicalPatternHeuristic
import imageio
import numpy as np

filename = "images/samples/Red Maze.png"
img = imageio.imread(filename)
tile_size = 1
pattern_width = 2
rotations = 0
output_size = [16, 16]
ground = None

# TODO: generalize this to more than the four cardinal directions
direction_offsets = list(enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]))

tile_catalog, tile_grid, code_list, unique_tiles = make_tile_catalog(img, tile_size)
pattern_catalog, pattern_weights, pattern_list, pattern_grid = make_pattern_catalog(tile_grid, pattern_width, rotations)
adjacency_relations = adjacency_extraction(pattern_grid, pattern_catalog, direction_offsets)

number_of_patterns = len(pattern_weights)
encode_patterns = dict(enumerate(pattern_list))
decode_patterns = {x: i for i, x in enumerate(pattern_list)}
decode_directions = {j:i for i,j in direction_offsets}

adjacency_list = {}
for i,d in direction_offsets:
    adjacency_list[d] = [set() for i in pattern_weights]
print(adjacency_list)
for i in adjacency_relations:
    print(i)
    print(decode_patterns[i[1]])
    adjacency_list[i[0]][decode_patterns[i[1]]].add(decode_patterns[i[2]])
        

# len(direction_offsets)
# print(dict(direction_offsets))
# print({j:i for i,j in direction_offsets})


# print(encode_patterns)
# print(decode_patterns)
# print(adjacency_list)

wave = makeWave(number_of_patterns, output_size[0], output_size[1])
adjacency_matrix = makeAdj(adjacency_list)

print(adjacency_matrix)

solution = run(wave.copy(),
               adjacency_matrix,
               locationHeuristic=lexicalLocationHeuristic,
               patternHeuristic=lexicalPatternHeuristic,
               periodic=True,
               backtracking=False,
               onChoice=None,
               onBacktrack=None)

print(solution)
               
               


def wfc_execute():
    #wave = wfc.wfc_solver.makeWave(3, 3, 4)
    #adjLists = {}
    #adjLists[(+1, 0)] = adjLists[(-1, 0)] = adjLists[(0, +1)] = adjLists[(0, -1)] = [[1], [0], [2]]
    #adjacencies = wfc.wfc_solver.makeAdj(adjLists)

    #result = run(wave,
    #             adjacencies,
    #             locationHeuristic=wfc.wfc_solver.lexicalLocationHeuristic,
    #             patternHeuristic=wfc.wfc_solver.lexicalPatternHeuristic,
    #             periodic=False)
    #print(result)

    import imageio
    filename = "images/samples/Red Maze.png"
    img = imageio.imread(filename)




