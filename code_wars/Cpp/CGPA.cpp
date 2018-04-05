/*
1 - The user will enter the number of students that he/she want to calculate the CGPA.

2 - The program will prompt the user to enter the first name and last name of the student

3 - The program will prompt the user to enter the number of courses.

4 - For each course, the program will prompt the user to enter the letter grade received in the course, and the number of credit hours of the course.

4 - After capturing the course letter grade, ang the credit for each course the program should calculate the cumulative GPA and display it to the user.


5 - The process will repeat for each student based on the number of students entered by the user.


### Output:

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

#include <iostream>
#include <iomanip>
using namespace std;

main()
{
	
	// Variables

	int numberOfStudents;
	string firstName;
	string lastName;
	int numberOfCourses;
	char grade;
	double gradeValue;
	int credit;
	int totalCredit;	// sum of credits
	double GWA; 			// gradeValue * credit
	double totalGWA; // sum of GWA
	double CGPA;	// totalGWA / totalCredit 

	cout << "Enter number of students: ";
	cin >> numberOfStudents;

	// First loop based on the number of students

	for(int i = 1; i <= numberOfStudents; i += 1)
	{
		// Students Names

		cout << "Enter student First name: ";
		cin >> firstName;
		cout << "Enter student Last name: ";
		cin >> lastName;

		// Number of courses

		cout << "How many courses do you have: ";
		cin >> numberOfCourses;

		// Secodn loop based on the number of courses;

		for(int j = 1; j <= numberOfCourses; j += 1)
		{
			

			bool b = true;  // boolean for the while loop

			while(b)
			{

				// Grade input

				cout << "Enter course letter grade for course " << j << ":";
				cin >> grade;

				switch(grade)
				{
					case 'A':
						gradeValue = 4.0;
						b = false;
						break;

					case 'B':
						gradeValue = 3.5;
						b = false;
						break;

					case 'C':
						gradeValue = 3.0;
						b = false;
						break;

					case 'D':
						gradeValue = 2.0;
						b = false;
						break;

					case 'F':
						gradeValue = 0;
						b = false;
						break;

					default:
						cout << "Not valid grade" << endl;
						cin.clear(); // clear the later input
					
				} // end switch (gradeValues)


			} // end while (errors)

			// Credit hours
			
			cout << "Enter credit hours for course " << j << ":";
			cin >> credit;

			// Most of the calculations

			totalCredit += credit;
			GWA = gradeValue * credit;
			totalGWA += GWA;

		} // end for (for number of courses )
		
		// Final calculation

		CGPA = totalGWA / totalCredit;

		

		cout << "\n\n"; // 2 newlines

		// CGPA for each students

		cout << "Total GPA for " << firstName << " " << lastName << " is: " << fixed << setprecision(2) << CGPA << endl;

		cout << "==============================================" << endl;

	} //end for (number of students)

}
