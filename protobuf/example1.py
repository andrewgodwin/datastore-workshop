from addresses_pb2 import AddressBook, Entry, Address

# Make an address book
book = AddressBook()
book.title = "Example Addresses"

entry1 = book.entries.add()
entry1.name = "Andrew Godwin"
entry1.age = 27
entry1.address.line1 = "1 Django St."
entry1.address.city = "Pythonia"
entry1.address.country = "SG"

entry2 = book.entries.add()
entry2.name = "Elisabeth Windsor"
entry2.age = 89
entry2.address.line1 = "Buckingham Palace"
entry2.address.city = "London"
entry2.address.country = "GB"
entry2.address.postcode = "SW1A 1AA"

with open("example.pb", "w") as fh:
    fh.write(book.SerializeToString())

# Load it and show addresses
with open("example.pb", "r") as fh:
    book = AddressBook()
    book.ParseFromString(fh.read())

for entry in book.entries:
    print entry
