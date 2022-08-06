from ui import *

class GUI:

    active_agent = Agent()
    window = tk.Tk()
    result = Return()

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
                    error_message.config(text=cls.result.message[1], foreground="Red")

        cls.window.title("PyBank")
        cls.window.geometry("450x400")

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
        menu_bar = Menu(cls.window)
        cls.window.config(menu=menu_bar)

        menu_agent = Menu(menu_bar, tearoff=0)
        menu_agent.add_command(label="Log in")
        menu_agent.add_command(label="Log out")
        menu_bar.add_cascade(label="Agent", menu=menu_agent)

        menu_customer = Menu(menu_bar, tearoff=0)
        menu_customer.add_command(label="Search")
        menu_customer.add_command(label="New customer")
        menu_bar.add_cascade(label="Customer", menu=menu_customer)

        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="About")
        menu_bar.add_cascade(label="Help", menu=menu_help)

    @classmethod
    def search(cls):
        def action_customer():
            area.destroy()
            cls.view_customer()

        def action_account():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Search customers and accounts")
        area.grid(column=0, row=1, padx=50, pady=20)

        search_label = ttk.Label(area, text="Search")
        search_label.grid(column=1, row=0, padx=20, pady=20, sticky="E")

        search_string = tk.StringVar()
        search_string_text = ttk.Entry(area, width=60, textvariable=search_string)
        search_string_text.grid(column=2, row=0, sticky="W")

        search_button = ttk.Button(area, text="Search", command=cls.search)
        search_button.grid(column=3, row=0, padx=40, sticky="E")

        customers_results_label = ttk.Label(area, text="Customers")
        customers_results_label.grid(column=0, row=1, padx=20, sticky="W")

        customers_results = ttk.Treeview(area)
        customers_results.grid(column=0, row=2, pady=10, columnspan=5)
        customers_results['columns'] = ('customer_id', 'customer_full_name', 'customer_address', 'customer_phone', 'customer_email')
        customers_results.column("#0", width=0, stretch=False)
        customers_results.column("customer_id", anchor="center", width=50)
        customers_results.column("customer_full_name", anchor="center", width=250)
        customers_results.column("customer_address", anchor="center", width=200)
        customers_results.column("customer_phone", anchor="center", width=100)
        customers_results.column("customer_email", anchor="center", width=250)
        customers_results.heading("#0", text="", anchor="center")
        customers_results.heading("customer_id", text="ID", anchor="center")
        customers_results.heading("customer_full_name", text="NAME", anchor="center")
        customers_results.heading("customer_address", text="ADDRESS", anchor="center")
        customers_results.heading("customer_phone", text="PHONE", anchor="center")
        customers_results.heading("customer_email", text="EMAIL", anchor="center")
        customers_results.insert(parent='', index='end', values=('1', 'Ninja Gaiden', '101 Weston', '1234567890', 'ryu@hotmail.com'))
        customers_results.insert(parent='', index='end', values=('2', 'Texas Ranger', '102 Melrose', '1234567890', 'ranger@hotmail.com'))
        customers_results.insert(parent='', index='end', values=('3', 'Blue Dragon', '104 Castleview', '1234567890', 'dragon@hotmail.com'))
        customers_results.insert(parent='', index='end', values=('4', 'Criss Cross', '105 California', '1234567890', 'kk@gmail.com'))
        customers_results.insert(parent='', index='end', values=('5', 'Tony Stark', '106 Wisconsin', '1234657890', 'tony@yahoo.com'))
        customers_results.insert(parent='', index='end', values=('6', 'Ninja Gaiden', '101 Weston', '1234567890', 'ryu@hotmail.com'))
        customers_results.insert(parent='', index='end', values=('7', 'Texas Ranger', '102 Melrose', '1234567890', 'ranger@hotmail.com'))
        customers_results.insert(parent='', index='end', values=('8', 'Blue Dragon', '104 Castleview', '1234567890', 'dragon@hotmail.com'))
        customers_results.insert(parent='', index='end', values=('9', 'Criss Cross', '105 California', '1234567890', 'kk@gmail.com'))
        customers_results.insert(parent='', index='end', values=('10', 'Tony Stark', '106 Wisconsin', '1234657890', 'tony@yahoo.com'))
        customers_results.insert(parent='', index='end', values=('11', 'Ninja Gaiden', '101 Weston', '1234567890', 'ryu@hotmail.com'))
        customers_results.insert(parent='', index='end', values=('12', 'Texas Ranger', '102 Melrose', '1234567890', 'ranger@hotmail.com'))
        customers_results.insert(parent='', index='end', values=('13', 'Blue Dragon', '104 Castleview', '1234567890', 'dragon@hotmail.com'))
        customers_results.insert(parent='', index='end', values=('14', 'Criss Cross', '105 California', '1234567890', 'kk@gmail.com'))
        customers_results.insert(parent='', index='end', values=('15', 'Tony Stark', '106 Wisconsin', '1234657890', 'tony@yahoo.com'))

        customers_results_button = ttk.Button(area, text="View customer", command=action_customer)
        customers_results_button.grid(column=5, row=2, padx=10)

        accounts_results_label = ttk.Label(area, text="Accounts")
        accounts_results_label.grid(column=0, row=3, padx=20, sticky="W")

        accounts_results = ttk.Treeview(area)
        accounts_results.grid(column=0, row=4, pady=10, columnspan=5)
        accounts_results['columns'] = ('account_number', 'account_type', 'customer_full_name', 'customer_address', 'customer_phone', 'customer_email')
        accounts_results.column("#0", width=0, stretch=False)
        accounts_results.column("account_number", anchor="center", width=100)
        accounts_results.column("account_type", anchor="center", width=100)
        accounts_results.column("customer_full_name", anchor="center", width=250)
        accounts_results.column("customer_address", anchor="center", width=200)
        accounts_results.column("customer_phone", anchor="center", width=100)
        accounts_results.column("customer_email", anchor="center", width=250)
        accounts_results.heading("#0", text="", anchor="center")
        accounts_results.heading("account_number", text="NUMBER", anchor="center")
        accounts_results.heading("account_type", text="TYPE", anchor="center")
        accounts_results.heading("customer_full_name", text="NAME", anchor="center")
        accounts_results.heading("customer_address", text="ADDRESS", anchor="center")
        accounts_results.heading("customer_phone", text="PHONE", anchor="center")
        accounts_results.heading("customer_email", text="EMAIL", anchor="center")
        accounts_results.insert(parent='', index='end', values=('109970001', 'Saving', 'Ninja Gaiden', '101 Weston', '1234567890', 'ryu@hotmail.com'))
        accounts_results.insert(parent='', index='end', values=('100043302', 'Invest', 'Texas Ranger', '102 Melrose', '1234567890', 'ranger@hotmail.com'))
        accounts_results.insert(parent='', index='end', values=('200654003', 'Checking', 'Blue Dragon', '104 Castleview', '1234567890', 'dragon@hotmail.com'))
        accounts_results.insert(parent='', index='end', values=('465204787', 'Checking', 'Criss Cross', '105 California', '1234567890', 'kk@gmail.com'))
        accounts_results.insert(parent='', index='end', values=('235000485', 'Saving', 'Tony Stark', '106 Wisconsin', '1234657890', 'tony@yahoo.com'))
        accounts_results.insert(parent='', index='end', values=('109970001', 'Saving', 'Ninja Gaiden', '101 Weston', '1234567890', 'ryu@hotmail.com'))
        accounts_results.insert(parent='', index='end', values=('100043302', 'Invest', 'Texas Ranger', '102 Melrose', '1234567890', 'ranger@hotmail.com'))
        accounts_results.insert(parent='', index='end', values=('200654003', 'Checking', 'Blue Dragon', '104 Castleview', '1234567890', 'dragon@hotmail.com'))
        accounts_results.insert(parent='', index='end', values=('465204787', 'Checking', 'Criss Cross', '105 California', '1234567890', 'kk@gmail.com'))
        accounts_results.insert(parent='', index='end', values=('235000485', 'Saving', 'Tony Stark', '106 Wisconsin', '1234657890', 'tony@yahoo.com'))
        accounts_results.insert(parent='', index='end', values=('109970001', 'Saving', 'Ninja Gaiden', '101 Weston', '1234567890', 'ryu@hotmail.com'))
        accounts_results.insert(parent='', index='end', values=('100043302', 'Invest', 'Texas Ranger', '102 Melrose', '1234567890', 'ranger@hotmail.com'))
        accounts_results.insert(parent='', index='end', values=('200654003', 'Checking', 'Blue Dragon', '104 Castleview', '1234567890', 'dragon@hotmail.com'))
        accounts_results.insert(parent='', index='end', values=('465204787', 'Checking', 'Criss Cross', '105 California', '1234567890', 'kk@gmail.com'))
        accounts_results.insert(parent='', index='end', values=('235000485', 'Saving', 'Tony Stark', '106 Wisconsin', '1234657890', 'tony@yahoo.com'))

        accounts_results_button = ttk.Button(area, text="View account", command=action_account)
        accounts_results_button.grid(column=5, row=4, padx=10)

    @classmethod
    def view_customer(cls):
        def action_update_customer():
            area.destroy()
            cls.update_customer()

        def action_delete_customer():
            area.destroy()
            cls.delete_customer()

        def action_open_account():
            area.destroy()
            cls.open_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

    @classmethod
    def view_account(cls):
        def action_deposit():
            area.destroy()
            cls.deposit()

        def action_withdrawal():
            area.destroy()
            cls.withdrawal()

        def action_transfer_own():
            area.destroy()
            cls.transfer_own()

        def action_transfer_others():
            area.destroy()
            cls.transfer_others()

        def action_change_type():
            area.destroy()
            cls.change_type()

        def action_delete_account():
            area.destroy()
            cls.delete_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

    @classmethod
    def update_customer(cls):
        def action_update():
            area.destroy()
            cls.view_customer()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

    @classmethod
    def delete_customer(cls):
        def action_delete():
            area.destroy()
            cls.search()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

    @classmethod
    def open_account(cls):
        def action_open():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

    @classmethod
    def deposit(cls):
        def action_deposit():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

    @classmethod
    def withdrawal(cls):
        def action_withdrawal():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

    @classmethod
    def transfer_own(cls):
        def action_transfer():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

    @classmethod
    def transfer_others(cls):
        def action_deposit():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

    @classmethod
    def delete_account(cls):
        def action_delete():
            area.destroy()
            cls.search()

        cls.window.geometry("1200x700")
        cls.create_top_menu()
