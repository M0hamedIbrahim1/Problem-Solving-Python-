#   link   : https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/U
#   author : Mohamed ibrahim


  
  #include <iostream>
using namespace std;

int main()
{
   int n1,n2,n3;
   long long ss=0;
   cin>>n1>>n2>>n3;
   
   for(int i=1;i<=n1;i++){
   	int mynum=i;
   	int sum = 0;
   	
   	   while(mynum){
	   	int m =mynum%10;
	   	sum +=m;
	   	mynum=mynum/10;
   }
   if(sum>=n2 && sum<=n3){
   	ss +=i;
  }
   
   	
   }
   cout<<ss;
}


