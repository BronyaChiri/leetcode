//三重循环滑动条暴力法

int lengthOfLongestSubstring(char* s) {
    char *p=s,*t=s;
    int n=0,count=0,countmax=0;
    n = strlen(s);
    for (p=s;p<s+n;p++){
        char *k=p;
        count=0;
        for(t=p;t<s+n;t++){
            char c=*t;
            for(k=p;k<t;k++){
                if (*k==c) break;
            }
            if (k==t) {count++;
            if(count>countmax) countmax=count;}
            else {count=0;break;}
        }
    }
    return countmax;
}