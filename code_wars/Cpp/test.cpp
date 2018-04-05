#include <iomanip>
#include <iostream>
using namespace std;

int main()
{
	int num = 45;
	cout << "This is suppose to show "<< num << " and stop."<<endl;
	int num2;
	cout << "Enter a second number:";
	cin >> num2; /*num2 = 23*/
	cout << "This is the second number:"<< num2 << endl;
	return 0;
}

/*
Enter number of students: 2
Enter student First name: Manal
Enter student Last name: Garga
How many courses do you have: 3
Enter course letter grade for course 1: A
Enter credit hours for course 1: 3
Enter course letter grade for    course 2: U
Not valid grade
Enter course letter grade for course 2: B
Enter credit hours for course 2: 4
Enter course letter grade for course 3: B
Enter credit hours for course 3: 2

Total GPA Grade for Manal Garga is: 3.67

*/
