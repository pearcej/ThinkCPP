Private functions
-----------------

In some cases, there are member functions that are used internally by a
class, but that should not be invoked by client programs. For example,
``calculatePolar`` and ``calculateCartesian`` are used by the accessor
functions, but there is probably no reason clients should call them
directly (although it would not do any harm). If we wanted to protect
these functions, we could declare them ``private`` the same way we do
with instance variables. In that case the complete class definition for
``Complex`` would look like:

::

   class Complex
   {
   private:
     double real, imag;
     double mag, theta;
     bool cartesian, polar;

     void calculateCartesian ();
     void calculatePolar ();

   public:
     Complex () { cartesian = false;  polar = false; }

     Complex (double r, double i)
     {
       real = r;  imag = i;
       cartesian = true;  polar = false;
     }

     void printCartesian ();
     void printPolar ();

     double getReal ();
     double getImag ();
     double getMag ();
     double getTheta ();

     void setCartesian (double r, double i);
     void setPolar (double m, double t);
   };

The ``private`` label at the beginning is not necessary, but it is a
useful reminder.

.. activecode:: fourteeneleven
   :language: cpp
   :compileargs: [ '-Wall', '-Werror' ]

   The active code below updates ``calculatePolar`` and ``calculateCartesian``
   to be private functions. Notice how we are no longer able to call 
   ``calculateCartesian`` in main. Feel free to modify the code and experiment around!
   ~~~~
   #include <iostream>
   #include <cmath>
   #include <cassert>
   using namespace std;

   class Complex
   {
     double real, imag;
     double mag, theta;
     bool cartesian, polar;
     void calculateCartesian ();
     void calculatePolar ();

   public:
     Complex ();
     Complex (double r, double i);
     double getReal ();
     double getImag ();
     double getMag ();
     double getTheta ();
     void printCartesian ();
     void printPolar ();
     void setPolar (double m, double t);
     void setCartesian (double r, double i);
   };

   Complex add (Complex& a, Complex& b);
   Complex subtract (Complex& a, Complex& b);
   Complex mult (Complex& a, Complex& b);

   int main() {
     Complex c1(-4.0, 0.0);
     c1.setPolar(4.0, 3.1415);
     // ``calculateCartesian`` can't be called in main because 
     // it is now a private member function
     c1.calculateCartesian();
   }
   ====
   Complex::Complex () { cartesian = false;  polar = false; }

   Complex::Complex (double r, double i) {
     real = r;  imag = i;
     cartesian = true;  polar = false;
   }

   void Complex::calculateCartesian () {
     assert (polar);
     real = mag * cos (theta);
     imag = mag * sin (theta);
     cartesian = true;
     assert (polar && cartesian);
   }

   double Complex::getReal () {
     if (cartesian == false) calculateCartesian ();
     return real;
   }

   double Complex::getImag () {
     if (cartesian == false) calculateCartesian ();
     return imag;
   }

   void Complex::calculatePolar () {
     mag = sqrt(pow(real, 2) + pow(imag, 2));
     theta = atan(imag / real);
     polar = true;
   }

   double Complex::getMag () {
     if (polar == false) {
       calculatePolar ();
     }
     return mag;
   }

   double Complex::getTheta () {
     if (polar == false) {
       calculatePolar ();
     }
     return theta;
   }

   void Complex::printCartesian () {
     cout << getReal() << " + " << getImag() << "i" << endl;
   }

   void Complex::printPolar () {
     cout << getMag() << " e^ " << getTheta() << "i" << endl;
   }

   Complex add (Complex& a, Complex& b) {
     double real = a.getReal() + b.getReal();
     double imag = a.getImag() + b.getImag();
     Complex sum (real, imag);
     return sum;
   }

   Complex subtract (Complex& a, Complex& b) {
     double real = a.getReal() - b.getReal();
     double imag = a.getImag() - b.getImag();
     Complex diff (real, imag);
     return diff;
   }

   void Complex::setPolar (double m, double t) {
     mag = m;  theta = t;
     cartesian = false;  polar = true;
   }

   Complex mult (Complex& a, Complex& b) {
     double mag = a.getMag() * b.getMag();
     double theta = a.getTheta() + b.getTheta();
     Complex product;
     product.setPolar (mag, theta);
     return product;
   }

   void Complex::setCartesian (double r, double i) {
     real = r;    imag = i;
     cartesian = true;  polar = false;
   }