/**
 * CSD 4523 Python II - CSAM Group 02 2022S
 * Term Project - Banking System
 * Hugo Beltran Escarraga - C0845680
 * Juan Luis Casanova Romero - C0851175
 */
 
-- ----------------------
-- Create Database -
-- ----------------------
 
-- Database Creation
CREATE DATABASE pybank;
USE pybank;

-- CREATE USER -- 
CREATE USER 'pybank'@'localhost' IDENTIFIED BY 'Lambton2022S';

-- ----------------------
-- Grant Privileges -
-- ----------------------

-- GRANT Global Privileges 
GRANT SHOW DATABASES, RELOAD
ON *.* 
TO 'pybank'@'localhost';

-- GRANT Database Privileges 
GRANT SELECT, INSERT, UPDATE, DELETE, 
  CREATE, INDEX, ALTER, EXECUTE, 
  CREATE VIEW, SHOW VIEW, CREATE ROUTINE, 
  ALTER ROUTINE, EVENT, TRIGGER, REFERENCES
ON pybank.* 
TO 'pybank'@'localhost';

FLUSH PRIVILEGES;
-- SHOW GRANTS FOR 'pybank'@'localhost';
	

-- ----------------------
-- Drop tables if exist -
-- ---------------------- 
DROP TABLE IF EXISTS movements;

DROP TABLE IF EXISTS accounts_hist;

DROP TABLE IF EXISTS accounts;

DROP TABLE IF EXISTS customers_hist;

DROP TABLE IF EXISTS customers;

DROP TABLE IF EXISTS agents;

DROP TABLE IF EXISTS transactions;

DROP TABLE IF EXISTS products;

DROP TABLE IF EXISTS positions;


-- Table Positions
CREATE TABLE positions (
    position_id INTEGER PRIMARY KEY,
    position_desc VARCHAR(25) NOT NULL,
    access_level INTEGER NOT NULL
);

 
-- Table Products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_type VARCHAR(25) NOT NULL,
    interest_rate DECIMAL(5 , 3 ) NOT NULL,
    amount_limit DECIMAL(8 , 2 ),
    quantity_limit INTEGER,
    minimum_balance DECIMAL(8 , 2 )
);


-- Table Transactions
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    transaction_desc VARCHAR(20) NOT NULL,
    fee DECIMAL(5 , 2 ) NOT NULL,
    access_level INTEGER
);


-- Table Agents 
CREATE TABLE agents (
    username VARCHAR(25) PRIMARY KEY,
    password VARCHAR(50) NOT NULL,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25),
    position_id INTEGER,
    CONSTRAINT agents_position_fk FOREIGN KEY (position_id)
        REFERENCES positions (position_id)
);

 
-- Table Customers 
CREATE TABLE customers (
    customer_id INTEGER NOT NULL AUTO_INCREMENT,
    pin VARCHAR(4) NOT NULL,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25),
    address VARCHAR(50),
    phone_number VARCHAR(15),
    email VARCHAR(30) NOT NULL UNIQUE,
    creation_date DATETIME NOT NULL,
    agent_id VARCHAR(25), 
	CONSTRAINT customers_pk PRIMARY KEY (customer_id),
    CONSTRAINT customers_agent_fk FOREIGN KEY (agent_id)
        REFERENCES agents (username)
);

CREATE INDEX customers_name_idx ON
  customers (first_name, last_name);
 
 
-- Table Customers History
CREATE TABLE customers_hist (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25),
    creation_date DATETIME NOT NULL,
    delete_date DATETIME NOT NULL,
    agent_id VARCHAR(25),
    CONSTRAINT customers_hist_agent_fk FOREIGN KEY (agent_id)
        REFERENCES agents (username)
);


-- Table Accounts
CREATE TABLE accounts (
    acc_number CHAR(9) PRIMARY KEY,
    acc_type INTEGER,
    balance DECIMAL(10 , 2 ) NOT NULL,
    transfer_amount DECIMAL(10 , 2 ) NOT NULL,
    transfer_quantity INTEGER NOT NULL,
    customer_id INTEGER,
    open_date DATETIME NOT NULL,
    agent_id VARCHAR(25),
    CONSTRAINT accounts_product_fk FOREIGN KEY (acc_type)
        REFERENCES products (product_id),
    CONSTRAINT accounts_customer_fk FOREIGN KEY (customer_id)
        REFERENCES customers (customer_id)
        ON DELETE CASCADE,
    CONSTRAINT accounts_agent_fk FOREIGN KEY (agent_id)
        REFERENCES agents (username)
);

CREATE INDEX accounts_customer_idx ON
  accounts (customer_id);


-- Table Accounts History
CREATE TABLE accounts_hist (
    acc_number CHAR(9) PRIMARY KEY,
    acc_type INTEGER,
    customer_id INTEGER,
    open_date DATETIME NOT NULL,
    close_date DATETIME NOT NULL,
    agent_id VARCHAR(25),
    CONSTRAINT accounts_hist_product_fk FOREIGN KEY (acc_type)
        REFERENCES products (product_id),
    CONSTRAINT accounts_hist_agent_fk FOREIGN KEY (agent_id)
        REFERENCES agents (username)
);

-- Table Movements 
CREATE TABLE movements (
    movement_id INTEGER NOT NULL AUTO_INCREMENT,
    source_account CHAR(9),
    destination_account CHAR(9),
    amount DECIMAL(10 , 2 ) NOT NULL,
    prev_balance DECIMAL(10 , 2 ) NOT NULL,
    new_balance DECIMAL(10 , 2 ) NOT NULL,
    movement_date DATETIME NOT NULL,
    transaction_id INTEGER,
    agent_id VARCHAR(25),
	CONSTRAINT movements_pk PRIMARY KEY (movement_id),
    CONSTRAINT movements_transaction_fk FOREIGN KEY (transaction_id)
        REFERENCES transactions (transaction_id),
    CONSTRAINT movements_agent_fk FOREIGN KEY (agent_id)
        REFERENCES agents (username)
);

CREATE INDEX movements_accounts_idx
  ON movements (source_account, destination_account);
CREATE INDEX movements_transaction_idx
  ON movements (transaction_id);

-- ----------------------
-- Table Inserts -
-- ----------------------

/*! SET TIME_ZONE='+00:00'; */
 

/* Insert for Positions Table */
INSERT INTO positions 
  (position_id, position_desc, access_level)
VALUES 
  (1, 'Manager', 1),
  (2, 'Supervisor', 2),
  (3, 'Agent', 3);


 /* Insert for Products Table */
INSERT INTO products 
  (product_id, product_type, interest_rate, amount_limit, quantity_limit, minimum_balance)
VALUES 
  (1, 'Checking', 0.009, 10000, 20,-5000),
  (2, 'Saving', 0.012, 6000, 10, 100),
  (3, 'Investing', 0.05, 0, 0, 1000);


/* Insert for Transactions Table */
INSERT INTO transactions 
  (transaction_id, transaction_desc, fee, access_level)
VALUES 
  (1, 'Create customer', 0, 3),
  (2, 'Update customer', 0, 2),
  (3, 'Delete customer', 0, 1),
  (4, 'Opening account', 0, 3),
  (5, 'Change account type', 4, 3),
  (6, 'Close account', 0, 1),
  (7, 'Deposit', 0, 3),
  (8, 'Withdrawal', 2.50, 2),
  (9, 'Funds transfer', 3.50, 2),
  (10, 'Fee', 0, 3);


 /* Insert for Agents Table */
INSERT INTO agents 
  (username, password, first_name, last_name, position_id)
VALUES 
  ('sagara', 'ua8w6WpM','Sagara', 'Samarawickrama', 1),
  ('hbe','70gatJ04', 'Hugo', 'Beltran', 2),
  ('juanl', 'Kd2xvlc', 'Juan', 'Casanova', 3);
 
 -- END --
 