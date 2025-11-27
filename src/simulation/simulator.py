import pandas as pd
import numpy as np

class SupplyChainSimulator:
    """
    A class for simulating interventions in the supply chain.
    """
    
    def __init__(self, model_effect_estimates):
        """
        Initialize with estimated causal effects.
        
        Args:
            model_effect_estimates (dict): Dictionary of effect estimates.
                                           e.g., {'route_choice': -3.0, 'weather_shock': 1.5}
        """
        self.effects = model_effect_estimates
        
    def simulate_intervention(self, data: pd.DataFrame, intervention_col: str, intervention_value: float):
        """
        Simulates the effect of an intervention on the outcome.
        
        Args:
            data (pd.DataFrame): The original data.
            intervention_col (str): The column to intervene on (e.g., 'route_choice').
            intervention_value (float): The value to set the intervention column to.
            
        Returns:
            pd.DataFrame: A DataFrame with the simulated outcome.
        """
        simulated_data = data.copy()
        
        # 1. Apply Intervention
        original_values = simulated_data[intervention_col].copy()
        simulated_data[intervention_col] = intervention_value
        
        # 2. Propagate Effect to Outcome (Simple Linear Approximation)
        # Outcome_new = Outcome_old + Effect * (New_Value - Old_Value)
        if intervention_col in self.effects:
            effect = self.effects[intervention_col]
            delta = intervention_value - original_values
            
            # Assuming 'delivery_delay' is the outcome
            if 'delivery_delay' in simulated_data.columns:
                simulated_data['delivery_delay'] += effect * delta
                # Ensure no negative delays
                simulated_data['delivery_delay'] = np.maximum(0, simulated_data['delivery_delay'])
        else:
            print(f"Warning: No effect estimate found for {intervention_col}. Outcome will not change.")
            
        return simulated_data
    
    def compare_scenarios(self, data: pd.DataFrame, scenarios: list):
        """
        Compares multiple intervention scenarios.
        
        Args:
            data (pd.DataFrame): Baseline data.
            scenarios (list): List of dicts, e.g., [{'name': 'Baseline', 'col': None, 'val': None}, 
                                                    {'name': 'All Alt Route', 'col': 'route_choice', 'val': 1}]
                                                    
        Returns:
            pd.DataFrame: Summary of outcomes for each scenario.
        """
        results = []
        
        for scenario in scenarios:
            name = scenario['name']
            col = scenario.get('col')
            val = scenario.get('val')
            
            if col is not None:
                sim_data = self.simulate_intervention(data, col, val)
            else:
                sim_data = data
                
            avg_delay = sim_data['delivery_delay'].mean()
            results.append({'Scenario': name, 'Avg Delivery Delay': avg_delay})
            
        return pd.DataFrame(results)
