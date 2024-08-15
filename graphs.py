import pygraphviz as pgv

class ControlFlowGraph:

    def __init__(self):
        self.graph = pgv.AGraph(directed=True)

    def while_loop(self):
        # Adiciona nós e arestas para representar o loop while
        self.graph.add_node("InicioLoop", shape="box")
        self.graph.add_node("FimLoop", shape="box")
        self.graph.add_node("Condicao", shape="diamond")

        # Adiciona arestas para conectar os nós
        self.graph.add_edge("InicioLoop", "Condicao")
        self.graph.add_edge("Condicao", "FimLoop")
        self.graph.add_edge("Condicao", "InicioLoop")  # Aresta para o loop

    def visualizar(self):
        # Salva e exibe o gráfico
        self.graph.draw("control_flow_graph.png", prog="dot", format="png")
        self.graph.display()


# Exemplo de uso
if __name__ == "__main__":
    cfg = ControlFlowGraph()
    cfg.while_loop()
    cfg.visualizar()
