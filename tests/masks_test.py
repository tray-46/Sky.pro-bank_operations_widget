from src import masks

# get_mask_card_number test
print("\nget_mask_card_number test:")
card_number = 7000792289606361

print(f"Card number:\t\t{card_number}")
print(f"Masked card number:\t{masks.get_mask_card_number(card_number)}")

# get_mask_account test
print("\nget_mask_account test")
account_number = 73654108430135874305

print(f"Account number:\t\t\t{account_number}")
print(f"Masked account number:\t{masks.get_mask_account(account_number)}")
