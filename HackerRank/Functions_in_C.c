#include <stdio.h>

int maxi(int a,int b)
{
    if(a>=b)
    {
        return a;
    }
    else {
    return b;
    }
}

int main()
{
    int a,b,c,d;
    scanf("%d%d%d%d",&a,&b,&c,&d);

    printf("%d\n",maxi(maxi(a,b),maxi(c,d)));
}
