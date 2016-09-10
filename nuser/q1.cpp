#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <iomanip>      // std::setprecision
#include <algorithm>
#include <fstream>
#include <math.h>
using namespace std;
int main()
{
	long long int p1,p2,p3,w;
	cin>>p1>>p2>>p3>>w;
	long long int ar[3];
	ar[0]=p1+p2;
	ar[1]=p2+p3;
	ar[2]=p3+p1;
	sort(ar,ar+3);
	if(ar[2]>=w)
		cout<<"YES"<<endl;
	else
		cout<<"NO"<<endl;
	return 0;
}