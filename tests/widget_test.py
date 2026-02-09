from src import widget

# mask_account_card test
print("\nmask_account_card test:")
number_to_mask = "Visa Platinum 7000792289606361"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

number_to_mask = "Maestro 7000792289606361"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

number_to_mask = "Счет 73654108430135874305"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

number_to_mask = "Maestro 1596837868705199"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

number_to_mask = "Счет 64686473678894779589"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

number_to_mask = "MasterCard 7158300734726758"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

number_to_mask = "Счет 35383033474447895560"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

number_to_mask = "Visa Classic 6831982476737658"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

number_to_mask = "Visa Platinum 8990922113665229"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

number_to_mask = "Visa Gold 5999414228426353"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

number_to_mask = "Счет 73654108430135874305"
print(f"\nAccount|Card number:\t{number_to_mask}")
print(f"Masked number:\t\t\t{widget.mask_account_card(number_to_mask)}")

# get_date test
print("\nget_date test:")
datetime_string = "2024-03-11T02:26:16.671407"
print(f"\ndatetime string is:\t{datetime_string}")
print(f"Formated date is:\t{widget.get_date(datetime_string)}")
