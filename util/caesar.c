#include <stdio.h>
#include <stdlib.h>

#define SIZE 256
#define USAGE \
    "Caesar Cipher based encryption and decryption tool.\n"\
    "The result is printed to standard output.\n\n"\
    "%s <key> <file>\n"\
    "  <key>  - Key used to encrypt or decrypt.\n"\
    "  <file> - File to encrypt or decrypt.\n"

int main(int argc, char **argv)
{
    char c, e;
    FILE *f;

    if (argc == 3)
    {
        int k = atoi(argv[1]);

        f = fopen(argv[2], "r");

        if (f)
        {
            while (fread(&c, 1, 1, f))
            {
                e = (c + k) % SIZE;
                if (e < 0)
                    e = SIZE + e;
                printf("%c", e);
            }
        }
    }
    else
        printf(USAGE, argv[0]);

    return 0;
}
