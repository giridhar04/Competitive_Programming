#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

void array_swap(float *ptr1,float *ptr2)
{
    float temp=*ptr1;
    *ptr1=*ptr2;
    *ptr2=temp;
}
void struct_swap(triangle *ptr1,triangle *ptr2)
{
    triangle temp=*ptr1;
    *ptr1=*ptr2;
    *ptr2=temp;
}

void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    int i=0,min_index,j;
    float area,p,array_area[n];

    for(i=0;i<n;i++)
    {
        p=(((tr+i)->a)+((tr+i)->b)+((tr+i)->c));
        p=p/2;
        area=sqrt((p)* (p-(tr+i)->a)* (p-(tr+i)->b) *(p-(tr+i)->c));
        array_area[i]=area;
    }

    for(i=0;i<n;i++)
    {
        min_index=i;
        for(j=i;j<=n-1;j++)
        {
            if(array_area[min_index]>array_area[j])
            {
                min_index=j;
            }
        }
        array_swap(&array_area[i],&array_area[min_index]);
        struct_swap(tr+i,tr+min_index);
    }

}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
