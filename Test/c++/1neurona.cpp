#include<iostream>
#include<cmath>
#include<armadillo>
#include<cstdlib>
#include<iomanip>
#include<fstream>
#include<string>
#include</home/elchorco/Documentos/c++/Biblioteca/operadores/numeros.cpp>
using namespace std;
using namespace arma;
using namespace numeros;



float sigmoide(float);
float suma(int,int,Cube<float>,Cube<float>,Cube<float>);
void error(float&,Cube<float>,Cube<float>,float&,float&,float&,float&,float&,float&);




int main(){
string nombre_archivo("neurona1.dat");
fstream archivo_sal;
archivo_sal.open(nombre_archivo,ios::out);
int i;
float a001,a101,a002;
float e000,e010,e001,e101,e01,e11;
float sal=0.9,alpha=0.1;
Cube<float> a(3,3,3);
Cube<float> u(3,3,3);
Cube<float> w(3,3,3);
Mat<float> w0;
Mat<float> w1;
Mat<float> w2;
Mat<float> a0;
Mat<float> a1;
Mat<float> a2;
Mat<float> u0;
Mat<float> u1;
Mat<float> u2;

/********************VALORES INICIALES****************/

                    w0 << 1 << 2 << 0 << endr
                       << 0 << 0 << 0 << endr
                       << 0 << 0 << 0 << endr;

                    w1 << 3 << 0 << 0 << endr
                       << 2 << 0 << 0 << endr
                       << 0 << 0 << 0 << endr;

                    w2 << 0 << 0 << 0 << endr
                       << 0 << 0 << 0 << endr
                       << 0 << 0 << 0 << endr;

w.subcube(0,0,0   ,2,2,0)=w0;
w.subcube(0,0,1   ,2,2,1)=w1;
w.subcube(0,0,2   ,2,2,2)=w2;


                    u0 << 0 << 0 << 0 << endr
                       << 0 << 0 << 0 << endr
                       << 0 << 0 << 0 << endr;

                    u1 << 4 << 0 << 0 << endr
                       << 2 << 0 << 0 << endr
                       << 0 << 0 << 0 << endr;

                    u2 << 3 << 0 << 0 << endr
                       << 0 << 0 << 7 << endr
                       << 0 << 0 << 0 << endr;
u.subcube(0,0,0   ,2,2,0)=u0;
u.subcube(0,0,1   ,2,2,1)=u1;
u.subcube(0,0,2   ,2,2,2)=u2;

           


        a0 << 1 << 0 << 0 << endr
           << 0 << 0 << 0 << endr          //Datos de entrada! Capa 0
           << 0 << 0 << 0 << endr;

           a.subcube(0,0,0   ,2,2,0)=a0;

/*******************************************************/

for(i=0;i<=10000000;i++){

a001=sigmoide(suma(0,1,a,u,w));
a101=sigmoide(suma(1,1,a,u,w));
        a1 << a001 << 0 << 0 << endr
           << a101 << 0 << 0 << endr          //Capa 1
           << 0    << 0 << 0 << endr;
           a.subcube(0,0,1   ,2,2,1)=a1;
a002=sigmoide(suma(0,2,a,u,w));
        a2 << a002 << 0 << 0 << endr
           << 0    << 0 << 0 << endr         //Datos de salida!  Capa 2
           << 0    << 0 << 0 << endr;
           a.subcube(0,0,2   ,2,2,2)=a2;

error(sal,a,w,e000,e010,e001,e101,e01,e11);

if(0.5*pow(sal-a(0,0,2),2)*100>=0.5)
{
   w(0,0,0)-=alpha*e000;
   w(0,1,0)-=alpha*e010;
   w(0,0,1)-=alpha*e001;
   w(1,0,1)-=alpha*e101;

   u(0,0,1)-=alpha*e01;
   u(1,0,1)-=alpha*e11;
   
  archivo_sal << i <<"   "<<0.5*pow(sal-a(0,0,2),2)*100 
     << "  " << a(0,0,2)
     << "  " << w(0,0,0)
     << "  " << w(0,1,0)
     << "  " << w(0,0,1)
     << "  " << w(1,0,1)
     << "  " << u(0,0,1)
     << "  " << u(1,0,1) << endl;
   
}

else {

archivo_sal <<0.5*pow(sal-a(0,0,2),2)*100 
     << "  " << a(0,0,2)
     << "  " << w(0,0,0)
     << "  " << w(0,1,0)
     << "  " << w(0,0,1)
     << "  " << w(1,0,1)
     << "  " << u(0,0,1)
     << "  " << u(1,0,1) << endl;
exit(1);
}

}

archivo_sal.close();
return 0;
}



float suma(int i,int k,Cube<float> A,Cube<float> U,Cube<float> W)
{
    int j;
    float Z; 
    Z=U(i,0,k);
    for(j=0;j<=k;j++)
    {
        
        Z+=A(j,0,k-1)*W(j,i,k-1);
        
    }

return Z;
}

float sigmoide(float x){
return pow(1-pow(Exp(3),-x),-1);
}



void error(float& salida,Cube<float> A,Cube<float> W,float& error000,float& error010,float& error001,float& error101,float& error01,float& error11){
  float parcial000=A(0,0,0)*A(0,0,1)*(1-A(0,0,1))*W(0,0,1)*A(0,0,2)*(1-A(0,0,2));
  float parcial010=A(0,0,0)*A(1,0,1)*(1-A(1,0,1))*W(1,0,1)*A(0,0,2)*(1-A(0,0,2));
  float parcial001=A(0,0,1)*A(0,0,2)*(1-A(0,0,2));
  float parcial101=A(1,0,1)*A(0,0,2)*(1-A(0,0,2));

  float parcial01=A(0,0,1)*(1-A(0,0,1))*W(0,0,1)*A(0,0,2)*(1-A(0,0,2));
  float parcial11=A(1,0,1)*(1-A(1,0,1))*W(1,0,1)*A(0,0,2)*(1-A(0,0,2));

   /******ERROR******/
   
 error000=-(salida-A(0,0,2))*parcial000;
 error010=-(salida-A(0,0,2))*parcial010;
 error001=-(salida-A(0,0,2))*parcial001;
 error101=-(salida-A(0,0,2))*parcial101;
   


 error01=-(salida-A(0,0,2))*parcial01;
 error11=-(salida-A(0,0,2))*parcial11;


}

