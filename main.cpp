#include <iostream>
#include <string>

using namespace std;

int main()
{
    float buff = 0;

  /*16 вариант*/  float currMass[5][6]={
    {12, -1,  0,  4,  5,  0},
    {0,   6,  1,  0,  1,  7},
    {3,  -1,  2,  0, -1, -2},
    {-2,  0,  0,  5,  3, -2},
    {5,   0, -2,  0,  1,  1}
    };

/*14 вариант*/  /*  float currMass[5][6] = {
        {2, -3,  5,  0, -1,  8},
        {7, 15,  9,  6,  0, 22},
        {4, -1,  3,  7,  5,  9},
        {-2,11,  2,  9,  7,  2},
        {4,  7, -2,  2,  6, -2}
    };
*/
    float det = currMass[0][0];

    float L[5][6] ={
        {1, 0, 0, 0, 0, 0},
        {0, 1, 0, 0, 0, 0},
        {0, 0, 1, 0, 0, 0},
        {0, 0, 0, 1, 0, 0},
        {0, 0, 0, 0, 1, 0}
    };

    for(int z = 0;z < 5;++z){                    //цикл для элементов главной диагонали

        if(currMass[z][z] != 0){

            for(int i = z+1; i < 5; ++i){                  //цикл для уравнений

                buff = currMass[i][z]/currMass[z][z];
                L[i][z] = float(int(buff*1000))/1000;

                for(int j = z;j<6;j++){                  //цикл для элементов уравнения

                    currMass[i][j] =float(int(1000*(currMass[i][j]-currMass[z][j]*buff)))/1000;

                }
            }
            if(z<4)
                det=det*currMass[z+1][z+1];
        }
    }

    float x1=0, x2=0, x3=0, x4=0, x5=0;

    float massX[5]={ x1, x2, x3, x4, x5};

    massX[4] = float(int(currMass[4][5]/currMass[4][4]*1000))/1000;
    massX[3] = float(int((currMass[3][5]-(currMass[3][4]*massX[4]))/currMass[3][3]*1000))/1000;
    massX[2] = float(int((currMass[2][5]-(currMass[2][4]*massX[4]) - (currMass[2][3]*massX[3]))/currMass[2][2]*1000))/1000;
    massX[1] = float(int((currMass[1][5]-(currMass[1][4]*massX[4]) - (currMass[1][3]*massX[3])-(currMass[1][2]*massX[2]))/currMass[1][1]*1000))/1000;
    massX[0] = float(int((currMass[0][5]-(currMass[0][4]*massX[4]) - (currMass[0][3]*massX[3])-(currMass[0][2]*massX[2])-(currMass[0][1]*massX[1]))/currMass[0][0]*1000))/1000;


    for(int m = 0;m<5;++m){
        string x= "x"+to_string(m+1)+"=";
        cout<<x<<massX[m]<<endl;
    }


    cout<<endl<<endl<<"L="<<endl;
    for(int q=0;q<5;++q){         //вывод массива L
        cout<<endl;
        for(int w = 0;w<6;++w){
            cout<<L[q][w]<<"\t";
        }
    }


    cout<<endl<<endl<<"U="<<endl;
    for(int k=0;k<5;++k){         //вывод массива U
        cout<<endl;
        for(int y = 0;y<6;++y){
            cout<<currMass[k][y]<<"\t";
        }
    }


    det=float(int(det*1000))/1000;
    cout<<endl<<endl<<"det="<<det<<endl;

    return 0;
}
