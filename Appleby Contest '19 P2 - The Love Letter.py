"""
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>


int len___;
int key;
char[] plaintext;
char temp;


int main(int argc, char** argv)
{	
	logic:
    scanf("%n", len___);
	scanf("%n", key);
	scanf("%s", plaintext);
	char ciphertext[strlen(plaintext)];
	
	for(int i = 0; i < strlen(plaintext); i++)
	{
	    if(isalpha(plaintext[i]))
	    {
	        if(isupper(plaintext[i]))
	        {
	            if(key > 65)
	            {
	                key -= 65;
	            }
	            temp = ((plaintext[i] + key- 'A') % 26);
	            ciphertext[i] = temp + 'A';
	        }
	        else
	        {
	            if(key > 97)
	            {
	                key -= 97;
	            }
	            temp = ((plaintext[i] +key- 'a') % 26);
	            ciphertext[i] = temp + 'a';
	        }
	    }
	    else
	    {
	        ciphertext[i] = plaintext[i];
	    }
	}
	printf("%s\n", ciphertext);
}
"""

N = int(input())
key = int(input())
plaintext = input()

ciphertext = []

for i in range(len(plaintext)):
    if(plaintext[i].isalpha()):
        if(plaintext[i].isupper()):
            if(key > 65):
                key -= 65
            temp = ((ord(plaintext[i]) + key- ord('A')) % 26)
            ciphertext.append(chr(temp + ord('A')))
        else:
            if(key > 97):
                key -= 97
            temp = ((ord(plaintext[i]) + key- ord('a')) % 26)
            ciphertext.append(chr(temp + ord('a')))
    else:
        ciphertext.append(plaintext[i])

for i in ciphertext:
    print(i, end="")
print("")