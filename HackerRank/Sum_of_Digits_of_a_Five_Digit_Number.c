#include<stdio.h>

int sum_of_digits(int n)
{
    if(n<10)
    {
        return n;
    }
    else
    {
        return (n%10)+sum_of_digits(n/10);
    }
}

int main()
{
    long long int n;
    scanf("%lld",&n);
    printf("%d\n",sum_of_digits(n));
}
