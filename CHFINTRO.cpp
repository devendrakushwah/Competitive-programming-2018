#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,r;
    cin>>n>>r;
    while(n--)
    {
        int m;
        cin>>m;
        if(m>=r)
        {
            cout<<"Good boi\n";
        }
        else
        {
            cout<<"Bad boi\n";
        }
    }
    return 0;
}
