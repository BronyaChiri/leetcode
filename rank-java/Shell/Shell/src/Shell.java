public class Shell{
    public Shell(){}

    public static void shellSort(int[] list){
        int h=1,i=0,j=0,t=0,n=list.length,k=0;
        while (h<n/3) {h = 3*h+1;}
        while(h>=1){
            for (i=0;i<h;i++){
                for (j=i+h;j<n;j+=h){
                    for (k=i;k<n-h-1;k+=h){
                    if (list[k]>list[k+h]) {t = list[k]; list[k]=list[k+h];list[k+h]=t;}
                    }
                }




            }
            h /= 3;
        }
    }

    public static void printList(int[] list){
        int i=0;
        System.out.print('{');
        for (i=0;i<list.length-1;i++){
            System.out.print(list[i]+",");
        }
        System.out.print(list[i]+"}");
    }

    public static void main(String []args){
        int[] a={70, 94, 48, 31, 89, 48, 11, 38, 41, 39, 35, 49, 71, 87, 70, 51, 78};
        shellSort(a);
        printList(a);

    }
}