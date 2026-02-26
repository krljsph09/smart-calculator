import operator
from typing import Dict, Callable, Union

def calculate(expression: str) -> Union[float, str]:
    """
    A pure functional calculator that processes a string expression.
    
    Args:
        expression: A string in the format "number operator number" (e.g., "10 + 5")
        
    Returns:
        The float result or an error message string.
    """
    
    # 1. Define operations as a mapping to pure functions
    # Using the operator module ensures no side effects and clean logic
    operations: Dict[str, Callable[[float, float], float]] = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod
    }

    # 2. Parse and Validate input (Pure transformation)
    parts = expression.split()
    
    if len(parts) != 3:
        return "Error: Invalid format. Use 'num op num' (e.g., '10 + 2')."

    left_val, op, right_val = parts

    # 3. Guard clauses (Return values instead of raising unhandled exceptions)
    try:
        num1 = float(left_val)
        num2 = float(right_val)
    except ValueError:
        return "Error: Non-numeric input detected."

    if op not in operations:
        return f"Error: Unsupported operator '{op}'."

    if op == '/' and num2 == 0:
        return "Error: Division by zero."
    
    if op == '%' and num2 == 0:
        return "Error: Modulo by zero."

    # 4. Execute the mapped function and return the result
    return operations[op](num1, num2)

# --- Test Cases ---
if __name__ == "__main__":
    test_inputs = ["10 + 5", "20 * 3", "10 / 2", "7 % 3", "bad input", "5 / 0"]
    
    print(f"{'Input':<15} | {'Result':<10}")
    print("-" * 30)
    for inp in test_inputs:
        print(f"{inp:<15} | {calculate(inp)}")
