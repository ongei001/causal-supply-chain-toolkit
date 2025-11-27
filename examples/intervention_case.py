"""
Example: Intervention Case
==========================

This script demonstrates how to use the Causal Supply Chain Toolkit to estimate
the effect of a logistics intervention.
"""

import pandas as pd
import numpy as np
# In a real scenario, you would import from your package:
# from causal_toolkit import CausalModel

def generate_mock_data(n=1000):
    """Generates mock supply chain data."""
    np.random.seed(42)
    # Confounder: Shipment Weight
    weight = np.random.normal(10, 2, n)
    
    # Treatment: Expedited Shipping (binary)
    # Heavier packages are less likely to be expedited
    prob_expedited = 1 / (1 + np.exp(weight - 10))
    expedited = np.random.binomial(1, prob_expedited, n)
    
    # Outcome: Delivery Delay (days)
    # Expedited shipping reduces delay, weight increases it
    delay = 5 + 0.5 * weight - 2 * expedited + np.random.normal(0, 1, n)
    
    return pd.DataFrame({
        'weight': weight,
        'expedited_shipping': expedited,
        'delivery_delay': delay
    })

def main():
    print("Generating mock data...")
    df = generate_mock_data()
    print(df.head())
    
    print("\nCalculating naive effect (difference in means)...")
    naive_effect = df[df['expedited_shipping'] == 1]['delivery_delay'].mean() - \
                   df[df['expedited_shipping'] == 0]['delivery_delay'].mean()
    print(f"Naive effect: {naive_effect:.2f} days")
    
    print("\n(Note: This is a placeholder. Real causal inference would adjust for confounders like weight.)")

if __name__ == "__main__":
    main()
