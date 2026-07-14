import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date
from typing import cast
import calendar


class ExpenseApp:

    def __init__(self, expense_service):
        self.expense_service = expense_service
        self.root = tk.Tk()
        self.root.title("Expense Agent")
        self.root.geometry("980x720")
        self.root.resizable(True, True)

        self._build_ui()
        self.refresh_expense_list()
        self._fill_report_defaults()

    def _build_ui(self):
        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.grid(row=0, column=0, sticky="NSEW")

        top_frame = ttk.LabelFrame(main_frame, text="Add Expense", padding=12)
        top_frame.grid(row=0, column=0, columnspan=2, sticky="EW", pady=(0, 12))

        ttk.Label(top_frame, text="Amount:").grid(row=0, column=0, sticky="W")
        self.amount_var = tk.StringVar()
        ttk.Entry(top_frame, textvariable=self.amount_var, width=18).grid(row=0, column=1, sticky="W", padx=(4, 18))

        ttk.Label(top_frame, text="Category:").grid(row=0, column=2, sticky="W")
        self.category_var = tk.StringVar(value=self.expense_service.ALLOWED_CATEGORIES[0])
        ttk.Combobox(
            top_frame,
            textvariable=self.category_var,
            values=self.expense_service.ALLOWED_CATEGORIES,
            state="readonly",
            width=16
        ).grid(row=0, column=3, sticky="W", padx=(4, 18))

        ttk.Label(top_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=4, sticky="W")
        self.date_var = tk.StringVar(value=date.today().isoformat())
        ttk.Entry(top_frame, textvariable=self.date_var, width=16).grid(row=0, column=5, sticky="W", padx=(4, 0))

        ttk.Label(top_frame, text="Description:").grid(row=1, column=0, sticky="NW", pady=(8, 0))
        self.description_text = tk.Text(top_frame, width=70, height=3)
        self.description_text.grid(row=1, column=1, columnspan=5, sticky="EW", pady=(8, 0))

        self.add_button = ttk.Button(top_frame, text="Add Expense", command=self.on_add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2, sticky="W", pady=(12, 0))

        self.status_label = ttk.Label(top_frame, text="Enter a new expense and click Add Expense.")
        self.status_label.grid(row=2, column=2, columnspan=4, sticky="W", padx=(12, 0), pady=(12, 0))

        parse_frame = ttk.LabelFrame(main_frame, text="Parse Natural Language Expense", padding=12)
        parse_frame.grid(row=1, column=0, columnspan=2, sticky="EW", pady=(0, 12))

        self.natural_text = tk.Text(parse_frame, width=110, height=3)
        self.natural_text.grid(row=0, column=0, columnspan=3, sticky="EW")

        self.parse_button = ttk.Button(parse_frame, text="Parse & Add", command=self.on_parse_expense_text)
        self.parse_button.grid(row=1, column=0, sticky="W", pady=(8, 0))

        self.parse_status = ttk.Label(parse_frame, text="Use natural language to describe an expense.")
        self.parse_status.grid(row=1, column=1, sticky="W", pady=(8, 0), padx=(12, 0))

        parse_frame.columnconfigure(0, weight=1)
        parse_frame.columnconfigure(1, weight=1)
        parse_frame.columnconfigure(2, weight=1)

        list_frame = ttk.LabelFrame(main_frame, text="Saved Expenses", padding=12)
        list_frame.grid(row=2, column=0, sticky="NSEW", pady=(0, 12))

        self.expense_tree = ttk.Treeview(
            list_frame,
            columns=("ID", "Date", "Amount", "Category", "Description"),
            show="headings",
            height=14
        )
        self.expense_tree.heading("ID", text="ID")
        self.expense_tree.heading("Date", text="Date")
        self.expense_tree.heading("Amount", text="Amount")
        self.expense_tree.heading("Category", text="Category")
        self.expense_tree.heading("Description", text="Description")
        self.expense_tree.column("ID", width=40, anchor="center")
        self.expense_tree.column("Date", width=100, anchor="center")
        self.expense_tree.column("Amount", width=100, anchor="e")
        self.expense_tree.column("Category", width=120, anchor="center")
        self.expense_tree.column("Description", width=430, anchor="w")
        self.expense_tree.grid(row=0, column=0, sticky="NSEW")

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.expense_tree.yview)
        self.expense_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="NS")

        refresh_button = ttk.Button(list_frame, text="Refresh List", command=self.refresh_expense_list)
        refresh_button.grid(row=1, column=0, sticky="W", pady=(8, 0))

        report_frame = ttk.LabelFrame(main_frame, text="Monthly Expense Report", padding=12)
        report_frame.grid(row=2, column=1, sticky="NSEW", pady=(0, 12), padx=(12, 0))

        ttk.Label(report_frame, text="Month:").grid(row=0, column=0, sticky="W")
        self.month_var = tk.StringVar(value=calendar.month_name[date.today().month])
        ttk.Combobox(
            report_frame,
            textvariable=self.month_var,
            values=list(calendar.month_name)[1:],
            state="readonly",
            width=15
        ).grid(row=0, column=1, sticky="W", padx=(4, 12))

        ttk.Label(report_frame, text="Year:").grid(row=0, column=2, sticky="W")
        self.year_var = tk.IntVar(value=date.today().year)
        ttk.Spinbox(report_frame, from_=2000, to=date.today().year + 5, textvariable=self.year_var, width=8).grid(row=0, column=3, sticky="W", padx=(4, 12))

        self.report_button = ttk.Button(report_frame, text="Generate Report", command=self.on_generate_report)
        self.report_button.grid(row=0, column=4, sticky="W")

        self.report_text = tk.Text(report_frame, width=56, height=20, state="disabled", wrap="none")
        self.report_text.grid(row=1, column=0, columnspan=5, pady=(8, 0), sticky="NSEW")

        report_scroll = ttk.Scrollbar(report_frame, orient="vertical", command=self.report_text.yview)
        self.report_text.configure(yscrollcommand=report_scroll.set)
        report_scroll.grid(row=1, column=5, sticky="NS")

        for child in top_frame.winfo_children():
            child = cast(tk.Widget, child)
            child.grid_configure(padx=4, pady=2)

        parse_frame.columnconfigure(0, weight=1)
        parse_frame.columnconfigure(1, weight=1)
        parse_frame.columnconfigure(2, weight=1)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        report_frame.columnconfigure(0, weight=1)
        report_frame.columnconfigure(1, weight=1)
        report_frame.columnconfigure(2, weight=1)
        report_frame.columnconfigure(3, weight=1)
        report_frame.columnconfigure(4, weight=1)
        report_frame.rowconfigure(1, weight=1)
        main_frame.columnconfigure(0, weight=3)
        main_frame.columnconfigure(1, weight=2)
        main_frame.rowconfigure(0, weight=0)
        main_frame.rowconfigure(1, weight=0)
        main_frame.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def _fill_report_defaults(self):
        self.on_generate_report()

    def on_add_expense(self):
        amount_text = self.amount_var.get().strip()
        category = self.category_var.get().strip()
        description = self.description_text.get("1.0", "end").strip()
        expense_date = self.date_var.get().strip() or date.today().isoformat()

        if not amount_text:
            messagebox.showwarning("Missing amount", "Please enter an amount for the expense.")
            return

        if not description:
            messagebox.showwarning("Missing description", "Please enter a description for the expense.")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            messagebox.showerror("Invalid amount", "Amount must be a valid number.")
            return

        try:
            expense = self.expense_service.add_expense_record(
                amount=amount,
                category=category,
                description=description,
                expense_date=expense_date
            )
        except Exception as exc:
            messagebox.showerror("Add Expense Failed", str(exc))
            return

        self.status_label.config(text=f"Expense added: {expense.description} ({expense.category})")
        self._clear_add_fields()
        self.refresh_expense_list()

    def on_parse_expense_text(self):
        natural_text = self.natural_text.get("1.0", "end").strip()
        if not natural_text:
            messagebox.showwarning("Missing text", "Please enter the natural language expense text.")
            return

        try:
            expense = self.expense_service.parse_expense_text(natural_text)
            self.expense_service.expense_repository.save(expense)
        except Exception as exc:
            self.parse_status.config(text=f"Failed to parse expense: {exc}")
            return

        self.parse_status.config(text=f"Expense parsed and saved: {expense.description}")
        self.natural_text.delete("1.0", "end")
        self.refresh_expense_list()

    def on_generate_report(self):
        month_name = self.month_var.get()
        year = self.year_var.get()
        try:
            month = list(calendar.month_name).index(month_name)
        except ValueError:
            messagebox.showerror("Invalid month", "Please select a valid month.")
            return

        summary_rows = self.expense_service.get_monthly_summary_data(month, year)
        if not summary_rows:
            report_text = f"No expenses found for {month_name} {year}."
        else:
            report_text = self.expense_service.format_monthly_report(month, year, summary_rows)

        self.report_text.configure(state="normal")
        self.report_text.delete("1.0", "end")
        self.report_text.insert("1.0", report_text)
        self.report_text.configure(state="disabled")

    def refresh_expense_list(self):
        for row in self.expense_tree.get_children():
            self.expense_tree.delete(row)

        expenses = self.expense_service.get_all_expenses()
        for expense in expenses:
            self.expense_tree.insert(
                "",
                "end",
                values=(
                    expense["id"],
                    expense["expense_date"],
                    f"₹{expense['amount']:.2f}",
                    expense["category"],
                    expense["description"]
                )
            )

        self.status_label.config(text=f"Loaded {len(expenses)} saved expenses.")

    def _clear_add_fields(self):
        self.amount_var.set("")
        self.category_var.set(self.expense_service.ALLOWED_CATEGORIES[0])
        self.description_text.delete("1.0", "end")
        self.date_var.set(date.today().isoformat())

    def run(self):
        self.root.mainloop()
