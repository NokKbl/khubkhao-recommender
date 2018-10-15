# Let Python unittest module find and run tests itself
test:
	python3 -m unittest discover -p "*_test.py"

# Manual way.  
# This requires each *_test.py file to have a "main" that invokes unittest.
dumbtest: *_test.py
	for t in $?; do \
		echo Running $$t; \
		python3 $$t; \
	done;

clean:
	rm *.pyc
