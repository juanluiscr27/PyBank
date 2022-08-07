from mysql.connector import errors

from db.database_conn import ConnectionPool
from model.result import Return


class AccountModel:

	@classmethod
	def view_acc_numbers(cls, account_numbers: list, result: Return):
		conn = None
		# Request a database connection from the pool
		try:
			conn = ConnectionPool.get_connection()

			if conn.is_connected():
				# print("Connection successful")
				query = "SELECT ac.acc_number FROM accounts ac " \
						"  LEFT OUTER JOIN accounts_hist ah " \
						"  ON ac.acc_number  = ah.acc_number " \
						"UNION " \
						" SELECT ah.acc_number FROM accounts ac " \
						" RIGHT OUTER JOIN accounts_hist ah " \
						" ON ac.acc_number = ah.acc_number"
				cursor = conn.cursor()

				cursor.execute(query)
				resul_set = cursor.fetchall()

				if cursor.rowcount > 0:
					# Unpack row fields from the result
					for acc_number in resul_set:
						account_numbers.append(acc_number)

					result.set_code("00")
				else:
					result.set_code("01")

				cursor.close()

		except errors.PoolError as pe:
			print(f"{pe.errno} Pool is exhausted due to many connection requests")
		except errors.Error as err:
			print(f'{err.errno}: {err.msg}')
		finally:
			if conn.is_connected():
				conn.close()
