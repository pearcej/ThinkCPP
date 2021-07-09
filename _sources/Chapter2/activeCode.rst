Activecode Exercises
--------------------

Answer the following **Activecode** questions to assess what you have learned in this chapter.


.. tabbed:: VARS_a1

   .. tab:: Question

      .. activecode:: VARS_a1q
         :language: cpp

         Fix the code below so that it runs without errors.  Hint: you might need to change the names of some variables.
         ~~~~
         #include <iostream>
         using namespace std;

         int main () {
             char true = 'T';
             char false = 'F';

             // DO NOT MODIFY ANYTHING BELOW THIS LINE.
             cout << true << " is short for true. ";
             cout << false << " is short for false." << endl;
         }
         
   .. tab:: Answer

      .. activecode:: VARS_a1a
         :language: cpp

         Below is one way to fix the program.  ``true`` and ``false`` are keywords, so they cannot be used as variable names.
         ~~~~
         #include <iostream>
         using namespace std;

         int main () {
             char t = 'T';
             char f = 'F';
             cout << t << " is short for true. ";
             cout << f << " is short for false." << endl;
         }    


.. tabbed:: VARS_a2_q

   .. tab:: Activecode

      .. activecode:: VARS_a2
         :language: cpp

         Finish the code below so that it prints "I drive a 2014 Buick Regal". Select the Parsonsprob tab for hints for the construction of the code.
         ~~~~
         #include <iostream>
         using namespace std;

         int main () {
            string make;
            make = "Buick"

            // Finish the rest of the assignment statements by assigning
            // 2014 and Regal to their respective variables.

            // DO NOT MODIFY ANYTHING BELOW THIS LINE.
            cout << "I drive a " << year << " " << make << " ";
            cout << model << endl.
         }

   .. tab:: Parsonsprob

      .. parsonsprob:: VARS_a2_p
         :numbered: left
         :adaptive:
         :noindent:

         Finish the code below so that it prints "I drive a 2014 Buick Regal". Use the lines to construct the code, then go back to complete the Activecode tab.

         -----
         int main() {
         =====
         string make;
         =====
         make = "Buick";
         =====
         int year;
         =====
         double year; #paired
         =====
         year = 2014;
         =====
         string model = "Regal";
         =====
         model = "Regal"; #paired
         =====
         cout << "I drive a " << year << " " << make << " ";
         =====
         cout << model << endl;
         =====
         }


.. tabbed:: VARS_a3

   .. tab:: Question

      .. activecode:: VARS_a3q
         :language: cpp

         Fix the code below so that it prints "Cady scored 90% on the exam." 
         ~~~~
         #include <iostream>
         using namespace std;

         int main() {
             // Modify the next line so that Cady = 0.9.
             int Cady = 3 * 5 * (6 / 100);

             // DO NOT MODIFY ANYTHING BELOW THIS LINE.
             cout << "Cady scored " << Cady * 100 << "% on the exam.";
         }

   .. tab:: Answer

      .. activecode:: VARS_a3a
         :language: cpp

         Below is one way to fix the program.  We want to use doubles so that our result isn't rounded down to 0 through integer division.
         ~~~~
         #include <iostream>
         using namespace std;

         int main() {
             double Cady = (3 * 5) * 6 / 100.0;
             cout << "Cady scored " << Cady * 100 << "% on the exam.";
         }    


.. tabbed:: VARS_a4_q

   .. tab:: Activecode

      .. activecode:: VARS_a4
         :language: cpp

         Finish the code below so that it returns the correct volume of a sphere. Select the Parsonsprob tab for hints for the construction of the code. Hint: think about what happens when you use integer division. The volume of a sphere is given by V = (4/3)(pi)(r^3).
         ~~~~
         #include <iostream>
         using namespace std;

         int main () {
            int radius = 5;
            double pi = 3.14;

            // Use these variables and the formula for volume to complete the next line.
            volume = 

            // DO NOT MODIFY ANYTHING BELOW THIS LINE.
            cout << "Your solution had volume = " << volume << endl;  cout << "The correct solution has volume = 104.667";
         }

   .. tab:: Parsonsprob

      .. parsonsprob:: VARS_a4_p
         :numbered: left
         :adaptive:
         :noindent:

         Finish the code below so that it returns the correct volume of a sphere. Use the lines to construct the code, then go back to complete the Activecode tab. The volume of a sphere is given by V = (4/3)(pi)(r^3).

         -----
         int main() {
         =====
         int radius = 5;
         =====
         double pi = 3.14;
         =====
         double volume;
         =====
         int volume; #paired
         =====
         volume = 4 * pi * radius * radius * radius / 3;
         =====
         volume = (4/3) * pi * radius * radius * radius; #paired
         =====
         volume = 4 * pi * radius * radius / 3; #paired
         =====
         cout << "Your solution had volume = " << volume << endl;
         =====
         cout << "The correct solution has volume = 104.667";
         =====
         }


.. tabbed:: VARS_a5

   .. tab:: Question

      .. activecode:: VARS_a5q
         :language: cpp

         Fix the code below so that assigns ``a`` its correct value of ``'a'``.  Hint: use character operations!
         ~~~~
         #include <iostream>
         using namespace std;

         int main () {
            char a = 's';

            // Fix the line below.  Do NOT change the numbers!  Instead, 
            // change the location of the parentheses.
            a = a - 3 * 4 + (1 + 3);

            // DO NOT MODIFY ANYTHING BELOW THIS LINE.
            cout << a;
         }

   .. tab:: Answer

      .. activecode:: VARS_a5a
         :language: cpp

         Below is one way to complete the program.  There are many creative ways that you could use the order of operations to come up with a complex expression that will bring you to ``'a'``, here is one way.
         ~~~~
         #include <iostream>
         using namespace std;
      
         int main () {
            char a = 's';
            a = a - (3 * (4 + 1) + 3);
            cout << a;
         }


.. tabbed:: VARS_a6_q

   .. tab:: Activecode

      .. activecode:: VARS_a6
         :language: cpp

         Write code that assigns "apples" to the variable oranges, and "oranges" to the variable apples, then swaps their values.  Be sure to inclue any necessary headers.  YOU MAY NOT HARDCODE YOUR SOLUTION. Select the Parsonsprob tab for hints for the construction of the code.
         ~~~~
         int main () {
            
            // DO NOT MODIFY ANYTHING BELOW THIS LINE.
            cout << "Your solution had apples = " << apples << "and oranges = " << oranges << "." << endl; cout << "The correct solution has apples = apples, and oranges = oranges.";
         }

   .. tab:: Parsonsprob

      .. parsonsprob:: VARS_a6_p
         :numbered: left
         :adaptive:
         :noindent:

         Write code that assigns "apples" to the variable oranges, and "oranges" to the variable apples, then swaps their values.  Be sure to inclue any necessary headers. 
         Use the lines to construct the code, then go back to complete the Activecode tab.

         -----
         int main() {
         =====
         string oranges = "apples";
         =====
         string apples = "oranges";
         =====
         string temp = apples;
         =====
         string temp = "apples"; #paired
         =====
         string temp = "oranges"; #paired
         =====
         apples = oranges;
         =====
         apples = "oranges"; #paired
         =====
         oranges = temp;
         =====
         oranges = "temp"; #paired
         =====
         cout << "Your solution had apples = " << apples << " and oranges = " << oranges << "." << endl;
         =====
         cout << "The correct solution has apples = apples, and oranges = oranges.;
         =====
         }


.. tabbed:: VARS_a7

   .. tab:: Question

      .. activecode:: VARS_a7q
         :language: cpp

         Write code that prints "Eat", "More", and "Chicken" on 3 consecutive lines. Be sure to inclue any necessary headers.
         ~~~~
         int main () {

         }

   .. tab:: Answer

      .. activecode:: VARS_a7a
         :language: cpp

         Below is one way to implement the solution.
         ~~~~
         #include <iostream>
         using namespace std;

         int main () {
             cout << "Eat" << endl;
             cout << "More" << endl;
             cout << "Chicken" << endl;
         } 


.. tabbed:: VARS_a8_q

   .. tab:: Activecode

         .. activecode:: VARS_a8
            :language: cpp

            Write code that calculates how much you you will spend after tipping 20% on your $36.25 dinner.  Save the result of this calculation in ``plusTip``.  Be sure to include any necessary headers. Select the Parsonsprob tab for hints for the construction of the code.
            ~~~~
            int main () {

               // DO NOT MODIFY ANYTHING BELOW THIS LINE.
               cout << "Your solution had plusTip = " << plusTip << endl; cout << "The correct solution has plusTip = 43.5";
            }

   .. tab:: Parsonsprob

      .. parsonsprob:: VARS_a8_p
         :numbered: left
         :adaptive:
         :noindent:

         Write code that calculates how much you you will spend after tipping 20% on your $36.25 dinner.  Save the result of this calculation in ``plusTip``. Use the lines on to construct the code, then go back to complete the Activecode tab.

         -----
         int main() {
         =====
         double price = 36.25;
         =====
         double tip = 1.20;
         =====
         double tip = .20; #paired
         =====
         int tip = 20; #paired
         =====
         double plusTip = tip * price;
         =====
         double plusTip = (tip * price) + price; #paired
         =====
         cout << "Your solution had a plusTip = " << plusTip << endl;
         =====
         cout << "The correct solution has a plusTip = 43.5";
         =====
         }


.. tabbed:: VARS_a9

   .. tab:: Question

      .. activecode:: VARS_a9q
         :language: cpp

         You have about three hours and fifteen minutes of homework to do today.  Rather than starting it right away, you choose to procrastinate by calculating how many seconds you'll be spending on your work.  Convert the time to seconds and store the result in ``seconds``.  Be sure to inclue any necessary headers.
         ~~~~
         int main () {

             // DO NOT MODIFY ANYTHING BELOW THIS LINE.
             cout << "Your solution had seconds = " << seconds << endl;  cout << "The correct solution has seconds = 11700";
         }

   .. tab:: Answer

      .. activecode:: VARS_a9a
         :language: cpp

         Below is one way to implement the solution.
         ~~~~
         #include <iostream>
         using namespace std;

         int main () {
             int hours = 3;
             int minutes = 15;
             int totalMinutes = minutes + 60 * hours;
             int seconds = totalMinutes * 60;
         }


.. tabbed:: VARS_a10_q

   .. tab:: Activecode
   
      .. activecode:: VARS_a10
         :language: cpp

         Write code that calculates and prints the average of a and b if a = 3.14, and b = 1.59.  You may only use one line of code.  Be sure to inclue any necessary headers. Select the Parsonsprob tab for hints for the construction of the code.
         ~~~~
         int main () {

            // DO NOT MODIFY ANYTHING BELOW THIS LINE.
            cout << "Your program should have printed 2.365";
         }

   .. tab:: Parsonsprob

      .. parsonsprob:: VARS_a10_p
         :numbered: left
         :adaptive:
         :noindent:

         Write code that calculates and prints the average of a and b if a = 3.14, and b = 1.59.  You may only use one line of code. Use the lines on to construct the code, then go back to complete the Activecode tab.

         -----
         int main() {
         =====
         cout << (3.14 + 1.59) / 2 << endl;
         =====
         cout << (1/2) * (3.14 + 1.59) << endl; #paired
         =====
         }