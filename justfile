set dotenv-load

[private]
default:
	@just --list


website:
	$BROWSER "https://adventofcode.com/2024/"

get-input day:
	curl - "session=$SESSION_COOKIE" https://adventofcode.com/2024/day/{{ day }}/input -o day{{ day }}/input.txt

run day:
	python day{{ day }}/__main__.py

new day:
	cp day00 day{{ day }} -r

edit day:
	$EDITOR "day{{ day }}"/__main__.py

list:
	fd --max-depth 1 day --exclude day00
