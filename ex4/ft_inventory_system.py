import sys


def main() -> None:
		inventory: dict[str, int] = {}

		for i in range(1, len(args)):
			stuf: str = (args[i].split(":"))[0]
			inventory[stuf] = int((args[i].split(":"))[1])

		total_items = 0
		for quantity in inventory.values():
					total_items += quantity
		print(f"Total items in inventory: {total_items}")
		print(f"Unique item types: {len(inventory)}")
		print()
		print("=== Current Inventory ===")

		################# IL FAUT TRIER L'AFFICHAGE ###################
		for elmt in inventory:
			print(f"{elmt}: {inventory.get(elmt)} units ({float(inventory.get(elmt) * 100 / total_items):.1f}%)")

		print("=== Inventory Statistics ===")

if __name__ == "__main__":
	args = sys.argv

	if len(args) > 1:
		try:
			print("=== Inventory System Analysis ===")
			main()
		except ValueError as e:
			print(f"Error caught: {e}")
