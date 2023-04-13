def knight_tour(chess_board_size, pos_x, pos_y, moves = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)], visited_count = 1):
    if chess_board_size%2!=0 and (pos_x+pos_y)%2!=0:
        return "knight tour not found"
    #initial maps
    degree_map = [[len([[x, y] for x,y in moves if i+x >= 0 and i+x < chess_board_size and j+y >= 0 and j+y < chess_board_size]) for i in range(chess_board_size)] for j in range(chess_board_size)]
    visited_map = [[0 for i in range(chess_board_size)] for j in range(chess_board_size)]
    def check_within_board_or_not_visited(pos_x, pos_y, move_x, move_y):
        return True if (pos_x+move_x<chess_board_size and pos_y+move_y<chess_board_size) and (pos_x+move_x>=0 and os_y+move_y>=0) and visited_map[pos_x+move_x][pos_y+move_y]==0 else False
    def find_possible_steps(pos_x, pos_y, moves, degree_map, visited_map):
        return [(pos_x+move_x, pos_y+move_y)  for move_x, move_y in moves if check_within_board_or_not_visited(pos_x, pos_y, move_x, move_y)]
    def reduce_degree(possible_steps):
        for new_x, new_y in possible_steps:
            degree_map[new_x][new_y] = degree_map[new_x][new_y]-1 
    # fist point condition update
    visited_map[pos_x][pos_y] = visited_count           
    reduce_degree(find_possible_steps(pos_x, pos_y, moves, degree_map, visited_map))      
    while visited_count != chess_board_size*chess_board_size:
        visited_count+=1
        possible_steps = find_possible_steps(pos_x, pos_y, moves, degree_map, visited_map)
        min_index = [degree_map[new_x][new_y] for new_x, new_y in possible_steps].index(min([degree_map[new_x][new_y] for new_x, new_y in possible_steps]))
        pos_x, pos_y = possible_steps[min_index][0], possible_steps[min_index][1]
        visited_map[pos_x][pos_y] = visited_count
        reduce_degree(possible_steps) 
    return visited_map