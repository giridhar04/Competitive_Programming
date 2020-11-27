//bitwise operators

#include<stdio.h>

int main()
{
    int n,k,i,j,bit_and=0,bit_or=0,bit_xor=0,temp1,temp2,temp3;
    scanf("%d %d",&n,&k);

    for(i=1;i<=n-1;i++)
    {
        for(j=i+1;j<=n;j++)
        {
            temp1=i&j;
            temp2=i|j;
            temp3=i^j;

            if(temp1>=bit_and && temp1<k)
            {
                bit_and=temp1;
            }

            if(temp2>=bit_or && temp2<k)
            {
                bit_or=temp2;
            }

            if(temp3>=bit_xor && temp3<k)
            {
                bit_xor=temp3;
            }
            //printf("%d %d\n",i,j);
        }
        //printf("\n");
    }
    printf("%d\n%d\n%d\n",bit_and,bit_or,bit_xor);
}
