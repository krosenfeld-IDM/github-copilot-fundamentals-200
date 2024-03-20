Documentation for diophantine_equation.py
This Python module contains functions for solving Diophantine equations. A Diophantine equation is a polynomial equation where only integer solutions are allowed. The module contains three main functions: diophantine, diophantine_all_soln, and extended_gcd.

Running the Module
To run this module, you can use the Python interpreter from your terminal:

python diophantine_equation.py
This will run the doctests for all functions in the module.

Functions
diophantine(a: int, b: int, c: int) -> tuple[float, float]
This function solves a Diophantine equation of the form ax + by = c where a, b, and c are integers, and x and y are the solutions we want to find. The function uses the greatest common divisor (gcd) of a and b and the extended Euclidean algorithm to find a solution. The function asserts that c is divisible by the gcd of a and b, as this is a necessary condition for the equation to have a solution.

diophantine_all_soln(a: int, b: int, c: int, n: int = 2) -> None
This function finds all solutions of a Diophantine equation. It uses the theorem that if (x0,y0) is a solution of the Diophantine equation ax + by = c, then all the solutions have the form a(x0 + tq) + b(y0 - tp) = c, where t is an arbitrary integer. The function prints n solutions, where n is a parameter with a default value of 2.

extended_gcd(a: int, b: int) -> tuple[int, int, int]
This function implements the extended Euclidean algorithm, which finds x and y such that gcd(a, b) = ax + by. The function uses recursion to find x and y. If b is 0, then gcd(a, b) = a, so it returns a, 1, and 0. Otherwise, it recursively calls itself with b and a % b as the arguments. It then uses the results of the recursive call to find x and y. The function also includes assertions to check that a and b are both non-negative and that d = ax + by.