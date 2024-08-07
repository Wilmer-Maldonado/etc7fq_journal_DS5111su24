default:
	@cat makefile

setup:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip; pip install -r requirements.txt;
	. env/bin/activate
	@echo "To activate the virtual environment, run: source env/bin/activate"

get_texts:
	wget https://gutenberg.org/cache/epub/932/pg932.txt
	wget https://gutenberg.org/cache/epub/17192/pg17192.txt
	wget https://gutenberg.org/cache/epub/1064/pg1064.txt
	wget https://gutenberg.org/cache/epub/1063/pg1063.txt
	wget https://gutenberg.org/cache/epub/51060/pg51060.txt
	wget https://gutenberg.org/cache/epub/32037/pg32037.txt
	wget https://gutenberg.org/cache/epub/67094/pg67094.txt
	wget https://gutenberg.org/cache/epub/50852/pg50852.txt
	wget https://gutenberg.org/cache/epub/65171/pg65171.txt
	wget https://gutenberg.org/cache/epub/14082/pg14082.txt
	wget https://gutenberg.org/cache/epub/10031/pg10031.txt

raven_line_count: pg17192.txt
	wc -l pg17192.txt

raven_word_count: pg17192.txt
	wc -w pg17192.txt

raven_counts: pg17192.txt
	echo "lowercase raven:"
	cat pg17192.txt | grep -o 'raven' | wc -l
	echo "title case raven:"
	cat pg17192.txt | grep -o 'Raven' | wc -l
	echo "ignore case raven:"
	cat pg17192.txt | grep -i 'raven' | wc -l

total_lines:
	wc -l pg*.txt

total_words:
	wc -w pg*.txt

tokenizer:
	python tokenizer.py

.PHONY: lint
lint:
	. env/bin/activate && pylint src/pkg_etc7fq/tokenizer.py

.PHONY: tests
tests: lint
	. env/bin/activate && pytest -m "not integration" tests/

.PHONY: integration_tests
integration_tests:
	. env/bin/activate && pytest -m "integration" tests/

pkg_import_test:
	. env/bin/activate && python -c "import pkg_etc7fq as pkg; print(pkg.tokenize('To be or not to be'))"
