# Causal Supply Chain Toolkit

A Python toolkit for causal inference methods for evaluating logistics interventions in supply chains.

## Overview

Global supply chains are under increasing strain from climate change and geopolitical shocks. Traditional machine learning models often fail to answer "what-if" questions about interventions. This toolkit fills that gap by providing a pipeline for **Causal Supply Chain Analysis**.

It allows you to:
1.  **Ingest** supply chain data (shipments, weather, congestion).
2.  **Discover** causal relationships (e.g., Does weather cause congestion, or is it just correlated?).
3.  **Estimate** the true effect of interventions (e.g., How much does rerouting reduce delay?).
4.  **Simulate** scenarios to optimize decisions under risk.

## Features

-   **Data Loading**: Utilities for synthetic data generation and CSV loading.
-   **Causal Discovery**: Heuristic and algorithm-based graph learning.
-   **Effect Estimation**: Wrappers around `DoWhy` for robust causal inference.
-   **Simulation**: "What-if" scenario analysis engine.

## Getting Started

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/causal-supply-chain-toolkit.git
cd causal-supply-chain-toolkit
pip install -r requirements.txt
```

### Quick Start

See `notebooks/01_causal_walkthrough.ipynb` for a complete interactive tutorial.

Or run the example script:

```bash
python examples/intervention_case.py
```

### Usage Example

```python
from utils.data_loader import generate_synthetic_data
from causal.estimation import EffectEstimator

# 1. Load Data
data = generate_synthetic_data()

# 2. Estimate Effect
estimator = EffectEstimator(data)
estimate = estimator.estimate_effect(
    treatment='route_choice',
    outcome='delivery_delay',
    common_causes=['port_congestion', 'weather_shock']
)

print(f"Effect: {estimate.value}")
```

## Use Cases

-   **Forecasting effect of changing shipment routes**: Understand how route changes impact delivery times.
-   **Identifying bottlenecks via causal graphs**: Discover hidden dependencies in your supply chain.
-   **Simulating interventions on lead times**: Predict the outcome of process improvements before implementing them.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to help improve this toolkit.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

-   Wyrembek et al. (2024). "What if? Causal Machine Learning in Supply Chain Risk Management".
-   Cevik & Gwon (2024). "Weather Anomalies, Supply Chain Pressures and Inflation".