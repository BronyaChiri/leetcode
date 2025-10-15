#include<stdio.h>
void insert_sort(int list[],int n);
void print_list(int list[],int n);
int main()
{int a[] = {15, 1, 53, 26, 43, 31, 47, 39, 8, 5
, 12, 25, 1, 93, 30, 60, 83, 58, 64, 3,
 23, 16, 97, 33, 77, 11, 28, 90, 59, 95};

int length = sizeof(a)/sizeof(a[0]);
insert_sort(a,length);
print_list(a,length);

    return 0 ;

}
void insert_sort(int list[],int n)
{ int i = 0 ,t = 0 ,tem = 0,k = 0;
for (i=1;i<n;i++){
        tem = list[i];
    for (t=0;t<i;t++){
        if(tem<list[t]) break;
    }
    for (k=i-1;k>=t;k--){
            list[k+1]=list[k];
            }
    list[t] = tem ;}
}
void print_list(int list[],int n)
{ int i = 0;
printf("%c",'[');
for (i=0;i<n;i++){
printf("%d%c",list[i],',');
}
printf("%c",']');
}
