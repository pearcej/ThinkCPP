Activecode Exercises
--------------------

Answer the following **Activecode** questions to
assess what you have learned in this chapter.


.. tabbed:: vars_types_a1

   .. tab:: Question

      .. activecode:: vars_types_a1q
         :language: cpp

         Fix the code below so that it runs without errors.  Hint: you might
         need to change the names of some variables.
         ~~~~
         #include <iostream>
         using namespace std;

         int main () {
             char true = 'T';
             char false = 'F';
             cout << true << " is short for true. ";
             cout << false << " is short for false." << endl;

             // Do not modify anything below.
             return 0;
         }

   .. tab:: Answer

      .. activecode:: vars_types_a1a
         :language: cpp

         Below is one way to fix the program.  ``true`` and ``false`` are
         keywords, so they cannot be used as variable names.
         ~~~~
         #include <iostream>
         using namespace std;

         int main () {
             char t = 'T';
             char f = 'F';
             cout << t << " is short for true. ";
             cout << f << " is short for false." << endl;

             // Do not modify anything below.
             return 0;
         }    


.. activecode:: vars_types_a2
   :language: cpp

   Fix the code below so that it prints "I drive a 2014 Buick Regal".
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       string make;
       make = "Buick"

       string model = "Regal";

       string year = 2014;

       cout << "I drive a";  cout << " ";
       cout << year << model << make << endl.
   }


.. tabbed:: vars_types_a3

   .. tab:: Question

      .. activecode:: vars_types_a3q
         :language: cpp

         Fix the code below so that it prints "Cady scored 0.9 on the exam."
         Although this isn't how we'd usually tell people our scores, 0.9 is
         the C++ way of expressing 90%.
         ~~~~
         #include <iostream>
         using namespace std;
         int main() {
             int Cady = (3 * 5) * 6 / 100;
             cout << "Cady scored" << Cady <<"on the exam.";
         }

   .. tab:: Answer

      .. activecode:: vars_types_a3a
         :language: cpp

         Below is one way to fix the program.  We want to use doubles so that
         our result isn't rounded down to 0 through integer division.
         ~~~~
         int main() {
             double Cady = (3 * 5) * 6 / 100.0;
             cout << "Cady scored " << Cady <<" on the exam.";
         }    


.. activecode:: vars_types_a4
   :language: cpp

   Finish the code below so that it returns the correct volume of a sphere.  Hint: 
   think about what happens when you use integer division.
   ~~~~
   #include <iostream>
   using namespace std;

   int main () {
       int radius = 5;

       // Complete the line below.
       volume = ;

       // Do not modify anything below.
       cout << volume;
   }


.. tabbed:: vars_types_a5

   .. tab:: Question

      .. activecode:: vars_types_a5q
         :language: cpp

         Finish the code below so that assigns ``a`` its correct value of ``'a'``.  Hint:
         use character operations!
         ~~~~
         #include <iostream>
         using namespace std;

         int main () {
            char a = 's';

            // Complete the line below.
            a = ;

            // Do not modify anything below.
            cout << a;
         }

   .. tab:: Answer

      .. activecode:: vars_types_a5a
         :language: cpp

         Below is one way to complete the program.  There are many creative
         ways that you could use the order of operations to come up with a complex
         expression that will bring you to ``'a'``, here is one way.
         ~~~~
         #include <iostream>
         using namespace std;
      
         int main () {
            char a = 's';

            // Complete the line below.
            a = a - (3 * 5 + 3);

            // Do not modify anything below.
            cout << a;
         }


.. activecode:: vars_types_a6
   :language: cpp

   Write code that assigns "apples" to oranges, and "oranges" to apples,
   then swaps their values.  Be sure to inclue any necessary headers.
   YOU MAY NOT HARDCODE YOUR SOLUTION.
   ~~~~
   int main () {

   }


.. tabbed:: vars_types_a7

   .. tab:: Question

      .. activecode:: vars_types_a7q
         :language: cpp

         Write code that prints "Eat", "More", and "Chicken" on 3 consecutive lines.
         Be sure to inclue any necessary headers.
         ~~~~
         int main () {

         }

   .. tab:: Answer

      .. activecode:: vars_types_a7a
         :language: cpp

         Below is one way to implement the solution.
         ~~~~
         int main () {
             cout << "Eat" << endl;
             cout << "More" << endl;
             cout << "Chicken" << endl;
         } 


.. activecode:: vars_types_a8
   :language: cpp

   Write code that calculates how much you you will spend after tipping 20% on your
   $36.25 dinner.  Save the result of this calculation in ``plusTip``.  Be sure to 
   inclue any necessary headers.
   ~~~~
   int main () {

   }


.. tabbed:: vars_types_a9

   .. tab:: Question

      .. activecode:: vars_types_a9q
         :language: cpp

         You have about three hours and fifteen minutes of homework to do today.  Rather
         than starting it right away, you choose to procrastinate by calculating how many
         seconds you'll be spending on your work.  Convert the time to seconds and store the
         result in ``seconds``.  Be sure to inclue any necessary headers.
         ~~~~
         int main () {

         }

   .. tab:: Answer

      .. activecode:: vars_types_a9a
         :language: cpp

         Below is one way to implement the solution.
         ~~~~
         int main () {
             int hours = 3;
             int minutes = 15;
             int totalMinutes = minutes + 60 * hours;
             int seconds = totalMinutes * 60;
         }


.. activecode:: vars_types_a10
   :language: cpp

   Write code that calculates and prints the average of a and b if a = 3.14, 
   and b = 1.59.  You may only use one line of code.  Be sure to inclue any necessary headers.
   ~~~~
   int main () {

   }