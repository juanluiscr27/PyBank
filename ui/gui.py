from model.movement import Movement
from model.product import Product
from ui import *
from model import util

class GUI:

    active_agent = Agent()
    active_customer = Customer()
    active_account = None
    active_movement = None
    result = Return()
    window = tk.Tk()
    customers = []
    accounts = []
    movements = []
    window.resizable(False, False)
    login_size = "450x400"
    window_size = "1200x700"

    @classmethod
    def start_gui(cls):
        cls.window.mainloop()

    @classmethod
    def agent_login(cls):
        def action_login():
            error_message.config(text="")
            if username.get() == "":
                error_message.config(text="Please input your username", foreground="Red")
            elif password.get() == "":
                error_message.config(text="Please input your password", foreground="Red")
            else:
                cls.active_agent.login(username.get(), password.get(), cls.result)
                if cls.result.code == "00":
                    print("Login OK")
                    area.destroy()
                    cls.search()
                else:
                    error_message.config(text=cls.result.message, foreground="Red")
        cls.window.title("PyBank")
        cls.window.geometry(cls.login_size)
        area = ttk.LabelFrame(cls.window, text="Agent login")
        area.grid(column=0, row=0, padx=50, pady=50)
        username_label = ttk.Label(area, text="Username")
        username_label.grid(column=0, row=0, padx=20, pady=10)
        username = tk.StringVar()
        username_text = ttk.Entry(area, width=30, textvariable=username)
        username_text.grid(column=1, row=0, padx=20, pady=10)
        password_label = ttk.Label(area, text="Password")
        password_label.grid(column=0, row=1, padx=20, pady=10)
        password = tk.StringVar()
        password_text = ttk.Entry(area, width=30, show='*', textvariable=password)
        password_text.grid(column=1, row=1, padx=20, pady=10)
        login = ttk.Button(area, text="Login", command=action_login)
        login.grid(column=0, row=2, padx=50, pady=50, columnspan=2)
        error_message = ttk.Label(area)
        error_message.grid(column=0, row=3, padx=20, pady=20, columnspan=2)

    @classmethod
    def create_top_menu(cls):
        def logout():
            areas = cls.window.winfo_children()
            for item in areas:
                item.destroy()
            cls.agent_login()
        def search():
            areas = cls.window.winfo_children()
            for item in areas:
                item.destroy()
            cls.search()
        def new_customer():
            areas = cls.window.winfo_children()
            for item in areas:
                item.destroy()
            cls.new_customer()
        def about():
            tk.messagebox.showinfo('About', 'This software was created by Hugo Beltran Escarraga and Juan Luis Casanova Romero.\n\nLambton College - CSAM\nCSD 4523 Python II - Term project')
        menu_bar = Menu(cls.window)
        cls.window.config(menu=menu_bar)
        menu_agent = Menu(menu_bar, tearoff=0)
        menu_agent.add_command(label="Log out", command=logout)
        menu_bar.add_cascade(label="Agent", menu=menu_agent)
        menu_customer = Menu(menu_bar, tearoff=0)
        menu_customer.add_command(label="Search", command=search)
        menu_customer.add_command(label="New customer", command=new_customer)
        menu_bar.add_cascade(label="Customer", menu=menu_customer)
        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="About", command=about)
        menu_bar.add_cascade(label="Help", menu=menu_help)

    @classmethod
    def create_grid_window(cls):
        for i in range(17):
            space_label = ttk.Label(cls.window)
            space_label.grid(column=0, row=i, padx=10, pady=10)
        for i in range(50):
            space_label = ttk.Label(cls.window)
            space_label.grid(column=i, row=0, padx=10, pady=10)

    @classmethod
    def create_grid_area(cls, area):
        for i in range(15):
            space_label = ttk.Label(area)
            space_label.grid(column=0, row=i, padx=10, pady=10)
        for i in range(48):
            space_label = ttk.Label(area)
            space_label.grid(column=i, row=0, padx=10, pady=10)

    @classmethod
    def search(cls):
        def exec_search():
            for i in customers_results.get_children():
                customers_results.delete(i)
            for i in accounts_results.get_children():
                accounts_results.delete(i)
            if search_string.get() != '':
                cls.customers = util.search_customer(search_string.get(), cls.result)
                if cls.result.code == "00":
                    for i in cls.customers:
                        customers_results.insert(parent='', index='end', values=(i.customer_id, i.first_name, i.last_name, i.address, i.phone_number, i.email))
                else:
                    tk.messagebox.showinfo('PyBank', 'No customers found')
                cls.accounts = util.search_account(search_string.get(), cls.result)
                if cls.result.code == "00":
                    for i in cls.accounts:
                        accounts_results.insert(parent='', index='end', values=(i.acc_number, i.acc_type.product_type, i.balance, i.transfer_amount, i.transfer_quantity, i.customer_id, i.open_date))
                else:
                    tk.messagebox.showinfo('PyBank', 'No accounts found')
            else:
                tk.messagebox.showerror('PyBank', 'Input search string')
        def action_customer():
            try:
                cls.active_customer = cls.customers[int(customers_results.selection()[0][1:], 16)-1]
                area.destroy()
                cls.view_customer()
            except IndexError as e:
                if len(customers_results.get_children()) > 0:
                    tk.messagebox.showerror('PyBank', 'Select a customer to view')
                else:
                    tk.messagebox.showerror('PyBank', 'No customers to display')
        def action_account():
            try:
                cls.active_account = cls.accounts[int(accounts_results.selection()[0][1:], 16)-1]
                cls.active_customer = cls.active_account.customer
                area.destroy()
                cls.view_account()
            except IndexError as e:
                if len(accounts_results.get_children()) > 0:
                    tk.messagebox.showerror('PyBank', 'Select an account to view')
                else:
                    tk.messagebox.showerror('PyBank', 'No accounts to display')
        cls.window.geometry(cls.window_size)
        cls.create_top_menu()
        area = ttk.LabelFrame(cls.window, text="Search customers and accounts")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        search_label = ttk.Label(area, text="Search")
        search_label.grid(column=10, row=1, columnspan=5)
        search_string = tk.StringVar()
        search_string_text = ttk.Entry(area, width=40, textvariable=search_string)
        search_string_text.grid(column=15, row=1, columnspan=10)
        search_button = ttk.Button(area, width=30, text="Search", command=exec_search)
        search_button.grid(column=25, row=1, columnspan=10)
        customers_results_label = ttk.Label(area, text="Customers")
        customers_results_label.grid(column=0, row=3, columnspan=10)
        customers_results = ttk.Treeview(area, height=5)
        customers_results.grid(column=0, row=4, columnspan=40, rowspan=5)
        customers_results['columns'] = ('customer_id', 'customer_first_name', 'customer_last_name', 'customer_address', 'customer_phone', 'customer_email')
        customers_results.column("#0", width=0, stretch=False)
        customers_results.column("customer_id", anchor="center", width=50)
        customers_results.column("customer_first_name", anchor="center", width=100)
        customers_results.column("customer_last_name", anchor="center", width=100)
        customers_results.column("customer_address", anchor="center", width=200)
        customers_results.column("customer_phone", anchor="center", width=100)
        customers_results.column("customer_email", anchor="center", width=200)
        customers_results.heading("#0", text="", anchor="center")
        customers_results.heading("customer_id", text="ID", anchor="center")
        customers_results.heading("customer_first_name", text="NAME", anchor="center")
        customers_results.heading("customer_last_name", text="NAME", anchor="center")
        customers_results.heading("customer_address", text="ADDRESS", anchor="center")
        customers_results.heading("customer_phone", text="PHONE", anchor="center")
        customers_results.heading("customer_email", text="EMAIL", anchor="center")
        customers_results_button = ttk.Button(area, width=20, text="View customer", command=action_customer)
        customers_results_button.grid(column=40, row=4, columnspan=8, rowspan=5)
        accounts_results_label = ttk.Label(area, text="Accounts")
        accounts_results_label.grid(column=0, row=9, columnspan=10)
        accounts_results = ttk.Treeview(area, height=5)
        accounts_results.grid(column=0, row=10, columnspan=40, rowspan=5)
        accounts_results['columns'] = ('account_number', 'account_type', 'balance', 'transfer_amount', 'transfer_quantity', 'customer_id', 'open_date')
        accounts_results.column("#0", width=0, stretch=False)
        accounts_results.column("account_number", anchor="center", width=100)
        accounts_results.column("account_type", anchor="center", width=100)
        accounts_results.column("balance", anchor="center", width=100)
        accounts_results.column("transfer_amount", anchor="center", width=100)
        accounts_results.column("transfer_quantity", anchor="center", width=100)
        accounts_results.column("customer_id", anchor="center", width=100)
        accounts_results.column("open_date", anchor="center", width=100)
        accounts_results.heading("#0", text="", anchor="center")
        accounts_results.heading("account_number", text="NUMBER", anchor="center")
        accounts_results.heading("account_type", text="TYPE", anchor="center")
        accounts_results.heading("balance", text="BALANCE", anchor="center")
        accounts_results.heading("transfer_amount", text="TRANSFERRED", anchor="center")
        accounts_results.heading("transfer_quantity", text="TRANSFERS", anchor="center")
        accounts_results.heading("customer_id", text="CUSTOMER", anchor="center")
        accounts_results.heading("open_date", text="OPEN DATE", anchor="center")
        accounts_results_button = ttk.Button(area, width=20, text="View account", command=action_account)
        accounts_results_button.grid(column=40, row=10, columnspan=8, rowspan=5)

    @classmethod
    def view_customer(cls):
        def action_account():
            try:
                cls.active_account = cls.accounts[int(customer_accounts.selection()[0][1:], 16) - 1]
                area.destroy()
                cls.view_account()
            except IndexError as e:
                if len(customer_accounts.get_children()) > 0:
                    tk.messagebox.showerror('PyBank', 'Select an account to view')
                else:
                    tk.messagebox.showerror('PyBank', 'No accounts to display')
        def action_open_account():
            area.destroy()
            cls.open_account()
        def action_update_customer():
            area.destroy()
            cls.update_customer()
        def action_delete_customer():
            area.destroy()
            cls.delete_customer()
        def action_money_chart():
            try:
                chart_accounts = []
                chart_balances = []
                for i in cls.accounts:
                    chart_accounts.append(i.acc_type.product_type + "\n" + i.acc_number + "\n$" + str(i.balance))
                    chart_balances.append(i.balance)
                plt.title("Money distribution")
                plt.pie(chart_balances, labels=chart_accounts)
                plt.show()
            except TypeError as e:
                tk.messagebox.showerror('PyBank', 'Customer has no open accounts')
        cls.window.geometry(cls.window_size)
        cls.create_top_menu()
        area = ttk.LabelFrame(cls.window, text="View customer")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        customer_id_label = ttk.Label(area, text="ID")
        customer_id_label.grid(column=0, row=1, columnspan=5)
        customer_id_text = ttk.Label(area, text=cls.active_customer.customer_id)
        customer_id_text.grid(column=0, row=2, columnspan=5)
        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=5, row=1, columnspan=5)
        customer_first_name_text = ttk.Label(area, text=cls.active_customer.first_name)
        customer_first_name_text.grid(column=5, row=2, columnspan=5)
        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=10, row=1, columnspan=5)
        customer_last_name_text = ttk.Label(area, text=cls.active_customer.last_name)
        customer_last_name_text.grid(column=10, row=2, columnspan=5)
        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=15, row=1, columnspan=5)
        customer_address_text = ttk.Label(area, text=cls.active_customer.address)
        customer_address_text.grid(column=15, row=2, columnspan=5)
        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=20, row=1, columnspan=5)
        customer_phone_text = ttk.Label(area, text=cls.active_customer.phone_number)
        customer_phone_text.grid(column=20, row=2, columnspan=5)
        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=25, row=1, columnspan=10)
        customer_email_text = ttk.Label(area, text=cls.active_customer.email)
        customer_email_text.grid(column=25, row=2, columnspan=10)
        customer_accounts_label = ttk.Label(area, text="Customer accounts")
        customer_accounts_label.grid(column=0, row=5, columnspan=10)
        customer_accounts = ttk.Treeview(area, height=5)
        customer_accounts.grid(column=0, row=6, columnspan=40, rowspan=5)
        customer_accounts['columns'] = ('account_number', 'account_type', 'account_balance', 'account_transfer_amount', 'account_transfer_quantity')
        customer_accounts.column("#0", width=0, stretch=False)
        customer_accounts.column("account_number", anchor="center", width=100)
        customer_accounts.column("account_type", anchor="center", width=100)
        customer_accounts.column("account_balance", anchor="center", width=100)
        customer_accounts.column("account_transfer_amount", anchor="center", width=100)
        customer_accounts.column("account_transfer_quantity", anchor="center", width=100)
        customer_accounts.heading("#0", text="", anchor="center")
        customer_accounts.heading("account_number", text="NUMBER", anchor="center")
        customer_accounts.heading("account_type", text="TYPE", anchor="center")
        customer_accounts.heading("account_balance", text="BALANCE", anchor="center")
        customer_accounts.heading("account_transfer_amount", text="TRANSFERRED", anchor="center")
        customer_accounts.heading("account_transfer_quantity", text="TRANSFERS", anchor="center")
        accounts_results_button = ttk.Button(area, width=20, text="View account", command=action_account)
        accounts_results_button.grid(column=40, row=6, columnspan=8, rowspan=5)
        update_customer_button = ttk.Button(area, width=20, text="Update customer", command=action_update_customer)
        update_customer_button.grid(column=40, row=1, columnspan=8)
        delete_customer_button = ttk.Button(area, width=20, text="Delete customer", command=action_delete_customer)
        delete_customer_button.grid(column=40, row=2, columnspan=8)
        open_account_button = ttk.Button(area, width=20, text="Open account", command=action_open_account)
        open_account_button.grid(column=40, row=3, columnspan=8)
        chart_button = ttk.Button(area, width=20, text="Money chart", command=action_money_chart)
        chart_button.grid(column=40, row=4, columnspan=8)
        cls.accounts = util.view_customer(cls.active_customer.customer_id, cls.result)
        if cls.result.code == "00":
            for i in cls.accounts:
                customer_accounts.insert(parent='', index='end', values=(i.acc_number, i.acc_type.product_type, i.balance, i.transfer_amount, i.transfer_quantity, i.customer_id, i.open_date))
        else:
            if cls.result.code != "99":
                tk.messagebox.showinfo('PyBank', cls.result.code + " - " + cls.result.message)
            else:
                tk.messagebox.showerror('PyBank', cls.result.code + " - " + cls.result.message)

    @classmethod
    def new_customer(cls):
        def action_confirm():
            re_phone = re.compile(r'([1-9]{3})\W*(\d{3})\W*(\d{4})\W*(\d*)$')
            re_email = re.compile(r'([A-Za-z\d]+[.-_])*[A-Za-z\d]+@[A-Za-z\d-]+(\.[A-Z|a-z]{2,})+$')
            re_pin = re.compile(r'\d{4}$')
            if customer_pin.get() != "" and customer_first_name.get() != "" and customer_last_name.get() != "" and customer_address.get() != "" and customer_phone.get() != "" and customer_email.get() != "":
                if not re.fullmatch(re_phone, customer_phone.get()):
                    tk.messagebox.showerror('PyBank', 'Phone not valid')
                elif not re.fullmatch(re_email, customer_email.get()):
                    tk.messagebox.showerror('PyBank', 'Email not valid')
                elif not re.fullmatch(re_pin, customer_pin.get()):
                    tk.messagebox.showerror('PyBank', 'PIN not valid')
                else:
                    cls.active_customer.pin=customer_pin.get()
                    cls.active_customer.first_name=customer_first_name.get()
                    cls.active_customer.last_name=customer_last_name.get()
                    cls.active_customer.address=customer_address.get()
                    cls.active_customer.phone_number=customer_phone.get()
                    cls.active_customer.email=customer_email.get()
                    cls.active_customer.agent_id=cls.active_agent.username
                    util.create_customer(cls.active_customer, cls.result)
                    if cls.result.code == "00":
                        tk.messagebox.showinfo('PyBank', 'Customer ' + str(cls.active_customer.customer_id) + ' created')
                        area.destroy()
                        cls.view_customer()
                    else:
                        tk.messagebox.showerror('PyBank', cls.result.code + " - " + cls.result.message)
            else:
                tk.messagebox.showerror('PyBank', 'All fields are required')
        def action_cancel():
            area.destroy()
            cls.search()
        cls.window.geometry(cls.window_size)
        cls.create_top_menu()
        area = ttk.LabelFrame(cls.window, text="New customer")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=5, row=2, columnspan=10)
        customer_first_name = tk.StringVar()
        customer_first_name_text = ttk.Entry(area, width=50, textvariable=customer_first_name)
        customer_first_name_text.grid(column=15, row=2, columnspan=20)
        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=5, row=3, columnspan=10)
        customer_last_name = tk.StringVar()
        customer_last_name_text = ttk.Entry(area, width=50, textvariable=customer_last_name)
        customer_last_name_text.grid(column=15, row=3, columnspan=20)
        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=5, row=4, columnspan=10)
        customer_address = tk.StringVar()
        customer_address_text = ttk.Entry(area, width=50, textvariable=customer_address)
        customer_address_text.grid(column=15, row=4, columnspan=20)
        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=5, row=5, columnspan=10)
        customer_phone = tk.StringVar()
        customer_phone_text = ttk.Entry(area, width=20, textvariable=customer_phone)
        customer_phone_text.grid(column=15, row=5, columnspan=20)
        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=5, row=6, columnspan=10)
        customer_email = tk.StringVar()
        customer_email_text = ttk.Entry(area, width=30, textvariable=customer_email)
        customer_email_text.grid(column=15, row=6, columnspan=20)
        customer_pin_label = ttk.Label(area, text="PIN")
        customer_pin_label.grid(column=5, row=7, columnspan=10)
        customer_pin = tk.StringVar()
        customer_pin_text = ttk.Entry(area, width=10, show='*', textvariable=customer_pin)
        customer_pin_text.grid(column=15, row=7, columnspan=20)
        confirm_button = ttk.Button(area, width=20, text="Confirm", command=action_confirm)
        confirm_button.grid(column=40, row=1, columnspan=8)
        cancel_button = ttk.Button(area, width=20, text="Cancel", command=action_cancel)
        cancel_button.grid(column=40, row=2, columnspan=8)

    @classmethod
    def update_customer(cls):
        def action_confirm():
            re_phone = re.compile(r'([1-9]{3})\W*(\d{3})\W*(\d{4})\W*(\d*)$')
            re_pin = re.compile(r'\d{4}$')
            if customer_pin.get() != "" and customer_first_name.get() != "" and customer_last_name.get() != "" and customer_address.get() != "" and customer_phone.get() != "":
                if not re.fullmatch(re_phone, customer_phone.get()):
                    tk.messagebox.showerror('PyBank', 'Phone not valid')
                elif not re.fullmatch(re_pin, customer_pin.get()):
                    tk.messagebox.showerror('PyBank', 'PIN not valid')
                else:
                    cls.active_customer.pin=customer_pin.get()
                    cls.active_customer.first_name=customer_first_name.get()
                    cls.active_customer.last_name=customer_last_name.get()
                    cls.active_customer.address=customer_address.get()
                    cls.active_customer.phone_number=customer_phone.get()
                    util.update_customer(cls.active_customer, cls.result)
                    if cls.result.code == "00":
                        tk.messagebox.showinfo('PyBank', 'Customer ' + str(cls.active_customer.customer_id) + ' updated')
                        area.destroy()
                        cls.view_customer()
                    else:
                        tk.messagebox.showerror('PyBank', cls.result.code + " - " + cls.result.message)
            else:
                tk.messagebox.showerror('PyBank', 'All fields are required')
        def action_cancel():
            area.destroy()
            cls.view_customer()
        area = ttk.LabelFrame(cls.window, text="Update customer")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=5, row=2, columnspan=10)
        customer_first_name = tk.StringVar()
        customer_first_name_text = ttk.Entry(area, width=50, textvariable=customer_first_name)
        customer_first_name_text.grid(column=15, row=2, columnspan=20)
        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=5, row=3, columnspan=10)
        customer_last_name = tk.StringVar()
        customer_last_name_text = ttk.Entry(area, width=50, textvariable=customer_last_name)
        customer_last_name_text.grid(column=15, row=3, columnspan=20)
        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=5, row=4, columnspan=10)
        customer_address = tk.StringVar()
        customer_address_text = ttk.Entry(area, width=50, textvariable=customer_address)
        customer_address_text.grid(column=15, row=4, columnspan=20)
        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=5, row=5, columnspan=10)
        customer_phone = tk.StringVar()
        customer_phone_text = ttk.Entry(area, width=20, textvariable=customer_phone)
        customer_phone_text.grid(column=15, row=5, columnspan=20)
        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=5, row=6, columnspan=10)
        customer_email_text = ttk.Label(area, text=cls.active_customer.email)
        customer_email_text.grid(column=15, row=6, columnspan=20)
        customer_pin_label = ttk.Label(area, text="PIN")
        customer_pin_label.grid(column=5, row=7, columnspan=10)
        customer_pin = tk.StringVar()
        customer_pin_text = ttk.Entry(area, width=10, show='*', textvariable=customer_pin)
        customer_pin_text.grid(column=15, row=7, columnspan=20)
        customer_first_name_text.insert(0, cls.active_customer.first_name)
        customer_last_name_text.insert(0, cls.active_customer.last_name)
        customer_address_text.insert(0, cls.active_customer.address)
        customer_phone_text.insert(0, cls.active_customer.phone_number)
        customer_pin_text.insert(0, cls.active_customer.pin)
        confirm_button = ttk.Button(area, width=20, text="Confirm", command=action_confirm)
        confirm_button.grid(column=40, row=1, columnspan=8)
        cancel_button = ttk.Button(area, width=20, text="Cancel", command=action_cancel)
        cancel_button.grid(column=40, row=2, columnspan=8)
        customer_pin_label.insert(0, '1234') #Error to print correctly GUI?

    @classmethod
    def delete_customer(cls):
        def action_confirm():
            util.delete_customer(cls.active_agent, cls.active_customer, cls.result)
            if cls.result.code == "00":
                tk.messagebox.showinfo('PyBank', 'Customer ' + str(cls.active_customer.customer_id) + ' deleted')
                area.destroy()
                cls.search()
            else:
                tk.messagebox.showerror('PyBank', cls.result.code + " - " + cls.result.message)
        def action_cancel():
            area.destroy()
            cls.view_customer()
        cls.window.geometry(cls.window_size)
        cls.create_top_menu()
        area = ttk.LabelFrame(cls.window, text="Delete customer")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=5, row=2, columnspan=10)
        customer_first_name_text = ttk.Label(area, text=cls.active_customer.first_name)
        customer_first_name_text.grid(column=15, row=2, columnspan=20)
        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=5, row=3, columnspan=10)
        customer_last_name_text = ttk.Label(area, text=cls.active_customer.last_name)
        customer_last_name_text.grid(column=15, row=3, columnspan=20)
        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=5, row=4, columnspan=10)
        customer_address_text = ttk.Label(area, text=cls.active_customer.address)
        customer_address_text.grid(column=15, row=4, columnspan=20)
        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=5, row=5, columnspan=10)
        customer_phone_text = ttk.Label(area, text=cls.active_customer.phone_number)
        customer_phone_text.grid(column=15, row=5, columnspan=20)
        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=5, row=6, columnspan=10)
        customer_email_text = ttk.Label(area, text=cls.active_customer.email)
        customer_email_text.grid(column=15, row=6, columnspan=20)
        confirm_button = ttk.Button(area, width=20, text="Confirm", command=action_confirm)
        confirm_button.grid(column=40, row=1, columnspan=8)
        cancel_button = ttk.Button(area, width=20, text="Cancel", command=action_cancel)
        cancel_button.grid(column=40, row=2, columnspan=8)

    @classmethod
    def view_account(cls):
        def action_deposit():
            area.destroy()
            cls.deposit()
        def action_withdrawal():
            area.destroy()
            cls.withdrawal()
        def action_transfer():
            area.destroy()
            cls.transfer()
        def action_close_account():
            area.destroy()
            cls.close_account()
        def action_advisor():
            try:
                income = 0
                outcome = 0
                fees = 0
                for i in cls.movements:
                    if i.source_account == cls.active_account.acc_number:
                        if i.transaction_id == 10:
                            fees += i.amount
                        else:
                            outcome += i.amount
                    if i.destination_account == cls.active_account.acc_number:
                        income += i.amount
                plt.title("Money advisor")
                for i in plt.bar(["Income", "Outcome", "Fees"], [income, outcome, fees], color=["Green", "Red", "Gray"]):
                    y_value = i.get_height()
                    plt.text(i.get_x() + i.get_width() / 3, y_value, "$" + str(y_value), va="bottom")
                plt.show()
            except TypeError as e:
                tk.messagebox.showerror('PyBank', 'Account has no movements')
        cls.window.geometry(cls.window_size)
        cls.create_top_menu()
        area = ttk.LabelFrame(cls.window, text="View account")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        customer_id_label = ttk.Label(area, text="ID")
        customer_id_label.grid(column=0, row=1, columnspan=5)
        customer_id_text = ttk.Label(area, text=cls.active_customer.customer_id)
        customer_id_text.grid(column=0, row=2, columnspan=5)
        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=5, row=1, columnspan=5)
        customer_first_name_text = ttk.Label(area, text=cls.active_customer.first_name)
        customer_first_name_text.grid(column=5, row=2, columnspan=5)
        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=10, row=1, columnspan=5)
        customer_last_name_text = ttk.Label(area, text=cls.active_customer.last_name)
        customer_last_name_text.grid(column=10, row=2, columnspan=5)
        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=15, row=1, columnspan=5)
        customer_address_text = ttk.Label(area, text=cls.active_customer.address)
        customer_address_text.grid(column=15, row=2, columnspan=5)
        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=20, row=1, columnspan=5)
        customer_phone_text = ttk.Label(area, text=cls.active_customer.phone_number)
        customer_phone_text.grid(column=20, row=2, columnspan=5)
        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=25, row=1, columnspan=10)
        customer_email_text = ttk.Label(area, text=cls.active_customer.email)
        customer_email_text.grid(column=25, row=2, columnspan=10)
        account_number_label = ttk.Label(area, text="Account number")
        account_number_label.grid(column=5, row=4, columnspan=5)
        account_number_text = ttk.Label(area, text=cls.active_account.acc_number)
        account_number_text.grid(column=5, row=5, columnspan=5)
        account_type_label = ttk.Label(area, text="Account type")
        account_type_label.grid(column=10, row=4, columnspan=5)
        account_type_text = ttk.Label(area, text=cls.active_account.acc_type.product_type)
        account_type_text.grid(column=10, row=5, columnspan=5)
        account_balance_label = ttk.Label(area, text="Balance")
        account_balance_label.grid(column=15, row=4, columnspan=5)
        account_balance_text = ttk.Label(area, text=cls.active_account.balance)
        account_balance_text.grid(column=15, row=5, columnspan=5)
        transferred_label = ttk.Label(area, text="Transferred")
        transferred_label.grid(column=20, row=4, columnspan=5)
        transferred_text = ttk.Label(area, text=cls.active_account.transfer_amount)
        transferred_text.grid(column=20, row=5, columnspan=5)
        transfers_label = ttk.Label(area, text="Transfers")
        transfers_label.grid(column=25, row=4, columnspan=5)
        transfers_text = ttk.Label(area, text=cls.active_account.transfer_quantity)
        transfers_text.grid(column=25, row=5, columnspan=5)
        customer_accounts_label = ttk.Label(area, text="Account movements")
        customer_accounts_label.grid(column=0, row=7, columnspan=10)
        account_movements = ttk.Treeview(area, height=5)
        account_movements.grid(column=0, row=8, columnspan=40, rowspan=5)
        account_movements['columns'] = ('date', 'transaction', 'source_account', 'destination_account', 'amount')
        account_movements.column("#0", width=0, stretch=False)
        account_movements.column("date", anchor="center", width=200)
        account_movements.column("transaction", anchor="center", width=100)
        account_movements.column("source_account", anchor="center", width=100)
        account_movements.column("destination_account", anchor="center", width=100)
        account_movements.column("amount", anchor="center", width=100)
        account_movements.heading("#0", text="", anchor="center")
        account_movements.heading("date", text="DATE", anchor="center")
        account_movements.heading("transaction", text="TRANSACTION", anchor="center")
        account_movements.heading("source_account", text="SOURCE", anchor="center")
        account_movements.heading("destination_account", text="DESTINATION", anchor="center")
        account_movements.heading("amount", text="AMOUNT", anchor="center")
        deposit_button = ttk.Button(area, width=20, text="Deposit", command=action_deposit)
        deposit_button.grid(column=40, row=1, columnspan=8)
        withdrawal_button = ttk.Button(area, width=20, text="Withdrawal", command=action_withdrawal)
        withdrawal_button.grid(column=40, row=2, columnspan=8)
        transfer_button = ttk.Button(area, width=20, text="Transfer", command=action_transfer)
        transfer_button.grid(column=40, row=3, columnspan=8)
        action_advisor = ttk.Button(area, width=20, text="Money advisor", command=action_advisor)
        action_advisor.grid(column=40, row=4, columnspan=8)
        delete_account_button = ttk.Button(area, width=20, text="Close account", command=action_close_account)
        delete_account_button.grid(column=40, row=5, columnspan=8)
        cls.movements = util.view_account(cls.active_account.acc_number, cls.result)
        if cls.result.code == "00":
            for i in cls.movements:
                account_movements.insert(parent='', index='end', values=(i.movement_date, i.description, i.source_account, i.destination_account, i.amount))
        else:
            if cls.result.code != "99":
                tk.messagebox.showinfo('PyBank', cls.result.code + " - " + cls.result.message)
            else:
                tk.messagebox.showerror('PyBank', cls.result.code + " - " + cls.result.message)

    @classmethod
    def open_account(cls):
        def get_account_features():
            new_account = Product(account_type.get())
            interest_rate_label.configure(text=str(round(new_account.interest_rate*100, 1)) + "%")
            amount_limit_label.configure(text=new_account.amount_limit)
            quantity_limit_label.configure(text=new_account.quantity_limit)
            minimum_balance_label.configure(text=new_account.minimum_balance)
        def action_confirm():
            if account_type.get() >= 1 and account_type.get() <= 3:
                cls.active_account = Account(acc_number="", acc_type_id=account_type.get(), balance=0.0, transfer_amount=0.0, transfer_quantity=0, customer_id=cls.active_customer.customer_id, open_date=datetime.now(), agent_id=cls.active_agent.username)
                util.open_account(cls.active_account, cls.result)
                if cls.result.code == "00":
                    tk.messagebox.showinfo('PyBank', 'Account ' + cls.active_account.acc_number + ' opened')
                    area.destroy()
                    cls.view_account()
                else:
                    tk.messagebox.showerror('PyBank', cls.result.code + " - " + cls.result.message)
            else:
                tk.messagebox.showerror('PyBank', "Select an account type")
        def action_cancel():
            area.destroy()
            cls.view_customer()
        cls.window.geometry(cls.window_size)
        cls.create_top_menu()
        area = ttk.LabelFrame(cls.window, text="Open account")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        customer_id_label = ttk.Label(area, text="ID")
        customer_id_label.grid(column=0, row=1, columnspan=5)
        customer_id_text = ttk.Label(area, text=cls.active_customer.customer_id)
        customer_id_text.grid(column=0, row=2, columnspan=5)
        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=5, row=1, columnspan=5)
        customer_first_name_text = ttk.Label(area, text=cls.active_customer.first_name)
        customer_first_name_text.grid(column=5, row=2, columnspan=5)
        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=10, row=1, columnspan=5)
        customer_last_name_text = ttk.Label(area, text=cls.active_customer.last_name)
        customer_last_name_text.grid(column=10, row=2, columnspan=5)
        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=15, row=1, columnspan=5)
        customer_address_text = ttk.Label(area, text=cls.active_customer.address)
        customer_address_text.grid(column=15, row=2, columnspan=5)
        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=20, row=1, columnspan=5)
        customer_phone_text = ttk.Label(area, text=cls.active_customer.phone_number)
        customer_phone_text.grid(column=20, row=2, columnspan=5)
        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=25, row=1, columnspan=10)
        customer_email_text = ttk.Label(area, text=cls.active_customer.email)
        customer_email_text.grid(column=25, row=2, columnspan=10)
        account_type_frame = ttk.LabelFrame(area, text="Account type")
        account_type_frame.grid(column=5, row=5, padx=20, columnspan=5, rowspan=4)
        account_type_values = ["Checking", "Saving", "Investing"]
        account_type = tk.IntVar()
        for i in range(3):
            account_type_radio = tk.Radiobutton(account_type_frame, text=account_type_values[i], variable=account_type, value=i+1, command=get_account_features)
            account_type_radio.grid(column=0, row=i)
        interest_label = ttk.Label(area, text="Interest rate")
        interest_label.grid(column=10, row=5, columnspan=5)
        interest_rate_label = ttk.Label(area)
        interest_rate_label.grid(column=10, row=6, columnspan=5)
        amount_label = ttk.Label(area, text="Amount limit")
        amount_label.grid(column=15, row=5, columnspan=5)
        amount_limit_label = ttk.Label(area)
        amount_limit_label.grid(column=15, row=6, columnspan=5)
        quantity_label = ttk.Label(area, text="Quantity limit")
        quantity_label.grid(column=20, row=5, columnspan=5)
        quantity_limit_label = ttk.Label(area)
        quantity_limit_label.grid(column=20, row=6, columnspan=5)
        balance_label = ttk.Label(area, text="Minimum balance")
        balance_label.grid(column=25, row=5, columnspan=5)
        minimum_balance_label = ttk.Label(area)
        minimum_balance_label.grid(column=25, row=6, columnspan=5)
        confirm_button = ttk.Button(area, width=20, text="Confirm", command=action_confirm)
        confirm_button.grid(column=40, row=1, columnspan=8)
        cancel_button = ttk.Button(area, width=20, text="Cancel", command=action_cancel)
        cancel_button.grid(column=40, row=2, columnspan=8)

    @classmethod
    def close_account(cls):
        def action_confirm():
            temp_balance = str(cls.active_account.balance)
            util.delete_account(cls.active_agent, cls.active_account, cls.result)
            if cls.result.code == "00":
                tk.messagebox.showinfo('PyBank', 'Account ' + cls.active_account.acc_number + ' closed')
                area.destroy()
                cls.view_customer()
            else:
                if cls.result.code == "05":
                    tk.messagebox.showinfo('PyBank', 'Account ' + cls.active_account.acc_number + ' closed\nCash refunded: $' + temp_balance)
                    area.destroy()
                    cls.view_customer()
                else:
                    tk.messagebox.showerror('PyBank', cls.result.code + " - " + cls.result.message)
        def action_cancel():
            area.destroy()
            cls.view_account()
        cls.window.geometry(cls.window_size)
        cls.create_top_menu()
        area = ttk.LabelFrame(cls.window, text="Close account")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        customer_id_label = ttk.Label(area, text="ID")
        customer_id_label.grid(column=0, row=1, columnspan=5)
        customer_id_text = ttk.Label(area, text=cls.active_customer.customer_id)
        customer_id_text.grid(column=0, row=2, columnspan=5)
        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=5, row=1, columnspan=5)
        customer_first_name_text = ttk.Label(area, text=cls.active_customer.first_name)
        customer_first_name_text.grid(column=5, row=2, columnspan=5)
        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=10, row=1, columnspan=5)
        customer_last_name_text = ttk.Label(area, text=cls.active_customer.last_name)
        customer_last_name_text.grid(column=10, row=2, columnspan=5)
        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=15, row=1, columnspan=5)
        customer_address_text = ttk.Label(area, text=cls.active_customer.address)
        customer_address_text.grid(column=15, row=2, columnspan=5)
        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=20, row=1, columnspan=5)
        customer_phone_text = ttk.Label(area, text=cls.active_customer.phone_number)
        customer_phone_text.grid(column=20, row=2, columnspan=5)
        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=25, row=1, columnspan=10)
        customer_email_text = ttk.Label(area, text=cls.active_customer.email)
        customer_email_text.grid(column=25, row=2, columnspan=10)
        account_number_label = ttk.Label(area, text="Account number")
        account_number_label.grid(column=5, row=4, columnspan=5)
        account_number_text = ttk.Label(area, text=cls.active_account.acc_number)
        account_number_text.grid(column=5, row=5, columnspan=5)
        account_type_label = ttk.Label(area, text="Account type")
        account_type_label.grid(column=10, row=4, columnspan=5)
        account_type_text = ttk.Label(area, text=cls.active_account.acc_type.product_type)
        account_type_text.grid(column=10, row=5, columnspan=5)
        account_balance_label = ttk.Label(area, text="Balance")
        account_balance_label.grid(column=15, row=4, columnspan=5)
        account_balance_text = ttk.Label(area, text=cls.active_account.balance)
        account_balance_text.grid(column=15, row=5, columnspan=5)
        transferred_label = ttk.Label(area, text="Transferred")
        transferred_label.grid(column=20, row=4, columnspan=5)
        transferred_text = ttk.Label(area, text=cls.active_account.transfer_amount)
        transferred_text.grid(column=20, row=5, columnspan=5)
        transfers_label = ttk.Label(area, text="Transfers")
        transfers_label.grid(column=25, row=4, columnspan=5)
        transfers_text = ttk.Label(area, text=cls.active_account.transfer_quantity)
        transfers_text.grid(column=25, row=5, columnspan=5)
        confirm_button = ttk.Button(area, width=20, text="Confirm", command=action_confirm)
        confirm_button.grid(column=40, row=1, columnspan=8)
        cancel_button = ttk.Button(area, width=20, text="Cancel", command=action_cancel)
        cancel_button.grid(column=40, row=2, columnspan=8)

    @classmethod
    def deposit(cls):
        def action_confirm():
            re_amount = re.compile(r'[1-9]\d*(\.\d{2})*')
            if re.fullmatch(re_amount, amount.get()):
                cls.active_movement = Movement(destination_account=cls.active_account.acc_number, amount=float(amount.get()), transaction_id=7, agent_id=cls.active_agent.username)
                util.deposit(cls.active_movement, cls.active_account, cls.result)
                if cls.result.code == "00":
                    tk.messagebox.showinfo('PyBank', 'Deposit successful')
                    area.destroy()
                    cls.view_account()
                else:
                    tk.messagebox.showerror('PyBank', cls.result.code + " - " + cls.result.message)
            else:
                tk.messagebox.showerror('PyBank', "Amount not valid")
        def action_cancel():
            area.destroy()
            cls.view_account()
        cls.window.geometry(cls.window_size)
        cls.create_top_menu()
        area = ttk.LabelFrame(cls.window, text="Deposit")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        customer_id_label = ttk.Label(area, text="ID")
        customer_id_label.grid(column=0, row=1, columnspan=5)
        customer_id_text = ttk.Label(area, text=cls.active_customer.customer_id)
        customer_id_text.grid(column=0, row=2, columnspan=5)
        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=5, row=1, columnspan=5)
        customer_first_name_text = ttk.Label(area, text=cls.active_customer.first_name)
        customer_first_name_text.grid(column=5, row=2, columnspan=5)
        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=10, row=1, columnspan=5)
        customer_last_name_text = ttk.Label(area, text=cls.active_customer.last_name)
        customer_last_name_text.grid(column=10, row=2, columnspan=5)
        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=15, row=1, columnspan=5)
        customer_address_text = ttk.Label(area, text=cls.active_customer.address)
        customer_address_text.grid(column=15, row=2, columnspan=5)
        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=20, row=1, columnspan=5)
        customer_phone_text = ttk.Label(area, text=cls.active_customer.phone_number)
        customer_phone_text.grid(column=20, row=2, columnspan=5)
        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=25, row=1, columnspan=10)
        customer_email_text = ttk.Label(area, text=cls.active_customer.email)
        customer_email_text.grid(column=25, row=2, columnspan=10)
        account_number_label = ttk.Label(area, text="Account number")
        account_number_label.grid(column=5, row=4, columnspan=5)
        account_number_text = ttk.Label(area, text=cls.active_account.acc_number)
        account_number_text.grid(column=5, row=5, columnspan=5)
        account_type_label = ttk.Label(area, text="Account type")
        account_type_label.grid(column=10, row=4, columnspan=5)
        account_type_text = ttk.Label(area, text=cls.active_account.acc_type.product_type)
        account_type_text.grid(column=10, row=5, columnspan=5)
        account_balance_label = ttk.Label(area, text="Balance")
        account_balance_label.grid(column=15, row=4, columnspan=5)
        account_balance_text = ttk.Label(area, text=cls.active_account.balance)
        account_balance_text.grid(column=15, row=5, columnspan=5)
        transferred_label = ttk.Label(area, text="Transferred")
        transferred_label.grid(column=20, row=4, columnspan=5)
        transferred_text = ttk.Label(area, text=cls.active_account.transfer_amount)
        transferred_text.grid(column=20, row=5, columnspan=5)
        transfers_label = ttk.Label(area, text="Transfers")
        transfers_label.grid(column=25, row=4, columnspan=5)
        transfers_text = ttk.Label(area, text=cls.active_account.transfer_quantity)
        transfers_text.grid(column=25, row=5, columnspan=5)
        amount_label = ttk.Label(area, text="Deposit amount")
        amount_label.grid(column=10, row=7, columnspan=5)
        amount = tk.StringVar()
        amount_text = ttk.Entry(area, width=30, textvariable=amount)
        amount_text.grid(column=15, row=7, columnspan=10)
        confirm_button = ttk.Button(area, width=20, text="Confirm", command=action_confirm)
        confirm_button.grid(column=40, row=1, columnspan=8)
        cancel_button = ttk.Button(area, width=20, text="Cancel", command=action_cancel)
        cancel_button.grid(column=40, row=2, columnspan=8)

    @classmethod
    def withdrawal(cls):
        def action_confirm():
            re_amount = re.compile(r'[1-9]\d*(\.\d{2})*')
            re_pin = re.compile(r'\d{4}$')
            if amount.get() != "" and pin.get():
                if re.fullmatch(re_amount, amount.get()):
                    if re.fullmatch(re_pin, pin.get()):
                        if cls.active_customer.pin == pin.get():
                            cls.active_movement = Movement(source_account=cls.active_account.acc_number, amount=float(amount.get()), transaction_id=8, agent_id=cls.active_agent.username)
                            util.withdrawal(cls.active_movement, cls.active_account, cls.result)
                            if cls.result.code == "00":
                                tk.messagebox.showinfo('PyBank', 'Withdrawal successful')
                                area.destroy()
                                cls.view_account()
                            else:
                                tk.messagebox.showerror('PyBank', cls.result.code + " - " + cls.result.message)
                        else:
                            tk.messagebox.showerror('PyBank', "PIN incorrect")
                    else:
                        tk.messagebox.showerror('PyBank', "PIN not valid")
                else:
                    tk.messagebox.showerror('PyBank', "Amount not valid")
            else:
                tk.messagebox.showerror('PyBank', 'All fields are required')
        def action_cancel():
            area.destroy()
            cls.view_account()
        cls.window.geometry(cls.window_size)
        cls.create_top_menu()
        area = ttk.LabelFrame(cls.window, text="Withdrawal")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        customer_id_label = ttk.Label(area, text="ID")
        customer_id_label.grid(column=0, row=1, columnspan=5)
        customer_id_text = ttk.Label(area, text=cls.active_customer.customer_id)
        customer_id_text.grid(column=0, row=2, columnspan=5)
        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=5, row=1, columnspan=5)
        customer_first_name_text = ttk.Label(area, text=cls.active_customer.first_name)
        customer_first_name_text.grid(column=5, row=2, columnspan=5)
        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=10, row=1, columnspan=5)
        customer_last_name_text = ttk.Label(area, text=cls.active_customer.last_name)
        customer_last_name_text.grid(column=10, row=2, columnspan=5)
        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=15, row=1, columnspan=5)
        customer_address_text = ttk.Label(area, text=cls.active_customer.address)
        customer_address_text.grid(column=15, row=2, columnspan=5)
        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=20, row=1, columnspan=5)
        customer_phone_text = ttk.Label(area, text=cls.active_customer.phone_number)
        customer_phone_text.grid(column=20, row=2, columnspan=5)
        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=25, row=1, columnspan=10)
        customer_email_text = ttk.Label(area, text=cls.active_customer.email)
        customer_email_text.grid(column=25, row=2, columnspan=10)
        account_number_label = ttk.Label(area, text="Account number")
        account_number_label.grid(column=5, row=4, columnspan=5)
        account_number_text = ttk.Label(area, text=cls.active_account.acc_number)
        account_number_text.grid(column=5, row=5, columnspan=5)
        account_type_label = ttk.Label(area, text="Account type")
        account_type_label.grid(column=10, row=4, columnspan=5)
        account_type_text = ttk.Label(area, text=cls.active_account.acc_type.product_type)
        account_type_text.grid(column=10, row=5, columnspan=5)
        account_balance_label = ttk.Label(area, text="Balance")
        account_balance_label.grid(column=15, row=4, columnspan=5)
        account_balance_text = ttk.Label(area, text=cls.active_account.balance)
        account_balance_text.grid(column=15, row=5, columnspan=5)
        transferred_label = ttk.Label(area, text="Transferred")
        transferred_label.grid(column=20, row=4, columnspan=5)
        transferred_text = ttk.Label(area, text=cls.active_account.transfer_amount)
        transferred_text.grid(column=20, row=5, columnspan=5)
        transfers_label = ttk.Label(area, text="Transfers")
        transfers_label.grid(column=25, row=4, columnspan=5)
        transfers_text = ttk.Label(area, text=cls.active_account.transfer_quantity)
        transfers_text.grid(column=25, row=5, columnspan=5)
        amount_label = ttk.Label(area, text="Withdrawal amount")
        amount_label.grid(column=10, row=7, columnspan=5)
        amount = tk.StringVar()
        amount_text = ttk.Entry(area, width=30, textvariable=amount)
        amount_text.grid(column=15, row=7, columnspan=10)
        pin_label = ttk.Label(area, text="Pin")
        pin_label.grid(column=10, row=8, columnspan=5)
        pin = tk.StringVar()
        pin_text = ttk.Entry(area, width=10, show='*', textvariable=pin)
        pin_text.grid(column=15, row=8, columnspan=10)
        confirm_button = ttk.Button(area, width=20, text="Confirm", command=action_confirm)
        confirm_button.grid(column=40, row=1, columnspan=8)
        cancel_button = ttk.Button(area, width=20, text="Cancel", command=action_cancel)
        cancel_button.grid(column=40, row=2, columnspan=8)

    @classmethod
    def transfer(cls):
        def action_confirm():
            re_destination = re.compile(r'\d{9}$')
            re_amount = re.compile(r'[1-9]\d*(\.\d{2})*')
            re_pin = re.compile(r'\d{4}$')
            if destination.get() != "" and amount.get() != "" and pin.get():
                if re.fullmatch(re_destination, destination.get()):
                    if re.fullmatch(re_amount, amount.get()):
                        if re.fullmatch(re_pin, pin.get()):
                            if cls.active_customer.pin == pin.get():
                                cls.active_movement = Movement(source_account=cls.active_account.acc_number, destination_account=destination.get(), amount=float(amount.get()), transaction_id=9, agent_id=cls.active_agent.username)
                                util.transfer(cls.active_movement, cls.active_account, cls.result)
                                if cls.result.code == "00":
                                    tk.messagebox.showinfo('PyBank', 'Transfer successful')
                                    area.destroy()
                                    cls.view_account()
                                else:
                                    tk.messagebox.showerror('PyBank', cls.result.code + " - " + cls.result.message)
                            else:
                                tk.messagebox.showerror('PyBank', "PIN incorrect")
                        else:
                            tk.messagebox.showerror('PyBank', "PIN not valid")
                    else:
                        tk.messagebox.showerror('PyBank', "Amount not valid")
                else:
                    tk.messagebox.showerror('PyBank', "Destination account not valid")
            else:
                tk.messagebox.showerror('PyBank', 'All fields are required')
        def action_cancel():
            area.destroy()
            cls.view_account()
        cls.window.geometry(cls.window_size)
        cls.create_top_menu()
        area = ttk.LabelFrame(cls.window, text="Transfer")
        area.grid(column=1, row=1, columnspan=47, rowspan=14)
        cls.create_grid_window()
        cls.create_grid_area(area)
        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=35, row=0, columnspan=15)
        customer_id_label = ttk.Label(area, text="ID")
        customer_id_label.grid(column=0, row=1, columnspan=5)
        customer_id_text = ttk.Label(area, text=cls.active_customer.customer_id)
        customer_id_text.grid(column=0, row=2, columnspan=5)
        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=5, row=1, columnspan=5)
        customer_first_name_text = ttk.Label(area, text=cls.active_customer.first_name)
        customer_first_name_text.grid(column=5, row=2, columnspan=5)
        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=10, row=1, columnspan=5)
        customer_last_name_text = ttk.Label(area, text=cls.active_customer.last_name)
        customer_last_name_text.grid(column=10, row=2, columnspan=5)
        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=15, row=1, columnspan=5)
        customer_address_text = ttk.Label(area, text=cls.active_customer.address)
        customer_address_text.grid(column=15, row=2, columnspan=5)
        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=20, row=1, columnspan=5)
        customer_phone_text = ttk.Label(area, text=cls.active_customer.phone_number)
        customer_phone_text.grid(column=20, row=2, columnspan=5)
        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=25, row=1, columnspan=10)
        customer_email_text = ttk.Label(area, text=cls.active_customer.email)
        customer_email_text.grid(column=25, row=2, columnspan=10)
        account_number_label = ttk.Label(area, text="Account number")
        account_number_label.grid(column=5, row=4, columnspan=5)
        account_number_text = ttk.Label(area, text=cls.active_account.acc_number)
        account_number_text.grid(column=5, row=5, columnspan=5)
        account_type_label = ttk.Label(area, text="Account type")
        account_type_label.grid(column=10, row=4, columnspan=5)
        account_type_text = ttk.Label(area, text=cls.active_account.acc_type.product_type)
        account_type_text.grid(column=10, row=5, columnspan=5)
        account_balance_label = ttk.Label(area, text="Balance")
        account_balance_label.grid(column=15, row=4, columnspan=5)
        account_balance_text = ttk.Label(area, text=cls.active_account.balance)
        account_balance_text.grid(column=15, row=5, columnspan=5)
        transferred_label = ttk.Label(area, text="Transferred")
        transferred_label.grid(column=20, row=4, columnspan=5)
        transferred_text = ttk.Label(area, text=cls.active_account.transfer_amount)
        transferred_text.grid(column=20, row=5, columnspan=5)
        transfers_label = ttk.Label(area, text="Transfers")
        transfers_label.grid(column=25, row=4, columnspan=5)
        transfers_text = ttk.Label(area, text=cls.active_account.transfer_quantity)
        transfers_text.grid(column=25, row=5, columnspan=5)
        destination_label = ttk.Label(area, text="Destination account")
        destination_label.grid(column=10, row=7, columnspan=5)
        destination = tk.StringVar()
        destination_text = ttk.Entry(area, width=30, textvariable=destination)
        destination_text.grid(column=15, row=7, columnspan=10)
        amount_label = ttk.Label(area, text="Transfer amount")
        amount_label.grid(column=10, row=8, columnspan=5)
        amount = tk.StringVar()
        amount_text = ttk.Entry(area, width=30, textvariable=amount)
        amount_text.grid(column=15, row=8, columnspan=10)
        pin_label = ttk.Label(area, text="Pin")
        pin_label.grid(column=10, row=9, columnspan=5)
        pin = tk.StringVar()
        pin_text = ttk.Entry(area, width=10, show='*', textvariable=pin)
        pin_text.grid(column=15, row=9, columnspan=10)
        confirm_button = ttk.Button(area, width=20, text="Confirm", command=action_confirm)
        confirm_button.grid(column=40, row=1, columnspan=8)
        cancel_button = ttk.Button(area, width=20, text="Cancel", command=action_cancel)
        cancel_button.grid(column=40, row=2, columnspan=8)
