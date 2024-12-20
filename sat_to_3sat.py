def sat_to_3sat(formula):
    """
    Converts a SAT formula to a 3-SAT formula.
    Assumes that the input formula is a list of clauses, where each clause is a list of literals.
    If a clause has more than 3 literals, it will be split into multiple clauses using auxiliary variables.
    If a clause has fewer than 3 literals, dummy variables will be added.
    """
    result = []
    auxiliary_counter = 0  # Counter for generating auxiliary variables (like y0, y1, etc.)
    
    for clause in formula:
        if len(clause) == 3:
            result.append(clause)  # Clause already has 3 literals, no change needed
        elif len(clause) > 3:
            # Split clauses with more than 3 literals into multiple 3-literal clauses using auxiliary variables
            while len(clause) > 3:
                new_clause = [clause[0], clause[1], f'y{auxiliary_counter}']
                result.append(new_clause)
                clause = [f'-y{auxiliary_counter}'] + clause[2:]
                auxiliary_counter += 1
            result.append(clause)  # Add the remaining clause (which now has exactly 3 literals)
        else:
            # Handle case for clauses with fewer than 3 literals (e.g., adding dummy literals)
            clause += ['dummy'] * (3 - len(clause))  # Add enough dummy variables to make it 3 literals
            result.append(clause)

    # Remove any "dummy" clauses at the end of the formula
    result = [clause for clause in result if clause != ['dummy', 'dummy', 'dummy']]

    return result


def read_formula_from_file(file_path):
    """
    Reads a formula from a text file. The file contains one clause per line,
    and literals in each clause are separated by spaces.
    """
    with open(file_path, 'r') as file:
        # Read the file line by line, split by space to get the literals for each clause
        formula = [line.strip().split() for line in file.readlines()]
    return formula


def write_formula_to_file(file_path, formula):
    """
    Writes the converted 3-SAT formula to a file.
    Each clause is written in one line with literals separated by spaces.
    """
    with open(file_path, 'w') as file:
        for clause in formula:
            file.write(' '.join(clause) + '\n')


def main():
    input_file = 'tests/example_inputs/example_2.txt'  # Replace with your actual input file path
    output_file = 'output_3sat.txt'  # Replace with your desired output file path

    # Read the original SAT formula from the file
    sat_formula = read_formula_from_file(input_file)

    # Convert the SAT formula to 3-SAT
    three_sat_formula = sat_to_3sat(sat_formula)

    # Write the 3-SAT formula to the output file
    write_formula_to_file(output_file, three_sat_formula)

    print(f"3-SAT formula written to {output_file}")


if __name__ == "__main__":
    main()

