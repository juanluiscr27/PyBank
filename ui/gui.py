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

        username_text.insert(0, 'hbe')
        password_text.insert(0, '12345')

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
    def search(cls):
        def exec_search():
            i=1

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

        search_button = ttk.Button(area, text="Search", command=exec_search)
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
    def new_customer(cls):
        def action_create_customer():
            area.destroy()
            cls.view_customer()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="New customer")
        area.grid(column=0, row=1, padx=50, pady=20)

        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=0, row=0, padx=20)

        customer_first_name = tk.StringVar()
        customer_first_name_text = ttk.Entry(area, width=50, textvariable=customer_first_name)
        customer_first_name_text.grid(column=1, row=0, padx=20, sticky="W")

        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=0, row=1, padx=20)

        customer_last_name = tk.StringVar()
        customer_last_name_text = ttk.Entry(area, width=50, textvariable=customer_last_name)
        customer_last_name_text.grid(column=1, row=1, padx=20, sticky="W")

        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=0, row=2, padx=20)

        customer_address = tk.StringVar()
        customer_address_text = ttk.Entry(area, width=50, textvariable=customer_address)
        customer_address_text.grid(column=1, row=2, padx=20, sticky="W")

        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=0, row=3, padx=20)

        customer_phone = tk.StringVar()
        customer_phone_text = ttk.Entry(area, width=20, textvariable=customer_phone)
        customer_phone_text.grid(column=1, row=3, padx=20, sticky="W")

        customer_email_label = ttk.Label(area, text="Email")
        customer_email_label.grid(column=0, row=4, padx=20)

        customer_email = tk.StringVar()
        customer_email_text = ttk.Entry(area, width=30, textvariable=customer_email)
        customer_email_text.grid(column=1, row=4, padx=20, sticky="W")

        customer_pin_label = ttk.Label(area, text="PIN")
        customer_pin_label.grid(column=0, row=5, padx=20)

        customer_pin = tk.StringVar()
        customer_pin_text = ttk.Entry(area, width=10, show='*', textvariable=customer_pin)
        customer_pin_text.grid(column=1, row=5, padx=20, sticky="W")

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=5, row=6, padx=20)

        create_customer_button = ttk.Button(area, text="Create customer", command=action_create_customer)
        create_customer_button.grid(column=0, row=7, columnspan=6, padx=10)
        create_customer_button.config(width=50)

    @classmethod
    def update_customer(cls):
        def action_update_customer():
            area.destroy()
            cls.view_customer()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Update customer")
        area.grid(column=0, row=1, padx=50, pady=20)

        customer_first_name_label = ttk.Label(area, text="First name")
        customer_first_name_label.grid(column=0, row=0, padx=20)

        customer_first_name = tk.StringVar()
        customer_first_name_text = ttk.Entry(area, width=50, textvariable=customer_first_name)
        customer_first_name_text.grid(column=1, row=0, padx=20, sticky="W")

        customer_last_name_label = ttk.Label(area, text="Last name")
        customer_last_name_label.grid(column=0, row=1, padx=20)

        customer_last_name = tk.StringVar()
        customer_last_name_text = ttk.Entry(area, width=50, textvariable=customer_last_name)
        customer_last_name_text.grid(column=1, row=1, padx=20, sticky="W")

        customer_address_label = ttk.Label(area, text="Address")
        customer_address_label.grid(column=0, row=2, padx=20)

        customer_address = tk.StringVar()
        customer_address_text = ttk.Entry(area, width=50, textvariable=customer_address)
        customer_address_text.grid(column=1, row=2, padx=20, sticky="W")

        customer_phone_label = ttk.Label(area, text="Phone")
        customer_phone_label.grid(column=0, row=3, padx=20)

        customer_phone = tk.StringVar()
        customer_phone_text = ttk.Entry(area, width=20, textvariable=customer_phone)
        customer_phone_text.grid(column=1, row=3, padx=20, sticky="W")

        customer_pin_label = ttk.Label(area, text="PIN")
        customer_pin_label.grid(column=0, row=5, padx=20)

        customer_pin = tk.StringVar()
        customer_pin_text = ttk.Entry(area, width=10, show='*', textvariable=customer_pin)
        customer_pin_text.grid(column=1, row=5, padx=20, sticky="W")

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=5, row=6, padx=20)

        update_customer_button = ttk.Button(area, text="Update customer", command=action_update_customer)
        update_customer_button.grid(column=0, row=7, columnspan=6, padx=10)
        update_customer_button.config(width=50)

    @classmethod
    def delete_customer(cls):
        def action_delete_customer():
            area.destroy()
            cls.search()

        def action_account():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Delete Customer")
        area.grid(column=0, row=1, padx=50, pady=20)

        id_label = ttk.Label(area, text="ID")
        id_label.grid(column=0, row=0, padx=20)

        customer_id_label = ttk.Label(area, text="1")
        customer_id_label.grid(column=0, row=1, padx=20)

        customer_name_label = ttk.Label(area, text="Ninja Gaiden")
        customer_name_label.grid(column=1, row=0, padx=20)

        customer_address_label = ttk.Label(area, text="101 Weston")
        customer_address_label.grid(column=2, row=0, padx=20)

        customer_phone_label = ttk.Label(area, text="1234567890")
        customer_phone_label.grid(column=3, row=0, padx=20)

        customer_email_label = ttk.Label(area, text="ryu@hotmail.com")
        customer_email_label.grid(column=4, row=0, padx=20)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=5, row=0, padx=20)

        delete_customer_button = ttk.Button(area, text="Delete customer", command=action_delete_customer)
        delete_customer_button.grid(column=6, row=0, padx=10)
        delete_customer_button.config(width=50)

    @classmethod
    def view_customer(cls):
        def action_account():
            area.destroy()
            cls.view_account()
        def action_open_account():
            area.destroy()
            cls.open_account()

        def action_update_customer():
            area.destroy()
            cls.update_customer()

        def action_delete_customer():
            area.destroy()
            cls.delete_customer()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Customer details")
        area.grid(column=0, row=1, padx=50, pady=20)

        id_label = ttk.Label(area, text="ID")
        id_label.grid(column=0, row=0, padx=20)

        customer_id_label = ttk.Label(area, text="1")
        customer_id_label.grid(column=0, row=1, padx=20)

        customer_name_label = ttk.Label(area, text="Ninja Gaiden")
        customer_name_label.grid(column=1, row=0, padx=20)

        customer_address_label = ttk.Label(area, text="101 Weston")
        customer_address_label.grid(column=2, row=0, padx=20)

        customer_phone_label = ttk.Label(area, text="1234567890")
        customer_phone_label.grid(column=3, row=0, padx=20)

        customer_email_label = ttk.Label(area, text="ryu@hotmail.com")
        customer_email_label.grid(column=4, row=0, padx=20)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=5, row=0, padx=20)

        open_account_button = ttk.Button(area, text="Open account", command=action_open_account)
        open_account_button.grid(column=6, row=0, padx=10)
        open_account_button.config(width=50)

        update_customer_button = ttk.Button(area, text="Update customer", command=action_update_customer)
        update_customer_button.grid(column=6, row=1, padx=10)
        update_customer_button.config(width=50)

        delete_customer_button = ttk.Button(area, text="Delete customer", command=action_delete_customer)
        delete_customer_button.grid(column=6, row=2, padx=10)
        delete_customer_button.config(width=50)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=0, row=3, padx=20)

        accounts_label = ttk.Label(area, text="Customer Accounts")
        accounts_label.grid(column=0, row=4, padx=20, sticky="SW")

        customer_accounts = ttk.Treeview(area)
        customer_accounts.grid(column=0, row=5, padx=50, columnspan=5)
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
        customer_accounts.insert(parent='', index='end', values=('109970001', 'Checking', '$5000', '$200', '4'))
        customer_accounts.insert(parent='', index='end', values=('409970001', 'Saving', '$200', '$15', '1'))
        customer_accounts.insert(parent='', index='end', values=('809970001', 'Investing', '$15000', '$0', '0'))

        view_account_button = ttk.Button(area, text="View account", command=action_account)
        view_account_button.grid(column=5, row=5, padx=10)

    @classmethod
    def open_account(cls):
        def action_open_account():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Open account")
        area.grid(column=0, row=1, padx=50, pady=20)

        id_label = ttk.Label(area, text="Customer ID")
        id_label.grid(column=0, row=0, padx=20)

        customer_id_label = ttk.Label(area, text="1")
        customer_id_label.grid(column=0, row=1, padx=20)

        name_label = ttk.Label(area, text="Name")
        name_label.grid(column=1, row=0, padx=20)

        customer_name_label = ttk.Label(area, text="Ninja Gaiden")
        customer_name_label.grid(column=1, row=1, padx=20)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=0, row=2, padx=20)

        account_type_frame = ttk.LabelFrame(area, text="Account type")
        account_type_frame.grid(column=0, row=3, padx=20, rowspan=4)

        account_type_values = ["Checking", "Saving", "Investing"]
        account_type = tk.IntVar()

        for i in range(3):
            account_type_radio = tk.Radiobutton(account_type_frame, text=account_type_values[i], variable=account_type, value=i)
            account_type_radio.grid(column=0, row=i, padx=20)

        interest_label = ttk.Label(area, text="Interest rate")
        interest_label.grid(column=1, row=3, padx=20)

        interest_rate_label = ttk.Label(area, text="5%")
        interest_rate_label.grid(column=2, row=3, padx=20)

        amount_label = ttk.Label(area, text="Amount limit")
        amount_label.grid(column=1, row=4, padx=20)

        amount_limit_label = ttk.Label(area, text="$1000")
        amount_limit_label.grid(column=2, row=4, padx=20)

        quantity_label = ttk.Label(area, text="Quantity limit")
        quantity_label.grid(column=1, row=5, padx=20)

        quantity_limit_label = ttk.Label(area, text="10")
        quantity_limit_label.grid(column=2, row=5, padx=20)

        balance_label = ttk.Label(area, text="Minimum balance")
        balance_label.grid(column=1, row=6, padx=20)

        minimum_balance_label = ttk.Label(area, text="$5000")
        minimum_balance_label.grid(column=2, row=6, padx=20)

        open_account_button = ttk.Button(area, text="Open account", command=action_open_account)
        open_account_button.grid(column=1, row=7, padx=20, pady=30)

    @classmethod
    def delete_account(cls):
        def action_delete_account():
            area.destroy()
            cls.search()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Delete account")
        area.grid(column=0, row=1, padx=50, pady=20)

        id_label = ttk.Label(area, text="Customer ID")
        id_label.grid(column=0, row=0, padx=20)

        customer_id_label = ttk.Label(area, text="1")
        customer_id_label.grid(column=0, row=1, padx=20)

        name_label = ttk.Label(area, text="Name")
        name_label.grid(column=1, row=0, padx=20)

        customer_name_label = ttk.Label(area, text="Ninja Gaiden")
        customer_name_label.grid(column=1, row=1, padx=20)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=0, row=2, padx=20)

        number_label = ttk.Label(area, text="Account number")
        number_label.grid(column=0, row=3, padx=20)

        account_number_label = ttk.Label(area, text="109970001")
        account_number_label.grid(column=0, row=4, padx=20)

        type_label = ttk.Label(area, text="Type")
        type_label.grid(column=1, row=3, padx=20)

        account_type_label = ttk.Label(area, text="Checking")
        account_type_label.grid(column=1, row=4, padx=20)

        balance_label = ttk.Label(area, text="Balance")
        balance_label.grid(column=2, row=3, padx=20)

        account_balance_label = ttk.Label(area, text="$1000")
        account_balance_label.grid(column=2, row=4, padx=20)

        transferred_label = ttk.Label(area, text="Transferred")
        transferred_label.grid(column=3, row=3, padx=20)

        account_transferred_label = ttk.Label(area, text="$300")
        account_transferred_label.grid(column=3, row=4, padx=20)

        transfers_label = ttk.Label(area, text="Transfers")
        transfers_label.grid(column=4, row=3, padx=20)

        account_transfers_label = ttk.Label(area, text="2")
        account_transfers_label.grid(column=4, row=4, padx=20)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=5, row=0, padx=20)

        delete_account_button = ttk.Button(area, text="Delete account", command=action_delete_account)
        delete_account_button.grid(column=6, row=0, padx=10)
        delete_account_button.config(width=50)

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

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Account details")
        area.grid(column=0, row=1, padx=50, pady=20)

        id_label = ttk.Label(area, text="Customer ID")
        id_label.grid(column=0, row=0, padx=20)

        customer_id_label = ttk.Label(area, text="1")
        customer_id_label.grid(column=0, row=1, padx=20)

        name_label = ttk.Label(area, text="Name")
        name_label.grid(column=1, row=0, padx=20)

        customer_name_label = ttk.Label(area, text="Ninja Gaiden")
        customer_name_label.grid(column=1, row=1, padx=20)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=0, row=2, padx=20)

        number_label = ttk.Label(area, text="Account number")
        number_label.grid(column=0, row=3, padx=20)

        account_number_label = ttk.Label(area, text="109970001")
        account_number_label.grid(column=0, row=4, padx=20)

        type_label = ttk.Label(area, text="Type")
        type_label.grid(column=1, row=3, padx=20)

        account_type_label = ttk.Label(area, text="Checking")
        account_type_label.grid(column=1, row=4, padx=20)

        balance_label = ttk.Label(area, text="Balance")
        balance_label.grid(column=2, row=3, padx=20)

        account_balance_label = ttk.Label(area, text="$1000")
        account_balance_label.grid(column=2, row=4, padx=20)

        transferred_label = ttk.Label(area, text="Transferred")
        transferred_label.grid(column=3, row=3, padx=20)

        account_transferred_label = ttk.Label(area, text="$300")
        account_transferred_label.grid(column=3, row=4, padx=20)

        transfers_label = ttk.Label(area, text="Transfers")
        transfers_label.grid(column=4, row=3, padx=20)

        account_transfers_label = ttk.Label(area, text="2")
        account_transfers_label.grid(column=4, row=4, padx=20)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=5, row=0, padx=20)

        deposit_button = ttk.Button(area, text="Deposit", command=action_deposit)
        deposit_button.grid(column=6, row=0, padx=10)
        deposit_button.config(width=50)

        withdrawal_button = ttk.Button(area, text="Withdrawal", command=action_withdrawal)
        withdrawal_button.grid(column=6, row=1, padx=10)
        withdrawal_button.config(width=50)

        transfer_own_button = ttk.Button(area, text="Transfer own", command=action_transfer_own)
        transfer_own_button.grid(column=6, row=2, padx=10)
        transfer_own_button.config(width=50)

        transfer_others_button = ttk.Button(area, text="Transfer others", command=action_transfer_others)
        transfer_others_button.grid(column=6, row=3, padx=10)
        transfer_others_button.config(width=50)

        change_type_button = ttk.Button(area, text="Change type", command=action_change_type)
        change_type_button.grid(column=6, row=4, padx=10)
        change_type_button.config(width=50)

        delete_account_button = ttk.Button(area, text="Delete account", command=action_delete_account)
        delete_account_button.grid(column=6, row=5, padx=10)
        delete_account_button.config(width=50)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=0, row=6, padx=20)

        movements_label = ttk.Label(area, text="Account movements")
        movements_label.grid(column=0, row=7, padx=20, sticky="SW")

        account_movements = ttk.Treeview(area)
        account_movements.grid(column=0, row=8, padx=50, columnspan=5)
        account_movements['columns'] = ('date', 'transaction', 'amount')
        account_movements.column("#0", width=0, stretch=False)
        account_movements.column("date", anchor="center", width=100)
        account_movements.column("transaction", anchor="center", width=100)
        account_movements.column("amount", anchor="center", width=100)
        account_movements.heading("#0", text="", anchor="center")
        account_movements.heading("date", text="NUMBER", anchor="center")
        account_movements.heading("transaction", text="TYPE", anchor="center")
        account_movements.heading("amount", text="BALANCE", anchor="center")
        account_movements.insert(parent='', index='end', values=('01-JAN-2022', 'Deposit', '$15'))
        account_movements.insert(parent='', index='end', values=('04-JUL-2022', 'Transfer own', '$200'))
        account_movements.insert(parent='', index='end', values=('02-AUG-2022', 'Withdrawal', '$150'))

    @classmethod
    def deposit(cls):
        def action_deposit():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Deposit")
        area.grid(column=0, row=1, padx=50, pady=20)

        id_label = ttk.Label(area, text="Customer ID")
        id_label.grid(column=0, row=0, padx=20)

        customer_id_label = ttk.Label(area, text="1")
        customer_id_label.grid(column=0, row=1, padx=20)

        customer_name_label = ttk.Label(area, text="Ninja Gaiden")
        customer_name_label.grid(column=1, row=0, padx=20)

        account_number_label = ttk.Label(area, text="109970001")
        account_number_label.grid(column=2, row=0, padx=20)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=0, row=2, padx=20)

        amount_label = ttk.Label(area, text="Amount")
        amount_label.grid(column=0, row=3, padx=20)

        deposit = tk.DoubleVar()
        deposit_text = ttk.Entry(area, width=20, textvariable=deposit)
        deposit_text.grid(column=1, row=3, padx=20, sticky="W")

        deposit_button = ttk.Button(area, text="Deposit", command=action_deposit)
        deposit_button.grid(column=2, row=3, padx=10)
        deposit_button.config(width=50)

    @classmethod
    def withdrawal(cls):
        def action_withdrawal():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Withdrawal")
        area.grid(column=0, row=1, padx=50, pady=20)

        id_label = ttk.Label(area, text="Customer ID")
        id_label.grid(column=0, row=0, padx=20)

        customer_id_label = ttk.Label(area, text="1")
        customer_id_label.grid(column=0, row=1, padx=20)

        customer_name_label = ttk.Label(area, text="Ninja Gaiden")
        customer_name_label.grid(column=1, row=0, padx=20)

        account_number_label = ttk.Label(area, text="109970001")
        account_number_label.grid(column=2, row=0, padx=20)

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=0, row=2, padx=20)

        amount_label = ttk.Label(area, text="Amount")
        amount_label.grid(column=0, row=3, padx=20)

        withdrawal = tk.DoubleVar()
        withdrawal_text = ttk.Entry(area, width=20, textvariable=withdrawal)
        withdrawal_text.grid(column=1, row=3, padx=20, sticky="W")

        withdrawal_button = ttk.Button(area, text="Withdrawal", command=action_withdrawal)
        withdrawal_button.grid(column=2, row=3, padx=10)
        withdrawal_button.config(width=50)

    @classmethod
    def transfer_own(cls):
        def action_transfer():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Transfer to own")
        area.grid(column=0, row=1, padx=50, pady=20)

        id_label = ttk.Label(area, text="Customer ID")
        id_label.grid(column=0, row=0, padx=20)

        customer_id_label = ttk.Label(area, text="1")
        customer_id_label.grid(column=0, row=1, padx=20)

        customer_name_label = ttk.Label(area, text="Ninja Gaiden")
        customer_name_label.grid(column=1, row=0, padx=20)

        account_number_label = ttk.Label(area, text="109970001")
        account_number_label.grid(column=2, row=0, padx=20)

        account_number_label = ttk.Label(area, text="Destination account")
        account_number_label.grid(column=0, row=2, padx=20)

        destination_account = tk.StringVar()
        destination_account_text = ttk.Entry(area, width=20, textvariable=destination_account)
        destination_account_text.grid(column=0, row=3, padx=20, sticky="W")

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=0, row=4, padx=20)

        amount_label = ttk.Label(area, text="Amount")
        amount_label.grid(column=0, row=5, padx=20)

        transfer = tk.DoubleVar()
        transfer_text = ttk.Entry(area, width=20, textvariable=transfer)
        transfer_text.grid(column=1, row=5, padx=20, sticky="W")

        transfer_button = ttk.Button(area, text="Transfer own", command=action_transfer)
        transfer_button.grid(column=2, row=5, padx=10)
        transfer_button.config(width=50)

    @classmethod
    def transfer_others(cls):
        def action_transfer():
            area.destroy()
            cls.view_account()

        cls.window.geometry("1200x700")
        cls.create_top_menu()

        agent_name_label = ttk.Label(cls.window, text=cls.active_agent.first_name + " " + cls.active_agent.last_name)
        agent_name_label.grid(column=0, row=0, padx=50, sticky="E")

        area = ttk.LabelFrame(cls.window, text="Transfer to others")
        area.grid(column=0, row=1, padx=50, pady=20)

        id_label = ttk.Label(area, text="Customer ID")
        id_label.grid(column=0, row=0, padx=20)

        customer_id_label = ttk.Label(area, text="1")
        customer_id_label.grid(column=0, row=1, padx=20)

        customer_name_label = ttk.Label(area, text="Ninja Gaiden")
        customer_name_label.grid(column=1, row=0, padx=20)

        account_number_label = ttk.Label(area, text="109970001")
        account_number_label.grid(column=2, row=0, padx=20)

        account_number_label = ttk.Label(area, text="Destination account")
        account_number_label.grid(column=0, row=2, padx=20)

        destination_account = tk.StringVar()
        destination_account_text = ttk.Entry(area, width=20, textvariable=destination_account)
        destination_account_text.grid(column=0, row=3, padx=20, sticky="W")

        space_label = ttk.Label(area, text=" ")
        space_label.grid(column=0, row=4, padx=20)

        amount_label = ttk.Label(area, text="Amount")
        amount_label.grid(column=0, row=5, padx=20)

        transfer = tk.DoubleVar()
        transfer_text = ttk.Entry(area, width=20, textvariable=transfer)
        transfer_text.grid(column=1, row=5, padx=20, sticky="W")

        transfer_button = ttk.Button(area, text="Transfer others", command=action_transfer)
        transfer_button.grid(column=2, row=5, padx=10)
        transfer_button.config(width=50)
