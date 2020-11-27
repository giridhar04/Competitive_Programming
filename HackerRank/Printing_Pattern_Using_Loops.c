//printing pattern using loops

#include<stdio.h>

int main()
{
    int n,i,j,k;
    scanf("%d",&n);
    k=n;
    int sta_row=0,end_row=2*n-2,sta_col=0,end_col=2*n-2,arr[2*n-1][2*n-1];

    while(sta_row<=end_row && sta_col<=end_col)
    {
        for(i=sta_col;i<=end_col;i++)
        {
            arr[sta_row][i]=n;
        }
        sta_row++;

        for(i=sta_row;i<=end_row;i++)
        {
            arr[i][end_col]=n;
        }
        end_col--;

        if(sta_row<=end_row)
        {
            for(i=end_col;i>=sta_col;i--)
            {
                arr[end_row][i]=n;
            }
            end_row--;
        }

        if(sta_col<=end_col)
        {
            for(i=end_row;i>=sta_row;i--)
            {
                arr[i][sta_col]=n;
            }
            sta_col++;
        }
        n--;
    }
    //printf("hi %d\n",arr[0][1]);
    //printf("%d %d\n",k=2*n-2,j=2*n-2);

    for(i=0;i<=2*k-2;i++)
    {
        for(j=0;j<=2*k-2;j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
}
