Mixed Up Code Practice
----------------------

.. parsonsprob:: mucp_14_1
   :numbered: left
   :adaptive:
   :noindent:
   :practice: T

   Below is the enumerated type Days which maps days of the week to integers
   starting at 1. Use a switch statement to determine whether or not day
   is a weekend or not. Check for cases in numerical order.
   -----
   enum Day { MON = 1, TUE, WED, THU, FRI, SAT, SUN };
   =====
   int main () {
   =====
      Day day = SUN;
   =====
      switch (day > 5) {
   =====
         case 0:
   =====
            cout << "It is not the weekend :(" << endl;
   =====
            break;
   =====
         case 1:
   =====
            cout << "It is the weekend :)" << endl;
   =====
            break;
   =====
         default:
   =====
            cout << "Invalid input." << endl;
   =====
            break;
   =====
      }
   =====
   }