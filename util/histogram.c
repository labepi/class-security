#include <stdio.h>
#include <stdlib.h>

#define SIZE 256
#define USAGE \
    "Prints the amount of occurrencies of each byte on a given file.\n"\
    "The result is printed to standard output.\n\n"\
    "%s <file>\n"\
    "  <file> - File to read.\n"

int main(int argc, char **argv)
{
    unsigned int i, h[SIZE];
    unsigned char c;
    FILE *f;

    if (argc == 2)
    {
        for (i = 0; i < SIZE; i++)
            h[i] = 0;

        f = fopen(argv[1], "r");

        if (f)
        {
            while (fread(&c, 1, 1, f))
                h[c] += 1;
        }

        for (i = 0; i < SIZE; i++)
            if (h[i] > 0)
                printf("%u %d\n", i, h[i]);
    }
    else
        printf(USAGE, argv[0]);

    return 0;
}
