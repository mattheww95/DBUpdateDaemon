CC=gcc


./bin/testd: ./src/dbdaemon.c
	$(CC) $^ -o $@