//Here Iam including only the function part of the question [Only this one is akesd in question]

// Complete the bonAppetit function below.
void bonAppetit(int bill_count, int* bill, int k, int b)
{
    int combined_actual_bill=0,anna_actual_bill=0,i;
    
    for(i=0;i<bill_count;i++)
    {
        combined_actual_bill+=*(bill+i);
    }
    
    anna_actual_bill=((combined_actual_bill)-(*(bill+k)))/2;
    
    if(b==anna_actual_bill)
    {
        printf("Bon Appetit\n");
    }
    else
    {
        printf("%d\n",*(bill+k)/2);
    }
}
