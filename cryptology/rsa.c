#include <stdio.h>
#include <stdlib.h>

#define USAGE \
    "RSA Cipher based encryption and decryption tool.\n"\
    "Encrypts each byte on the input using two bytes as output.\n"\
    "Decrypts each two byte on the input using one byte as output.\n"\
    "The possile module values are limited to the interval [259, 65531].\n"\
    "The result is printed to standard output.\n\n"\
    "%s [e|d] <key> <file>\n"\
    "  [e|d]  - Encryption or Decryption.\n"\
    "  <key>  - Key to be used to encrypt or decrypt.\n"\
    "  <mod>  - Value for the modulo right operand.\n"\
    "  <file> - File to encrypt or decrypt.\n"

unsigned int mod_exp(unsigned int c, unsigned int k, unsigned int m)
{
    unsigned int i = 1;
    unsigned int r = 1;

    while (i++ <= k)
        r = (r * c) % m;

    return r;
}

int main(int argc, char **argv)
{
    unsigned int k, m;
    unsigned char b, byte;
    unsigned int twobyte;
    FILE *f;

    if (argc != 5)
    {
        printf(USAGE, argv[0]);

        return 0;
    }

    f = fopen(argv[4], "r");

    if (f == NULL)
    {
        printf("Unable to open %s.\n", argv[5]);
        printf(USAGE, argv[0]);

        return 0;
    }

    b = argv[1][0];
    k = atoi(argv[2]);
    m = atoi(argv[3]);

    if (b == 'e')
    {
        while (fread(&byte, 1, 1, f))
        {
            twobyte = (unsigned short int) mod_exp(byte, k, m);
            fwrite(&twobyte, 2, 1, stdout);
        }
    }
    else if (b == 'd')
    {
        while (fread(&twobyte, 2, 1, f))
        {
            byte = (unsigned char) mod_exp(twobyte, k, m);
            fwrite(&byte, 1, 1, stdout);
        }
    }

    fclose(f);

    return 0;
}
