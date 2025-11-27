import dowhy
from dowhy import CausalModel
import pandas as pd

class EffectEstimator:
    """
    A class for estimating causal effects using DoWhy.
    """
    
    def __init__(self, data: pd.DataFrame, graph_dot: str = None):
        """
        Initialize with data and optional graph (in DOT format).
        If graph is not provided, it will be inferred or assumed.
        """
        self.data = data
        self.graph_dot = graph_dot
        self.model = None
        
    def estimate_effect(self, treatment, outcome, common_causes=None, method_name="backdoor.linear_regression"):
        """
        Estimates the causal effect of treatment on outcome.
        
        Args:
            treatment (str): Name of the treatment variable.
            outcome (str): Name of the outcome variable.
            common_causes (list): List of confounders.
            method_name (str): Estimation method (e.g., "backdoor.linear_regression", "backdoor.propensity_score_matching").
            
        Returns:
            CausalEstimate: The estimated effect.
        """
        # 1. Define Causal Model
        self.model = CausalModel(
            data=self.data,
            treatment=treatment,
            outcome=outcome,
            common_causes=common_causes,
            graph=self.graph_dot
        )
        
        # 2. Identify Effect
        identified_estimand = self.model.identify_effect(proceed_when_unidentifiable=True)
        print("Identified Estimand:", identified_estimand)
        
        # 3. Estimate Effect
        estimate = self.model.estimate_effect(
            identified_estimand,
            method_name=method_name
        )
        
        return estimate
    
    def refute_estimate(self, estimate, method_name="random_common_cause"):
        """
        Refutes the estimated effect to check robustness.
        
        Args:
            estimate (CausalEstimate): The estimate to refute.
            method_name (str): Refutation method (e.g., "random_common_cause", "placebo_treatment_refuter").
            
        Returns:
            RefuteResult: The result of the refutation test.
        """
        refutation = self.model.refute_estimate(
            estimate.identified_estimand,
            estimate,
            method_name=method_name
        )
        
        return refutation
