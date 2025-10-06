"""Simple calculator script

Features:
- Functions: add, subtract, multiply, divide, modulo, power
- Interactive menu mode
- CLI mode: python day4.py add 2 3
- Input validation and divide-by-zero handling
"""

import sys
import operator

# Basic operations mapping: name -> (function, symbol)
OPS = {
	"add": (operator.add, "+"),
	"sub": (operator.sub, "-"),
	"mul": (operator.mul, "*"),
	"div": (operator.truediv, "/"),
	"mod": (operator.mod, "%"),
	"pow": (operator.pow, "**"),
}


def calculate(op_name, a, b):
	"""Perform calculation and return result or raise ValueError for invalid ops."""
	if op_name not in OPS:
		raise ValueError(f"Unknown operation: {op_name}")
	func, _ = OPS[op_name]
	# handle division by zero for div and mod
	if op_name in ("div", "mod") and b == 0:
		raise ZeroDivisionError("division by zero")
	return func(a, b)


def interactive():
	print("Simple calculator (type 'q' to quit)")
	print("Operations: " + ", ".join(OPS.keys()))
	while True:
		choice = input("Operation: ").strip()
		if choice.lower() in ("q", "quit", "exit"):
			print("Goodbye")
			return
		if choice not in OPS:
			print("Unknown operation. Try again.")
			continue
		try:
			a = float(input("Enter first number: "))
			b = float(input("Enter second number: "))
		except ValueError:
			print("Invalid number. Try again.")
			continue
		try:
			res = calculate(choice, a, b)
		except ZeroDivisionError:
			print("Error: division by zero")
		except Exception as e:
			print(f"Error: {e}")
		else:
			print(f"Result: {a} {OPS[choice][1]} {b} = {res}")


def cli_mode(args):
	# args: [op, a, b]
	if len(args) < 3:
		raise ValueError("CLI mode requires: <op> <num1> <num2>")
	op = args[0]
	try:
		a = float(args[1])
		b = float(args[2])
	except ValueError:
		raise ValueError("Both operands must be numbers")
	return calculate(op, a, b)


def main():
	if len(sys.argv) > 1:
		# CLI mode
		try:
			result = cli_mode(sys.argv[1:])
		except Exception as e:
			print(f"Error: {e}")
			sys.exit(1)
		else:
			print(result)
			return
	else:
		interactive()


if __name__ == "__main__":
	main()
