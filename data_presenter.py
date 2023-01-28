from matplotlib import pyplot as plt

# Open the CupcakeInvoices.csv.
open_file = open("CupcakeInvoices.csv")

# Loop through all the data and print each row.
for line in open_file:
    print(line)

# Return to start of file
open_file.seek(0)

# Loop through all the data and print the type of cupcakes purchased.
for line in open_file:
    line = line.strip()
    items = line.split(",")
    print(items[2])

# Return to start of file
open_file.seek(0)

# Loop through all the data and print out the total for each invoice
total = 0
for line in open_file:
    line = line.strip()
    items = line.split(",")
    line_total = float(items[3])*float(items[4])
    total += line_total
    print(round(line_total))

# Loop through all the data, and print out the total for all invoices combined.
print("Total for all invoices combined:", round(total))

# Return to start of file
open_file.seek(0)

# Display the total income of chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.
choc_total = 0
vanilla_total = 0
strawberry_total = 0
for line in open_file:
    line = line.strip()
    items = line.split(",")
    line_total = 0
    if items[2] == "Chocolate":
        line_total = float(items[3])*float(items[4])
        choc_total += line_total
    elif items[2] == "Vanilla":
        line_total = float(items[3])*float(items[4])
        vanilla_total += line_total
    elif items[2] == "Strawberry":
        line_total = float(items[3])*float(items[4])
        strawberry_total += line_total

open_file.close()

flavor_list = ["Chocolate", "Vanilla", "Strawberry"]
total_list = [choc_total, vanilla_total, strawberry_total]

plt.bar(flavor_list, total_list)
plt.show()
