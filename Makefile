installTools:
	sh ./setup/setup.sh
runJupyter:
	juypter-lab
runAllAnswers:
	@for dir in $(shell find exercises -type d); do \
		if [ -f $$dir/App.py ]; then \
			echo "Running $$dir/App.py"; \
			python3 $$dir/App.py; \
		fi \
	done