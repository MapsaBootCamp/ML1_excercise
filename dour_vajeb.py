import typing


class Graph:

    def __init__(self):
        self.nodes: typing.Dict[str, set[str]] = {}

    def get_graph(self):
        number_of_edges = int(input().split()[1])
        input_list = [input() for _ in range(number_of_edges)]
        for line in input_list:
            self.add_edge_and_node(*line.split())

    def add_edge_and_node(self, source: str, sink: str):
        if source not in self.nodes:
            self.nodes[source] = set()
        if sink not in self.nodes:
            self.nodes[sink] = set()
        self.nodes[source].add(sink)
        self.nodes[sink].add(source)

    @staticmethod
    def _singles_nodes(in_nodes: typing.Dict[str, set[str]]):
        branches: typing.Dict[str, set[str]] = {}
        for root, leaves in in_nodes.items():
            if len(leaves) == 1:
                branches.setdefault(leaves.pop(), set()).add(root)
        return branches

    def nodes_analyser(self):
        branches = self._singles_nodes(self.nodes)
        heads = set(branches.keys())
        pipe = heads.copy()
        while pipe:
            root = pipe.pop()
            leaves = branches[root]
            a = self.nodes[root] - leaves
            b = a - heads
            if len(a) == 1 and len(b) == 0:
                del branches[root]
                pipe.update(a)
                branches.setdefault(a.pop(), set()).add(root)
        self._dead_ends = branches
        return True

    def dead_ends(self):
        n = sum(len(item) for item in self._dead_ends.values())
        print(f'{n}')
        for root in sorted(self._dead_ends.keys()):
            for leaf in sorted(self._dead_ends[root]):
                print(root, leaf)


if __name__ == '__main__':
    base = Graph()
    # base.get_graph()
    # base.nodes = {'1': {'3', '6', '2', '5'}, '2': {'3', '1'}, '3': {'4', '2', '1'}, '4': {'3'}, '5': {'1'},
    #               '6': {'8', '7', '1'}, '7': {'6'}, '8': {'6'}}
    base.nodes = {'1': {'4', '3', '2'}, '2': {'1', '3'}, '3': {'1', '2'}, '4': {'1', '6', '5'}, '5': {'4', '6'}, '6': {'4', '5'}}
    if base.nodes_analyser():
        base.dead_ends()
    # print('0')
