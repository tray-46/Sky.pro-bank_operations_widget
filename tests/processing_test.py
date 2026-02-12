from src import processing

bank_operation_list = [
    {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 1, "date": "2018-10-14T08:21:33.419441"},
    {"id": 2, "date": "2018-10-14T08:21:33.419441"},
    {"id": 3, "date": "2018-10-14T08:21:33.419441"},
]

print("\nBank operations list:")
print(*bank_operation_list, sep="\n")

# filter_by_state test
print("\nfilter_by_state tests")

targeted_state = "EXECUTED"
print(f"\nTargeted state:\t{targeted_state}")
print("Filtered operations list:")
print(*processing.filter_by_state(bank_operation_list), sep="\n")

targeted_state = "CANCELED"
print(f"\nTargeted state:\t{targeted_state}")
print("Filtered operations list:")
print(*processing.filter_by_state(bank_operation_list, targeted_state), sep="\n")


# sort_by_date test
print("\nsort_by_date tests")

print("\nDescending order:")
print(*processing.sort_by_date(bank_operation_list), sep="\n")

print("\nAscending order:")
print(*processing.sort_by_date(bank_operation_list, descending_sorting=False), sep="\n")
