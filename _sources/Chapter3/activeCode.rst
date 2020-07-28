Activecode Exercises
--------------------

Answer the following **Activecode** questions to
assess what you have learned in this chapter.


.. tabbed:: functions_a1

   .. tab:: Question

      .. activecode:: functions_a1q
         :language: cpp

         Fix the code below so that it prints the area of a circle
         with radius 5.
         ~~~~
         #include <iostream>
         using namespace std;

         void printArea(double r) {
             double pi = acos(-0.5);
             double area = pi * r * r;
             cout << area;
         }

         int main () {
             printArea(5);
         }

   .. tab:: Answer

      .. activecode:: functions_a1a
         :language: cpp

         Below is one way to fix the program.  The *area* of a circle is 
         given by ``pi * r * r``, while the *circumference* is given by 
         ``2 * pi * r``.
         ~~~~
         #include <iostream>
         #include <cmath>
         using namespace std;

         void printArea(double r) {
             double pi = acos(-1.0);
             double area = pi * r * r;
             cout << area;
         }

         int main () {
             printArea(5);
         }


.. activecode:: functions_a2
   :language: cpp

   Fix the code below so that it prints "2 elephants".
   ~~~~
   #include <iostream>
   using namespace std;

   void printAnimals(string a, int b) {
       cout << b << a;
   }

   int main () {
       printAnimals(2, "elephants");
   }


.. tabbed:: functions_a3

   .. tab:: Question

      .. activecode:: functions_a3q
         :language: cpp

         Fix the code below so that it prints ``12 / 8 = 1.5.``
         ~~~~
         #include <iostream>
         using namespace std;

         void divide (int a, int b) {
             cout << a / b;
         }

         int main () {
             int a = 8;
             int b = 12;
             cout << b << " / " << a << " = ";
             divide (a, b);
         }

   .. tab:: Answer

      .. activecode:: functions_a3a
         :language: cpp

         Below is one way to fix the program.  It's crucial that
         you input your arguments in the correct order so as to
         avoid a semantic error.  Also, it's important that you
         understand that when you divide two integers... you will
         get an integer as a result.
         ~~~~
         #include <iostream>
         using namespace std;

         void divide (double a, double b) {
             cout << a / b;
         }

         int main () {
             int a = 8;
             int b = 12;
             cout << b << " / " << a << " = ";
             divide (b, a);
         }


.. activecode:: functions_a4
   :language: cpp

   Finish the code below so that it calculates the log of ``a``
   minus the *natural* log of ``a`` and prints the difference.
   You will need to use cmath functions.
   ~~~~
   #include <iostream>
   using namespace std;

   void logSubtraction (int a) {
       difference = ;
       cout << difference;
   }


.. tabbed:: functions_a5

   .. tab:: Question

      .. activecode:: functions_a5q
         :language: cpp

         Finish the code below so that it prints "First Line", a border,
         and "Second Line." on three separate lines.
         ~~~~
         #include <iostream>
         using namespace std;

         void border () {
             cout << "------------" << endl;
         }

         int main () {
             return 0;
         }

   .. tab:: Answer

      .. activecode:: functions_a5a
         :language: cpp

         Below is one way to complete the program.
         ~~~~
         #include <iostream>
         using namespace std;

         void border () {
             cout << "------------" << endl;
         }

         int main () {
             cout << "First Line." << endl;
             border();
             cout << "Second Line." << endl;
             return 0;
         }


.. activecode:: functions_a6
   :language: cpp

   Write a function called ``doubleDiv`` that takes two 
   doubles as parameters, converts them to integers, and
   prints the quotient of the first number divided by the
   second.  Be sure to include any necessary headers.
   ~~~~
   void doubleDiv () {
      
   }


.. tabbed:: functions_a7

   .. tab:: Question

      .. activecode:: functions_a7q
         :language: cpp

         Write a function called gpaBoost that prints your
         GPA rounded up to the nearest point.  Be sure to 
         include any necessary headers.
         ~~~~
         void gpaBoost () {

         }

   .. tab:: Answer

      .. activecode:: functions_a7a
         :language: cpp

         Below is one way to complete the program.  I used the
         ``ceil`` function from the ``cmath`` library, but you
         could have solved this problem without using any functions
         from ``cmath``.
         ~~~~
         #include <iostream>
         #include <cmath>
         using namespace std;

         void gpaBoost (double GPA) {
             int betterGPA = ceil(GPA);
             cout << betterGPA << ".000";
         }


.. activecode:: functions_a8
   :language: cpp

   Write a function called ``volumeSphere`` that takes a radius
   as a parameter, and calculates and prints the volume of a sphere 
   with that radius.  Be sure to include any necessary headers.
   ~~~~
   void volumeSphere () {
      
   }


.. tabbed:: functions_a9

   .. tab:: Question

      .. activecode:: functions_a9q
         :language: cpp

         Write a function called ``tanD`` that prints the tangent
         of an angle given in degrees. Use 3.14 for pi.  Be sure to include
         any necessary headers.
         ~~~~
         void tanDegrees (double degrees) {

         }


   .. tab:: Answer

      .. activecode:: functions_a9a
         :language: cpp

         Below is one way to complete the program.  Cotangent, arctangent,
         and ``atan`` from the ``cmath`` library are all the same.  You just
         need to make sure to convert your angle to radians before doing any
         calculations with sinusoidal functions.
         ~~~~
         #include <iostream>
         #include <cmath>
         using namespace std;

         void tanDegrees (double degrees) {
             double radians = degrees * (2 * 3.14) / 360.0;
             double tangent = tan(radians);
             cout << tangent;
         }


.. activecode:: functions_a10
   :language: cpp

   Write a function called ``volumeSphere`` that takes a radius
   as a parameter, and calculates and prints the volume of a sphere 
   with that radius.  Be sure to include any necessary headers.
   ~~~~
   void volumeSphere () {
      
   }