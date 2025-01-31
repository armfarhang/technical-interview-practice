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
        print("Displaying the graph:")
        while edge != None:
            print("node:", node.data)
            print("     Edges:", edge.modifier)
            node = edge.dest
            edge = node.next_edge
        print("Final node:", node.data)

    def topdown_fill_nodes(self):
        def topdown_modify(input_list, modifier):
            '''
            modifies the input list of shapes based on the modifier tuple
            :param input_list:
            :param modifier:
            :return:
            '''
            output_list = []
            for i in modifier:
                output_list.append(input_list[i - 1])
            return output_list

        node = self.root_node
        edge = node.next_edge
        while edge != None:
            next_node = edge.dest
            input_shapes = node.data
            modifier = edge.modifier
            if next_node.data == None and (isinstance(modifier, tuple)):
                #if next node is empty and modifier is a tuple fill the data for the next node
                output_shapes = []
                for i in modifier:
                    output_shapes.append(input_shapes[i - 1])
                next_node.data = output_shapes
            if next_node.data != None and node.data != None and (isinstance(modifier, list)):
                #if current node and next node are not empty and modifier is a list,
                # search through the modifier list to find the modifier that will transform the current node data to the next node data
                for i in modifier:
                    output = topdown_modify(node.data, i)
                    if output==next_node.data:
                        edge.modifier = i
                        break


            node = next_node
            edge = node.next_edge
        print("Top Down Node Filling Complete")




def topdown_transform_list_by_modifier(input_list, modifierlist):
    output_list = []
    for i in modifierlist:
        output_list.append(input_list[i-1])
    return output_list
def buttomup_transform_list_by_modifier(output_list, modifierlist):
    input_list = [None] * len(output_list)
    #interate over index and value of modiferlist
    for i, val in enumerate(modifierlist):
        input_list[val-1] = output_list[i]
    return input_list

# def search_topdown(stage_dict, stage_count):
#     stage_dict = stage_dict
#     input_list = None
#     output_list = None
#     for key, value in stage_dict.items():
#         if key == "input":
#             input_list = value
#         elif key == "output":
#             output_list = value
#         else:
#             for i in range(stage_count):
#                 if key == f"stage{i+1}":
#                     if isinstance(value, tuple):
#                         stage_dict[key] = {"modifier": value,
#                                            "modified_val": topdown_transform_list_by_modifier(input_list, value)}()
#                     elif isinstance(value, list):
#                         break
#
#
#
#
#         if isinstance(value, tuple):
#             input_list = topdown_transform_list_by_modifier(input_list, value)
#         elif isinstance(value, list):
#             for i in value:
#                 input_list = topdown_transform_list_by_modifier(input_list, i)
def generate_arrays(length):
    return list(permutations(range(1, length + 1)))

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

# if __name__ == '__main__':
#     input_list = ["cross", "square", "triangle", "circle"]
#     output_list = ["triangle", "cross", "circle", "square"]
#     permut_list = generate_arrays(len(input_list))
#     stage_dict = {"stage1": permut_list, "stage2": permut_list}
#
#     # prompt_master(input_list, output_list)
#     output = topdown_transform_list_by_modifier(input_list, [2, 1, 4, 3])
#     input = buttomup_transform_list_by_modifier(output, [2, 1, 4, 3])
#     print(f"topdown output: {output}")
#     print(f"buttom up input: {input}")

if __name__ == "__main__":
    node1 = Node(["cross", "square", "triangle", "circle"], None, None)
    node2 = Node(None, None, None)
    node3 = Node(None, None, None)
    final_node = Node(["triangle", "cross", "circle", "square"], None, None)

    edge1 = Edge(node1, node2, None)
    edge2 = Edge(node2, node3, [(2,3,4,1), (2,3,1,4)])
    edge3 = Edge(node3, final_node, (1,2,4,3))
    node1.next_edge = edge1
    node2.prev_edge = edge1
    node2.next_edge = edge2
    final_node.prev_edge = edge2


    graph = Graph(node1)
    graph.display_graph()
    graph.topdown_fill_nodes()
    graph.display_graph()



