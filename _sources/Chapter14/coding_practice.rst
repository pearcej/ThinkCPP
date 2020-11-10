Coding Practice
---------------

.. tabbed:: cp_14_1

    .. tab:: Question

        Create the enumerated type Planet, which maps the planets in our solar system to integers
        starting at 1. Make sure to list the planets out in order! (Sadly, Pluto is not a planet :( )

        .. activecode:: cp_14_AC_1q
           :language: cpp
           :practice: T

           #include <iostream>
           using namespace std;

           // Write your code for the enumerated type Planet.

    .. tab:: Answer

        Below is one way to implement the program. The planets in our solar system
        are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.

        .. activecode:: cp_14_AC_1a
           :language: cpp
           :optional:

           #include <iostream>
           using namespace std;

           enum Planet { MERCURY = 1, VENUS, EARTH, MARS, JUPITER, SATURN, URANUS, NEPTUNE };

.. activecode:: cp_14_AC_2q
    :language: cpp

    How long is a year on other planets? Let's write a program that prints out the number of days
    in a year on each planet using a switch statement. These values are, in planetary order, 
    88 days, 225 days, 365 days, 687 days, 4333 days, 10759 days, 30687 days, and 60190 days.
    Print out this information in the following format: Planet ``planet`` has ``numDays`` number of days in
    a year!
    ~~~~
    #include <iostream>
    using namespace std;

    enum Planet { MERCURY = 1, VENUS, EARTH, MARS, JUPITER, SATURN, URANUS, NEPTUNE };

    int main() {
        Planet p = JUPITER;
        // Write your code here.
    }
