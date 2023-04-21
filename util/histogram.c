#include <stdio.h>
#include <stdlib.h>

#define SIZE 256
#define USAGE \
    "Prints the amount of occurrencies of each byte on a given file.\n"\
    "The result is printed to standard output.\n\n"\
    "%s <min> <file>\n"\
    "  <min>  - Minimum amount of occurrencies.\n"\
    "  <file> - File to read.\n"

int main(int argc, char **argv)
{
    unsigned int i, h[SIZE];
    unsigned char c;
    FILE *f;
    int k;

    if (argc == 3)
    {
        k = atoi(argv[1]);

        for (i = 0; i < SIZE; i++)
            h[i] = 0;

        f = fopen(argv[2], "r");

        if (f)
        {
            while (fread(&c, 1, 1, f))
                h[c] += 1;
        }

        for (i = 0; i < SIZE; i++)
            if (h[i] >= k)
                printf("%.2x %d\n", i, h[i]);
    }
    else
        printf(USAGE, argv[0]);

    return 0;
}
