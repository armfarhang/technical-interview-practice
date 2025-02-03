from icecream import ic
from itertools import permutations

class Node:
    """A class to represent a single node in a linked list."""
    def __init__(self, data, prev_edge, next_edge):
        self.data = data  # Data stored in the node
        self.prev_edge = prev_edge  # Pointer to the previous edge
        self.next_edge = next_edge  # Pointer to the next edge


class Edge:
    """A class to represent an edge in a graph."""
    def __init__(self, src_node, dest_node, modifier):
        self.modifier = modifier  # Weight of the edge
        self.src = src_node  # Source vertex
        self.dest = dest_node  # Destination vertex

class Graph:
    """A class to represent a graph using linked nodes."""
    def __init__(self, root_node):
        self.root_node = root_node

    def set_root_node(self, data):
        """Set the root node of the graph."""
        if self.root_node == None:
            self.root_node = Node(data)

    def insert_edge(self, src_data, dest_data, modifier):
        """Insert an edge between two nodes."""
        src_node = self.find_node(src_data)
        dest_node = self.find_node(dest_data)
        if src_node and dest_node:
            new_edge = Edge(src_node, dest_node, modifier)
            src_node.prev_edge = new_edge

    def display_graph(self):
        node = self.root_node
        edge = node.next_edge
        output_print = "Displaying the graph:\n"
        while edge != None:
            output_print += f"node: {node.data}\n"
            output_print += f"     Edges: {edge.modifier}\n"
            node = edge.dest
            edge = node.next_edge
        output_print += f"Final node: {node.data}\n"
        return output_print


    def topdown_fill_nodes(self):
        def in_out_find_mod(src_data, dest_data): #given the inpt and output shapes/strings find the modifier betwee them
            modifier = [None] * len(src_data)
            for i in src_data:
                    modifier[dest_data.index(i)] = src_data.index(i)+1
            return tuple(modifier)
        def in_mod_find_out(src_data, modifier): #given the input shapes and the modifier find the output shapes
            output_list = []
            for i in modifier:
                output_list.append(src_data[i - 1])
            return output_list
        def out_mod_find_in(output_list, modifier): #given the output shapes and the modifier find the input shapes
            input_list = [None] * len(modifier)
            for i, val in enumerate(modifier):
                input_list[val - 1] = output_list[i]
            return input_list
        def one_pass(root_node):
            current_node = self.root_node
            between_edge = current_node.next_edge
            next_node = between_edge.dest
            remain_nodes = []
            while current_node.next_edge != None:
                between_edge = current_node.next_edge
                next_node = between_edge.dest
                input_shapes = current_node.data
                modifier = between_edge.modifier
                #if input shape data exist and modifer is a tuple --->  calculate the next node data
                if input_shapes != None: #if we have input
                    if next_node.data != None:
                        current_node.next_edge.modifier = in_out_find_mod(input_shapes, next_node.data)
                        current_node = next_node
                        # if modifier != None:
                        #     if isinstance(modifier, list): #if we have modifier options
                        #         for i in modifier:
                        #             modifier = in_out_find_mod(input_shapes, next_node.data)
                        #             if i==modifier:
                        #                 current_node.next_edge.modifier = i
                        #                 current_node = next_node
                        #                 break
                            # else:
                            #     current_node.next_edge.modifier = in_out_find_mod(input_shapes, next_node.data)
                            #     current_node = next_node
                        # else:
                        #     current_node.next_edge.modifier = in_out_find_mod(input_shapes, next_node.data)
                        #     current_node = next_node

                    else:
                        if isinstance(modifier, tuple):  # if we have 1 modifier
                            output_shapes = in_mod_find_out(input_shapes, modifier)
                            next_node.data = output_shapes
                        else:
                            remain_nodes.append(next_node)
                            current_node = next_node

                else:
                    if next_node.data !=None:
                        if isinstance(modifier, tuple):
                            input_shapes = out_mod_find_in(next_node.data, modifier)
                            current_node.data = input_shapes
                            current_node = next_node

                        else:
                            remain_nodes.append(current_node)
                            current_node = next_node

                    else:
                        remain_nodes.append(current_node)
                        remain_nodes.append(next_node)
                        current_node = next_node
            return remain_nodes

        remain_nodes = one_pass(self.root_node)
        while remain_nodes != []:
            node = remain_nodes.pop()
            for i in one_pass(node):
                remain_nodes.append(i)




        print("Top Down Node Filling Complete")


def generate_arrays(length):
    return list(permutations(range(1, length + 1)))
def connect_nodes(src_node, edge,dest_node):
    src_node.next_edge = edge
    dest_node.prev_edge = edge
    edge.src = src_node
    edge.dest = dest_node
def prompt_master(input_list, output_list):
    stage_dict = {}
    stage_dict["input"] = input_list
    stage_dict["output"] = output_list
    stage_count = int(input("how many stages are there? "))
    input_list = input_list
    output_list = output_list

    for i in range(stage_count):
        stage_modifer = input(f"enter the modifier for stage {str(i+1)}:")
        if stage_modifer == "":
            stage_dict[f"stage{i + 1}"] = ()
        else:
            split_comma = stage_modifer.split(",")
            split_space = [tuple(map(int, i.split(" "))) for i in split_comma]
            stage_modifer_list = split_space
            stage_dict[f"stage{i + 1}"] = stage_modifer_list

    for key, value in stage_dict.items():
        #if value is a tuple
        if isinstance(value, tuple):
            input_list = topdown_transform_list_by_modifier(input_list, value)
        elif isinstance(value, list):
            for i in value:
                input_list = topdown_transform_list_by_modifier(input_list, i)


if __name__ == "__main__":
    node1 = Node(None, None, None)

    edge1 = Edge(None, None, (2, 3, 4, 1))
    node2 = Node(['triangle', 'circle', 'cross', 'square'], None, None)

    edge2 = Edge(None, None, [(3, 4, 1, 2), (4, 2, 1, 3)])
    node3 = Node(['circle', 'cross', 'square', 'triangle'], None, None)

    edge3 = Edge(None, None, (4, 2, 1, 3))
    final_node = Node(['triangle', 'cross', 'circle', 'square'], None, None)

    connect_nodes(node1, edge1, node2)
    connect_nodes(node2, edge2, node3)
    connect_nodes(node3, edge3, final_node)

    graph = Graph(node1)
    graph.topdown_fill_nodes()

    display_graph = graph.display_graph()


    print(display_graph)

