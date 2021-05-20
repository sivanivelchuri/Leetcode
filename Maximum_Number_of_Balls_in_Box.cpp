class Solution {
    int add(int n)
    {
        int sum=0;
        if(n==0)
        {
            return 0;
        }
        else{
            return n%10+add(int(n/10));
        }
    }
public:
    int countBalls(int lowLimit, int highLimit) {
        int ar[100001]={0};
        int i=0,s=0;
        for(int i=lowLimit;i<=highLimit;i++)
        {
            s=add(i);
            ar[s]+=1;
        }
        int maxi=0;
        for(i=0;i<=highLimit;i++)
        {
            if(ar[i]>maxi)
            {
                maxi=ar[i];
            }
        }
        return maxi;
    }
};