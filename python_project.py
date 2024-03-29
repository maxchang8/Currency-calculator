"""Importing"""
import tkinter as tk

class CurrencyConverter:
    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Currency Converter")
        self.rootWin.config(bg="lightblue")
        self.historyLog = []

        titleLabel = tk.Label(self.rootWin, text="Currency Converter", font="Arial 36 bold", bg="lightblue", bd=10,
                              justify=tk.CENTER, padx=10, pady=10)
        titleLabel.grid(row=0, column=0, columnspan=3)
        titleLabel.config(bg="blue")

        historyLogLabel = tk.Label(self.rootWin, text="History Log", font="Arial 24", bg="lightblue", bd=10,
                              justify=tk.CENTER, padx=10, pady=10)
        historyLogLabel.grid(row=3, column=0, columnspan=3)
        historyLogLabel.config(bg="blue")

        self.historyLogText = tk.Label(self.rootWin, text="", font="Arial 24", bg="lightblue", bd=10,
                                          justify=tk.LEFT, padx=10, pady=10)
        self.historyLogText.grid(row=4, column=0, columnspan=3)
        self.historyLogText.config(bg="lightblue")

        starter_currency_label = tk.Label(self.rootWin, text="Starter Currency:", font="Arial 30")
        starter_currency_label.grid(row=1, column=0)
        starter_currency_options = ["US Dollar", "Euro", "Won", "JPY", "CNH"]
        selected_starter_currency = tk.StringVar()
        selected_starter_currency.set(starter_currency_options[0])
        starter_currency_dropdown = tk.OptionMenu(self.rootWin, selected_starter_currency, *starter_currency_options)
        starter_currency_dropdown.grid(row=1, column=1, pady=10)

        ending_currency_label = tk.Label(self.rootWin, text="Ending Currency:", font="Arial 30")
        ending_currency_label.grid(row=1, column=2)
        ending_currency_options = ["US Dollar", "Euro", "Won", "JPY", "CNH"]

        selected_ending_currency = tk.StringVar()
        selected_ending_currency.set(ending_currency_options[0])
        ending_currency_dropdown = tk.OptionMenu(self.rootWin, selected_ending_currency, *ending_currency_options)
        ending_currency_dropdown.grid(row=1, column=3, pady=10)

        convertButton = tk.Button(self.rootWin, text="Convert!", font="Arial 30", command=self.convert_currencies)
        convertButton.grid(row=2, column=1)

        self.entryBox = tk.Entry(self.rootWin, bg="white", font="Arial 30", width=5, justify=tk.CENTER)
        self.entryBox.grid(row=2, column=0)

        self.resultLabel = tk.Label(self.rootWin, text="", font="Arial 30", bg="lightblue", bd=10,
                                    justify=tk.CENTER, padx=10, pady=10)
        self.resultLabel.grid(row=2, column=2, columnspan=1)

        self.rootWin.rowconfigure(0, minsize=50, weight=1)
        self.rootWin.columnconfigure([0, 1, 2], minsize=50, weight=1)

        self.selected_starter_currency = selected_starter_currency
        self.selected_ending_currency = selected_ending_currency

        self.clearHistoryButton = tk.Button(self.rootWin, text="Clear History", font="Arial 20", command=self.clear_history)
        self.clearHistoryButton.grid(row=5, column=1)

    def clear_history(self):
            self.historyLog = []
            self.update_history_log()

    def convert_currencies(self):
        """takes the input value from the entry box and runs the function "get conversion rate" to get the conversion
        then round the number to 2 decimal places and changes the resultLabel to the new value"""
        try:
            input_num = float(self.entryBox.get())
        except ValueError:
            self.resultLabel["text"] = "Invalid input"
            return
        input_num = float(self.entryBox.get())
        starter_currency = self.selected_starter_currency.get()
        ending_currency = self.selected_ending_currency.get()

        conversion_rate = self.get_conversion_rate(starter_currency, ending_currency)
        new_num = round(input_num * conversion_rate, 2)

        self.resultLabel["text"] = new_num

        conversion_record = {
            "from_currency": starter_currency,
            "to_currency": ending_currency,
            "amount": input_num,
            "result": new_num,
        }
        self.historyLog.append(conversion_record)

        self.update_history_log()

    def update_history_log(self):
        """It allows the last 15 entries from historyLog to show, then it joins the last entry of the dictionary to a
        string, and updates history log text"""
        last_entries = self.historyLog[-15:]
        log_text = "\n".join([f"{entry['amount']} {entry['from_currency']} "
                              f"to {entry['result']} {entry['to_currency']}" for entry in last_entries])
        self.historyLogText["text"] = log_text

    def get_conversion_rate(self, starter_currency, ending_currency):
        """It holds the dictionary for conversion rates and feeds them to "convert currencies" when needed"""
        conversion_rates = {
            ("US Dollar", "Dollar"): 1.0,
            ("US Dollar", "Euro"): 0.93,
            ("US Dollar", "Won"): 1319.38,
            ("US Dollar", "JPY"): 146.36,
            ("US Dollar", "CNH"): 7.192767,
            ("Euro", "US Dollar"): 1.08,
            ("Euro", "Euro"): 1.0,
            ("Euro", "Won"): 1418.39,
            ("Euro", "JPY"): 157.38,
            ("Euro", "CNH"): 7.73447,
            ("Won", "US Dollar"): 0.00076,
            ("Won", "Euro"): 0.00070,
            ("Won", "Won"): 1.0,
            ("Won", "JPY"): 0.11,
            ("Won", "CNH"): 0.005459,
            ("JPY", "US Dollar"): 0.0068,
            ("JPY", "Euro"): 0.0064,
            ("JPY", "Won"): 9.01,
            ("JPY", "JPY"): 1.0,
            ("JPY", "CNH"): 0.049414,
            ("CNH", "US Dollar"): 0.139086,
            ("CNH", "Euro"): 0.129169,
            ("CNH", "Won"): 183.383041,
            ("CNH", "JPY"): 20.22399634,
            ("CNH", "CNH"): 1.0,
        }
        return conversion_rates.get((starter_currency, ending_currency), 1.0)

    def run(self):
        """runs the class function forever..."""
        self.rootWin.mainloop()

convert = CurrencyConverter()
convert.run()