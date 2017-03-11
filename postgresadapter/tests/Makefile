CC = gcc
CFLAGS = -g -Werror -Wall -Wdeclaration-after-statement
TEXT_INCLUDE_DIRS = -I ../lib

field_info.o: ../lib/field_info.c
	$(CC) $(CFLAGS) -c ../lib/field_info.c $(TEXT_INCLUDE_DIRS)

clean:
	-rm -f *.o

