#include<stdio.h>
#include<stdlib.h>

void update(int *ptr1,int *ptr2)
{   
    int *temp;
    *temp=*ptr1;

    *ptr1=*ptr1+ *ptr2;
    *ptr2=abs(*temp - *ptr2);
}

int main()
{
    int a,b;
    scanf("%d%d",&a,&b);

    update(&a,&b);
    printf("%d\n%d\n",a,b);
}
