//printing tokens

#include<stdio.h>

int main()
{
    char str[1000];
    int i=0;

    scanf("%[^\n]",str);

    while(str[i] != '\0')
    {
        if(str[i]==' ')
        {
            i=i+1;
            printf("\n");
            continue;
        }
        printf("%c",str[i]);
        i++;
    }
}
