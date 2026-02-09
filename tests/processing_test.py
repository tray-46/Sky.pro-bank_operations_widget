from src import processing

# filter_by_state test
bank_operation_list = [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

targeted_state = "EXECUTED"

print("\nBank operations list:")
print(*bank_operation_list, sep='\n')
print(f"\nTargeted state:\t{targeted_state}")
print("Filtered operations list:")
print(*processing.filter_by_state(bank_operation_list), sep='\n')

targeted_state = "CANCELED"
print(f"\nTargeted state:\t{targeted_state}")
print("Filtered operations list:")
print(*processing.filter_by_state(bank_operation_list, targeted_state), sep='\n')
