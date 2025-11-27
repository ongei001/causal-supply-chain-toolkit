import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

class CausalDiscovery:
    """
    A class for discovering causal structures from supply chain data.
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize with a pandas DataFrame.
        """
        self.data = data
        self.graph = None
        
    def learn_graph(self, method='heuristic', threshold=0.3):
        """
        Learns the causal graph structure.
        
        Args:
            method (str): 'heuristic' (correlation-based) or 'pc' (placeholder for PC algorithm).
            threshold (float): Correlation threshold for heuristic method.
            
        Returns:
            nx.DiGraph: A directed graph representing causal relationships.
        """
        if method == 'heuristic':
            self.graph = self._learn_heuristic(threshold)
        else:
            raise NotImplementedError(f"Method {method} not implemented yet.")
            
        return self.graph
    
    def _learn_heuristic(self, threshold):
        """
        A simple heuristic method based on correlation and domain knowledge constraints.
        Note: Real causal discovery requires conditional independence tests (e.g., PC algorithm).
        """
        corr_matrix = self.data.corr().abs()
        G = nx.DiGraph()
        G.add_nodes_from(self.data.columns)
        
        # Add edges based on correlation threshold
        for i, col1 in enumerate(self.data.columns):
            for j, col2 in enumerate(self.data.columns):
                if i != j and corr_matrix.iloc[i, j] > threshold:
                    # Apply simple domain constraints to orient edges (Time/Logic)
                    # Example: Weather -> Congestion (Weather causes Congestion, not vice versa)
                    if 'weather' in col1 and 'congestion' in col2:
                        G.add_edge(col1, col2)
                    # Example: Congestion -> Delay
                    elif 'congestion' in col1 and 'delay' in col2:
                        G.add_edge(col1, col2)
                    # Example: Route Choice -> Delay
                    elif 'route' in col1 and 'delay' in col2:
                        G.add_edge(col1, col2)
                    # Example: Weather -> Delay
                    elif 'weather' in col1 and 'delay' in col2:
                        G.add_edge(col1, col2)
                    # Example: Congestion -> Route Choice (Reverse causality/Confounding)
                    elif 'congestion' in col1 and 'route' in col2:
                        G.add_edge(col1, col2)
                        
        return G

    def plot_graph(self):
        """
        Visualizes the learned causal graph.
        """
        if self.graph is None:
            print("Graph not learned yet. Call learn_graph() first.")
            return
            
        pos = nx.spring_layout(self.graph, seed=42)
        plt.figure(figsize=(10, 6))
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', 
                node_size=2000, arrowsize=20, font_size=12)
        plt.title("Causal Graph")
        plt.show()
