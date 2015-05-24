all: ultest

clean:
	rm ultest

ultest: ultest.c
	$(CC) $(FLAGS) -o $@ $^ -lumberlog
