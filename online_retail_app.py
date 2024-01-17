import pandas as pd

class OnlineRetailData:
    def __init__(self, invoice_no, stock_code, description, quantity, invoice_date, unit_price, customer_id, country):
        self.invoice_no = invoice_no
        self.stock_code = stock_code
        self.description = description
        self.quantity = quantity
        self.invoice_date = invoice_date
        self.unit_price = unit_price
        self.customer_id = customer_id
        self.country = country

class DataManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            cls._instance.data = pd.DataFrame(columns=[
                'InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'
            ])
        return cls._instance

    def read_data(self, file_path):
        self._instance.data = pd.read_csv(file_path)

    def add_data(self, new_data):
        self._instance.data = pd.concat([self._instance.data, new_data], ignore_index=True)

    def edit_data(self, index, column, new_value):
        self._instance.data.at[index, column] = new_value

    def delete_data(self, index):
        self._instance.data.drop(index, inplace=True)

    def get_mean(self):
        return self._instance.data['Quantity'].mean()

    def get_median(self):
        return self._instance.data['Quantity'].median()

    def filter_data_by_country(self, country):
        return self._instance.data[self._instance.data['Country'] == country]

    def filter_data_by_quantity(self, min_quantity, max_quantity):
        return self._instance.data[(self._instance.data['Quantity'] >= min_quantity) & (self._instance.data['Quantity'] <= max_quantity)]
    
    def filter_data_by_country(self, country):
        filtered_data = self._instance.data[self._instance.data['Country'] == country]
        return filtered_data

    def filter_data_by_quantity_range(self, min_quantity, max_quantity):
        filtered_data = self._instance.data[
            (self._instance.data['Quantity'] >= min_quantity) & (self._instance.data['Quantity'] <= max_quantity)
        ]
        return filtered_data

class Application:
    def __init__(self):
        self.manager = DataManager()

    def display_menu(self):
        print("\nMenu:")
        print("1. Read Data from File")
        print("2. Add Data")
        print("3. Edit Data")
        print("4. Delete Data")
        print("5. Display Mean and Median")
        print("6. Filter Data by Country")
        print("7. Filter Data by Quantity Range")
        print("8. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                file_path = input("Enter the file path: ")
                self.manager.read_data(file_path)
            elif choice == '2':
                invoice_no = input("Enter Invoice No: ")
                stock_code = input("Enter Stock Code: ")
                description = input("Enter Description: ")
                quantity = int(input("Enter Quantity: "))
                invoice_date = input("Enter Invoice Date: ")
                unit_price = float(input("Enter Unit Price: "))
                customer_id = input("Enter Customer ID: ")
                country = input("Enter Country: ")

                new_data = pd.DataFrame([[invoice_no, stock_code, description, quantity, invoice_date, unit_price, customer_id, country]],
                                        columns=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'])
                self.manager.add_data(new_data)
            elif choice == '3':
                index = int(input("Enter the index to edit: "))
                column = input("Enter the column to edit: ")
                new_value = input("Enter the new value: ")
                self.manager.edit_data(index, column, new_value)
            elif choice == '4':
                index = int(input("Enter the index to delete: "))
                self.manager.delete_data(index)
                print(" index Deleted ! ")
            elif choice == '5':
                print(f"Mean: {self.manager.get_mean()}")
                print(f"Median: {self.manager.get_median()}")
            elif choice == '6':
                country = input("Enter the country to filter by: ")
                filtered_data = self.manager.filter_data_by_country(country)
                print("\nFiltered Data:")
                print(filtered_data)
            elif choice == '7':
                min_quantity = int(input("Enter the minimum quantity: "))
                max_quantity = int(input("Enter the maximum quantity: "))
                filtered_data = self.manager.filter_data_by_quantity_range(min_quantity, max_quantity)
                print("\nFiltered Data:")
                print(filtered_data)
            elif choice == '8':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = Application()
    app.run()
