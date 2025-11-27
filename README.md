# Causal Supply Chain Toolkit

A Python toolkit for causal inference methods for evaluating logistics interventions in supply chains.

## Overview

This toolkit implements causal inference methods to help supply chain analysts and data scientists evaluate the impact of interventions. By leveraging causal analysis, you can go beyond correlation and understand the true drivers of efficiency, delays, and costs in your logistics network.

## Getting Started

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/causal-supply-chain-toolkit.git
cd causal-supply-chain-toolkit
pip install -r requirements.txt
```

### Usage Example

Here is a minimal example of how to use the toolkit to estimate the effect of an intervention:

```python
from causal_toolkit import CausalModel
import pandas as pd

# Load your data
data = pd.read_csv('data/processed/supply_chain_data.csv')

# Initialize the model
model = CausalModel(data, treatment='expedited_shipping', outcome='delivery_delay')

# Estimate the effect
effect = model.estimate_effect()

print(f"Estimated effect of expedited shipping on delay: {effect:.2f} days")
# Output: Estimated effect of expedited shipping on delay: -5.20 days
```

## Use Cases

- **Forecasting effect of changing shipment routes**: Understand how route changes impact delivery times.
- **Identifying bottlenecks via causal graphs**: Discover hidden dependencies in your supply chain.
- **Simulating interventions on lead times**: Predict the outcome of process improvements before implementing them.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to help improve this toolkit.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- Wyrembek et al. (2024). "Causal ML for Supply Chain Risk".