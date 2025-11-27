import pandas as pd
import numpy as np

def generate_synthetic_data(n_samples=1000, seed=42):
    """
    Generates synthetic supply chain data for demonstration purposes.
    
    Args:
        n_samples (int): Number of samples to generate.
        seed (int): Random seed for reproducibility.
        
    Returns:
        pd.DataFrame: A DataFrame containing the synthetic data.
    """
    np.random.seed(seed)
    
    # 1. Exogenous Variables
    # Weather Shock (0: Normal, 1: Mild, 2: Severe)
    weather_shock = np.random.choice([0, 1, 2], size=n_samples, p=[0.7, 0.2, 0.1])
    
    # Port Congestion (Continuous index, influenced by weather)
    # Base congestion + weather effect + noise
    port_congestion = np.random.normal(5, 1, n_samples) + 2 * weather_shock
    
    # 2. Treatment Variable
    # Route Choice (Binary: 0=Standard, 1=Alternative)
    # Decisions are influenced by congestion (confounder)
    # Higher congestion -> Higher probability of choosing alternative route
    prob_alt_route = 1 / (1 + np.exp(-(port_congestion - 6)))
    route_choice = np.random.binomial(1, prob_alt_route, n_samples)
    
    # 3. Mediator / Intermediate Variables
    # Cargo Volume (influenced by route choice? Maybe not, usually exogenous or demand-driven)
    # Let's say Inventory Level is influenced by Route Choice (Alt route might be faster/slower)
    inventory_level = np.random.normal(100, 10, n_samples) - 5 * route_choice
    
    # 4. Outcome Variable
    # Delivery Delay (Days)
    # Influenced by: Weather, Port Congestion, Route Choice
    # Alt route reduces delay if congestion is high, but adds base time?
    # Let's model: Delay = Base + 0.5*Congestion + 2*Weather - 3*RouteChoice + Noise
    delivery_delay = 2 + 0.5 * port_congestion + 1.5 * weather_shock - 3 * route_choice + np.random.normal(0, 1, n_samples)
    
    # Ensure no negative delays
    delivery_delay = np.maximum(0, delivery_delay)
    
    data = pd.DataFrame({
        'weather_shock': weather_shock,
        'port_congestion': port_congestion,
        'route_choice': route_choice,
        'inventory_level': inventory_level,
        'delivery_delay': delivery_delay
    })
    
    return data

def load_csv_data(filepath):
    """
    Loads data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
