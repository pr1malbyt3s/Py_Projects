# AOC 2021 Day 3
import sys

# This function is used to read a file input from the command line. It returns the file contents as a list of lines.
def read_file():
	if len(sys.argv) != 2:
		print("Specify puzzle input file")
		sys.exit(-1)
	else:
		# Open file at command line position 1:	
		with open(sys.argv[1], 'r') as f:
			input_list = [line.strip() for line in f]
			numbers = [int(num) for num in input_list[0].split(',')]
			cards_input = input_list[1:]
	return cards_input, numbers

def read_cards(cards_input:list) -> list:
	cards = []
	for line in cards_input:
		if(line == ''):
			card = []
			cards.append(card)
			continue
		card.append([int(num) for num in line.split()])
	return cards

def card_check(cards:list, drawn:list) -> list:
	winning_cards = []
	for card in cards:
		for row in card:
			if(all(nums in drawn for nums in row)):
				winning_cards.append(card)
		for i in range(0,len(card)):
			col_list = list(list(zip(*card))[i])
			if(all(nums in drawn for nums in col_list)):
				winning_cards.append(card)
	return winning_cards

# Part 1
def find_winner(cards:list, numbers:list):
	drawn = []
	for number in numbers:
		drawn.append(number)
		winning_cards = card_check(cards, drawn)
		if(winning_cards):
			break
	return drawn, winning_cards[0], drawn[-1]

# Part 2
def find_last_winner(cards:list, numbers:list):
	drawn = []
	for number in numbers:
		drawn.append(number)
		winning_cards = card_check(cards, drawn)
		cards = [card for card in cards if card not in winning_cards]
		if(not cards):
			break
	return drawn, winning_cards[-1], drawn[-1]

def final_score(drawn:list, card:list, last_drawn:int) -> int:
	card_numbers = [number for row in card for number in row]
	drawn = drawn[:(drawn.index(last_drawn) + 1)]
	remaining = set()
	for number in card_numbers:
		if number not in drawn:
			remaining.add(number)
	card_sum = sum(remaining)
	return card_sum * drawn[-1]

def main():
	cards_input, numbers = read_file()
	cards = read_cards(cards_input)
	# Part 1
	drawn1, winner1, last_drawn1 = find_winner(cards, numbers)
	print(final_score(drawn1, winner1, last_drawn1))
	# Part 2
	drawn2, last_winner2, last_drawn2 = find_last_winner(cards, numbers)
	print(final_score(drawn2, last_winner2, last_drawn2))

if __name__ == "__main__":
	main()
