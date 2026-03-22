def generate_report(sales_data, filename):
    total = 0
    for price in sales_data.values():
        total += price
    avarage = total / len(sales_data)
    with open(filename, "w") as f:
        f.write("WEEKLY SALES REPORT\n")
        f.write("-------------------\n")
        for day, price in sales_data.items():
            f.write(f"{day}: {price}\n")
        f.write("-------------------\n")
        f.write(f"Total: {total}\n")
        f.write(f"Avarage: {avarage:.2f}\n")

sales_data = {"Mon": 100.50, "Tue": 200.00, "Wed": 150.75}
filename = "report.txt"
generate_report(sales_data, filename)