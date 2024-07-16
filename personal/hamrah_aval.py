input_data = {
    "1": {"months": 2, "size": 12, "price": 616400},
    "2": {"months": 4, "size": 15, "price": 830800},
    "3": {"months": 3, "size": 210, "price": 7700000},
    "4": {"months": 3, "size": 300, "price": 10500300},
    "5": {"months": 1, "size": 7, "price": 300000},
    "6": {"months": 0.44, "size": 6, "price": 261300},
}

most_profitable = None
min_profitability = float("inf")  # Initialize with positive infinity

for key, value in input_data.items():
    arzesh_afzode = value["price"] + value["price"] / 10  # Calculate arzesh_afzodeh
    profitability = arzesh_afzode / value["size"]
    print(f"Item {key}: profitability = {profitability:.2f}")
    if profitability < min_profitability:
        min_profitability = profitability
        most_profitable = key

print(
    f"Most profitable item: {most_profitable} with profitability = {min_profitability:.2f}"
)
