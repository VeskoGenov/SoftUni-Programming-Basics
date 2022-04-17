v = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

pipes_debit = (pipe_1 + pipe_2) * hours
percentage_fill = (pipes_debit * 100) / v
overflow = pipes_debit - v

pipe_1_contribution = ((pipe_1 * hours) / pipes_debit) * 100
pipe_2_contribution = ((pipe_2 * hours) / pipes_debit) * 100

if pipes_debit < v:
    print(f"The pool is {percentage_fill:.2f}% full. Pipe 1: {pipe_1_contribution:.2f}%. "
          f"Pipe 2: {pipe_2_contribution:.2f}%.")
else:
    print(f"For {hours:.2f} hours the poоl overflows with {overflow:.2f} liters.")