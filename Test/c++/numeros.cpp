#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

namespace numeros 
{

float Pi(int);
float Exp(int);
float Fac(int);


//PI

float Pi(int x){

cout << setprecision(x+1);

return asin(1.0)*2.0;
}


//Factorial

float Fac(int N){
int i;
int fac;
fac=1;
i=1;

if(N==0)
fac=1;
else{
while(i<=N){
fac*=i;
i++;
}
}

return fac;
}


//Euler

float Exp(int x){
float e=1;
int i;
for(i=1;i<=x;i++){
e+=1/Fac(i);

}
return e;
}


} //Fin del namespace
