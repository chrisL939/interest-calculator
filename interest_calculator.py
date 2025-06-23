import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from scipy.optimize import root_scalar

# ------------------ Calculation Functions ------------------

def calculate_final_capital(starting_capital, interest_rate, years, monthly_contribution):
    """
    Calculate the final capital from given parameters. 
    """
    monthly_rate = interest_rate / 100 / 12
    months = int(years * 12)
    final_capital = starting_capital * (1 + monthly_rate) ** months

    for m in range(1, months + 1):
        final_capital += monthly_contribution * (1 + monthly_rate) ** (months - m)

    return final_capital

def calculate_starting_capital(final_capital, interest_rate, years, monthly_contribution):
    """
    Calculate the required starting capital to reach a desired final capital.
    """
    monthly_rate = interest_rate / 100 / 12
    months = int(years * 12)

    contribution_sum = sum(monthly_contribution * (1 + monthly_rate) ** (months - m) for m in range(1, months + 1))
    starting_capital = (final_capital - contribution_sum) / ((1 + monthly_rate) ** months)

    return starting_capital

def calculate_years(starting_capital, interest_rate, final_capital, monthly_contribution):
    """
    Estimate the number of years needed to reach the final capital.
    """
    monthly_rate = interest_rate / 100 / 12
    balance = starting_capital
    months = 0

    while balance < final_capital and months < 1000 * 12:
        balance *= (1 + monthly_rate)
        balance += monthly_contribution
        months += 1

    return months / 12 if balance >= final_capital else None

def calculate_interest_rate(starting_capital, years, final_capital, monthly_contribution):
    """
    Use scipy's root_scalar to find the interest rate that results in the desired final capital.
    """
    months = int(years * 12)

    def fv_function(rate):
        monthly_rate = rate / 12
        future_value = starting_capital * (1 + monthly_rate) ** months
        for m in range(1, months + 1):
            future_value += monthly_contribution * (1 + monthly_rate) ** (months - m)
        return future_value - final_capital

    result = root_scalar(fv_function, bracket=[0.00001, 1], method='brentq')
    return result.root * 100 if result.converged else None

# ------------------ GUI Logic ------------------

def perform_calculation():
    """
    Collect user inputs, perform the selected calculation, and display the result.
    """
    try:
        target = combo.get()

        starting_capital = float(entry_starting.get()) if entry_starting["state"] == "normal" and entry_starting.get() else 0
        interest = float(entry_interest.get()) if entry_interest["state"] == "normal" and entry_interest.get() else 0
        years = float(entry_years.get()) if entry_years["state"] == "normal" and entry_years.get() else 0
        final_capital = float(entry_final.get()) if entry_final["state"] == "normal" and entry_final.get() else 0
        contribution = float(entry_contribution.get())

        if target == "Final Capital":
            result = calculate_final_capital(starting_capital, interest, years, contribution)
            label_result.config(text=f"Final Capital: €{result:.2f}")
        elif target == "Starting Capital":
            result = calculate_starting_capital(final_capital, interest, years, contribution)
            label_result.config(text=f"Starting Capital: €{result:.2f}")
        elif target == "Interest Rate":
            result = calculate_interest_rate(starting_capital, years, final_capital, contribution)
            if result is not None:
                label_result.config(text=f"Interest Rate: {result:.4f}% p.a.")
            else:
                label_result.config(text="Could not determine the interest rate.")
        elif target == "Duration":
            result = calculate_years(starting_capital, interest, final_capital, contribution)
            if result is not None:
                label_result.config(text=f"Duration: {result:.1f} years")
            else:
                label_result.config(text="Could not determine the duration.")
        else:
            messagebox.showerror("Error", "Invalid selection.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")

def update_input_fields(event=None):
    """
    Enable all input fields except the one being calculated.
    """
    target = combo.get()

    fields = {
        "Starting Capital": entry_starting,
        "Interest Rate": entry_interest,
        "Duration": entry_years,
        "Final Capital": entry_final,
    }

    for field in fields.values():
        field.config(state="normal")
        field.delete(0, tk.END)

    if target in fields:
        fields[target].config(state="disabled")

# ------------------ Main Window ------------------

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("380x370")
root.resizable(False, False)

# Dropdown for choosing what to calculate
tk.Label(root, text="What do you want to calculate?", font=("Arial", 10)).grid(row=0, column=0, columnspan=2, pady=10)
combo = ttk.Combobox(root, values=["Final Capital", "Starting Capital", "Interest Rate", "Duration"])
combo.set("Final Capital")
combo.grid(row=1, column=0, columnspan=2)
combo.bind("<<ComboboxSelected>>", update_input_fields)

# Input fields
tk.Label(root, text="Starting Capital (€):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_starting = tk.Entry(root)
entry_starting.grid(row=2, column=1)

tk.Label(root, text="Interest Rate (% p.a.):").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_interest = tk.Entry(root)
entry_interest.grid(row=3, column=1)

tk.Label(root, text="Duration (years):").grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_years = tk.Entry(root)
entry_years.grid(row=4, column=1)

tk.Label(root, text="Final Capital (€):").grid(row=5, column=0, sticky="e", padx=5, pady=5)
entry_final = tk.Entry(root)
entry_final.grid(row=5, column=1)

tk.Label(root, text="Monthly Contribution (€):").grid(row=6, column=0, sticky="e", padx=5, pady=5)
entry_contribution = tk.Entry(root)
entry_contribution.grid(row=6, column=1)

# Button to calculate
tk.Button(root, text="Calculate", command=perform_calculation, bg="#4CAF50", fg="white").grid(row=7, column=0, columnspan=2, pady=15)

# Result display
label_result = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_result.grid(row=8, column=0, columnspan=2, pady=10)

# Initialize input fields
update_input_fields()

# Start the GUI
root.mainloop()
