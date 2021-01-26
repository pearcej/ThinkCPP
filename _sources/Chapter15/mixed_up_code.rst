Mixed Up Code Practice
----------------------

.. parsonsprob:: mucp_15_1
   :numbered: left
   :adaptive:
   :noindent:
   :practice: T

   Let's write the class definition for <code>Circle</code>. <code>Circle</code> should have its
   radius stored in a private member variable. Also write the constructor 
   for <code>Circle</code>, which takes a radius as a parameter, in addition to the
   public member function <code>calculateArea</code>, which returns the area of 
   the <code>Circle</code>. Make sure to include the <code>private</code> and <code>public</code> keywords!
   Use 3.14 for the value of pi. Put the necessary
   blocks of code in the correct order.
   -----
   class Circle {   
   =====
   struct Circle {  #distractor
   =====
      private:
   =====
      private {  #distractor
   =====
      }  #distractor
   =====
         double radius;
   =====
      public:
   =====
         Circle (double r) { radius = r; }
   =====
         Circle (int r) { radius = r; }  #distractor
   =====
         double calculateArea () { return 3.14 * radius * radius; }
   };