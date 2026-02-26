# ============================================================
#  Smart Arithmetic Calculator — Procedural Paradigm
#  Lab Activity 3: Applying Software Paradigms
# ============================================================

RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RED     = "\033[91m"

# Custom palette via ANSI 256-color 
PINK     = "\033[38;5;211m"   # ≈ #FFA0B6 — title highlight
LAVENDER = "\033[38;5;147m"   # ≈ #C1C1ED — banner border & text
BLUSH    = "\033[38;5;217m"   # ≈ #FFD6E0 — result banner

BORDER = "═" * 50

def banner():
    """Display the application banner."""
    print(f"\n{LAVENDER}{BORDER}{RESET}")
    print(f"{LAVENDER}  {PINK}{BOLD}{'Smart Arithmetic Calculator':^48}{RESET}")
    print(f"{LAVENDER}  {DIM}Paradigm: Procedural  ·  Language: Python{RESET}{LAVENDER}")
    print(f"{BORDER}{RESET}\n")

def section(label):
    """Print a dimmed section separator."""
    print(f"  {DIM}{'─' * 44}{RESET}")
    if label:
        print(f"  {DIM}{label}{RESET}")

def fmt_num(n):
    """Format a number: show as int if it's a whole number."""
    return int(n) if n == int(n) else n

# ── Input helpers ────────────────────────────────────────────

def get_number(prompt):
    """Prompt the user for a numeric input and validate it."""
    while True:
        raw = input(f"  {BOLD}{prompt}{RESET} ").strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  {RED}[✗] Invalid input — please enter a valid number.{RESET}\n")

def get_operation():
    """Prompt the user for an operation and validate it."""
    valid = {"+", "-", "*", "/", "%"}
    print(f"\n  {DIM}Available operations:{RESET}")
    ops = [
        ("+", "Addition"),
        ("-", "Subtraction"),
        ("*", "Multiplication"),
        ("/", "Division"),
        ("%", "Modulus"),
    ]
    for sym, name in ops:
        print(f"    {LAVENDER}{sym}{RESET}  {name}")
    print()
    while True:
        op = input(f"  {BOLD}Choose an operation:{RESET} ").strip()
        if op in valid:
            return op
        print(f"  {RED}[✗] Invalid — choose one of: + - * / %{RESET}\n")

# ── Arithmetic functions ─────────────────────────────────────

def add(a, b):       return a + b
def subtract(a, b):  return a - b
def multiply(a, b):  return a * b

def divide(a, b):
    if b == 0:
        return None, "Division by zero is not allowed."
    return a / b, None

def modulus(a, b):
    if b == 0:
        return None, "Modulus by zero is not allowed."
    return a % b, None

def calculate(a, op, b):
    """
    Dispatch to the correct arithmetic function.
    Returns (result, error). On success, error is None.
    """
    dispatch = {
        "+": lambda: (add(a, b), None),
        "-": lambda: (subtract(a, b), None),
        "*": lambda: (multiply(a, b), None),
        "/": lambda: divide(a, b),
        "%": lambda: modulus(a, b),
    }
    return dispatch[op]()

# ── Display helpers ──────────────────────────────────────────

OP_NAMES = {
    "+": "Addition",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division",
    "%": "Modulus",
}

def display_result(a, op, b, result):
    """Show the calculation result in a styled box."""
    a_d, b_d, r_d = fmt_num(a), fmt_num(b), fmt_num(result)
    op_name = OP_NAMES.get(op, op)
    print(f"\n  {DIM}Operation : {RESET}{op_name}")
    print(f"  {DIM}Expression: {RESET}{BOLD}{a_d} {op} {b_d}{RESET}")
    print(f"\n  {BLUSH}{'─' * 30}{RESET}")
    print(f"  {BLUSH}{BOLD}     Result = {r_d}{RESET}")
    print(f"  {BLUSH}{'─' * 30}{RESET}")

def display_history(history):
    """Print a summary of all calculations done this session."""
    if not history:
        return
    section("Session History")
    for i, (a, op, b, res) in enumerate(history, 1):
        a_d, b_d, r_d = fmt_num(a), fmt_num(b), fmt_num(res)
        print(f"  {DIM}[{i}]{RESET}  {a_d} {LAVENDER}{op}{RESET} {b_d} {DIM}={RESET} {BOLD}{r_d}{RESET}")

# ── Main loop ────────────────────────────────────────────────

def main():
    banner()
    history = []

    while True:
        section("")

        # Step 1 — Get inputs
        a  = get_number("First number  :")
        op = get_operation()
        b  = get_number("Second number :")

        # Step 2 — Calculate
        result, error = calculate(a, op, b)

        # Step 3 — Show result or error
        if error:
            print(f"\n  {RED}[✗] {error}{RESET}")
        else:
            display_result(a, op, b, result)
            history.append((a, op, b, result))

        # Step 4 — Continue?
        print()
        again = input(f"  {BOLD}Calculate again?{RESET} {DIM}(yes / no){RESET}: ").strip().lower()
        if again != "yes":
            print()
            display_history(history)
            print(f"\n  {PINK}{BOLD}Thank you for using Smart Calculator. Goodbye!{RESET}")
            print(f"  {LAVENDER}{BORDER}{RESET}\n")
            break

# ── Entry point ──────────────────────────────────────────────

if __name__ == "__main__":
    main()
