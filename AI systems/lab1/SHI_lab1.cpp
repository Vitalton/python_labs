#include <iostream>
#include<math.h>
#include<cmath>
#define n 2
using namespace std;

void L(int num_1[n], int num_2[n]) {
	double result_1 = 0.0; //arg for 1.2
	double result_2 = 0.0; //arg for 1.3
	double result_3 = 0.0; //arg for 1.5
	double result_4 = 0.0; //1.11
	double result_5 = 0.0; //1.22
	double result_6 = 0.0; //1.23
	double result_7 = 0.0; //1.24
	double result_8 = 0.0; //1.25

	double a = 0.0;
	double b = 0.0;
	double g = 0.0;
	double h = 0.0;
	double k = 0.0;

	int N = 5; // coefficient for 1.5
	cout << "S(";  
	for (int i = 0; i < n; i++) {
		cout << num_1[i];
		if(i==0)
		cout << ",";
	}
	cout <<")"<< endl;  // show attributes of S

	cout << "X(";
	for (int i = 0; i < n; i++) {
		cout << num_2[i];
		if (i == 0)
		cout << ",";
	}
	cout << ")" << endl; // show attributes of X

	//1.2
	for (int i = 0; i < n; i++) {
		result_1 = pow(num_1[i] - num_2[i], 2) + result_1; // whole  formula without sqrt
	}
	result_1 = sqrt(result_1);
	cout <<"1.2 |Result: " << result_1 << endl;
	
	//1.3

	for (int i = 0; i < n; i++) {
		result_2 = pow(num_1[i] - num_2[i], 4) + result_2; // whole  formula without root of 4
	}
	result_2 = pow(result_2,1.0/4.0);
	cout << "1.3 |Result: " << result_2 << endl;

	//1.5

	for (int i = 0; i < n; i++) {
		result_3 = N*(pow(num_1[i] - num_2[i], 2)) + result_3; // whole  formula without sqrt
	}
	result_3 = sqrt(result_3);
	cout << "1.5 |Result: " << result_3 << endl;

	//1.8
	double resultFL_2 = 0.0;
	double resultFL = 0.0;
	double result = 0.0;

	for (int i = 0; i < n; i++) {
		resultFL = abs(num_1[i] - num_2[i]);
		resultFL_2 = abs(num_1[i] + num_2[i]); 
		result = (resultFL / resultFL_2) + result;
		//result_4 = (abs(num_1[i] - num_2[i]) / abs(num_1[i] + num_2[i])) + result_4;
	}
	cout << "1.8 |Result: " << result << endl;

	//1.11
	for (int i = 0; i < n;i++) {
		result_4 = acos((num_1[i] * num_2[i] + num_1[i + 1] * num_2[i + 1]) / sqrt( pow(num_1[i],2) + pow(num_1[i+1], 2)) * sqrt(pow(num_1[i], 2) + pow(num_1[i + 1], 2)));
		break;
	}
	cout << "1.11 |Result: " << result_4 << endl;
	
	//1.22
	for (int i = 0; i < n; i++) {
		a = num_1[i] * num_2[i] + a;

		b = ((1 - num_1[i])*(1 - num_2[i])) + b;

		g = (num_1[i] * (1 - num_2[i])) + g;

		h = ((1 - num_1[i]) * num_2[i]) + h;
	}

	cout << endl << "a: " << a << endl;
	cout << "b: " << b << endl;
	cout << "g: " << g << endl;
	cout << "h: " << h << endl << endl;

	result_5 = a / (a + b + g + h);
	cout << "1.22 |Result: " << result_5 << endl;

	k = a / result_5;

	//1.23

	result_6 = a / (a + g + h);
	cout << "1.23 |Result: " << result_6 << endl;

	//1.24

	result_7 = a / (2 * a + g + h);
	cout << "1.24 |Result: " << result_7 << endl;


	//1.25
	
	result_8 = a / (a + 2 * (g + h));
	cout << "1.25 |Result: " << result_8 << endl;
}

int main()
{


	int s[n];
	int x[n];

	cout << "Two attributes!" << endl << endl;

	cout << "Enter the first attribute for S : ";
	for (int i = 0; i < n; i++) {
		cin >> s[i];
		if(i==0)
		cout << "Enter the second attribute for S : ";
	}
	cout << endl;


	cout << "Enter the second attribute for X : ";
	for (int i = 0; i < n; i++) {
		cin >> x[i];
		if (i == 0)
		cout << "Enter the second attribute for X : ";
	}
	cout << endl;

	L(s, x);
}

