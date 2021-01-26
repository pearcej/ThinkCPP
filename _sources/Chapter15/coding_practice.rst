Coding Practice
---------------

.. tabbed:: cp_15_1

    .. tab:: Question

        Below is the ``struct`` definition for ``Room``, which has a length,
        width, and height. It also has two member functions, ``calculateArea``
        and ``calculateVolume``. Turn this ``struct`` into a ``class`` with 
        private member variables.

        .. activecode:: cp_15_AC_1q
           :language: cpp
           :practice: T

           #include <iostream>
           using namespace std;

           // Turn the struct definition of Room into a class definition.
           struct Room {
               int length;
               int width;
               int height;

               int calculateArea () {
                   return length * width;
               }

               int calculateVolume () {
                   return length * width * height;
               }
           };

    .. tab:: Answer

        Below is the ``class`` definition of ``Room``. As you can see, there isn't 
        a big difference between ``struct``\s and ``class``\es.

        .. activecode:: cp_15_AC_1a
           :language: cpp
           :optional:

           #include <iostream>
           using namespace std;

           class Room {
               private: 
                   int length;
                   int width;
                   int height;

               public:  
                   int calculateArea () {
                       return length * width;
                   }

                   int calculateVolume () {
                       return length * width * height;
                   }
           };

.. activecode:: cp_15_AC_2q
    :language: cpp

    There are errors in the code below. Modify the code so that ``main`` runs
    successfully. 
    ~~~~
    #include <iostream>
    using namespace std;

    class Room {
        private: 
            int length;
            int width;
            int height;

        public:  
            int calculateArea () {
                return length * width;
            }

            int calculateVolume () {
                return length * width * height;
            }

            // Add any necessary functions here.
    };

    int main() {
        Room r;
        r.length = 12;
        r.width = 14;
        r.height = 10;
        cout << "The room with dimensions " << r.length ", " << r.width 
             << ", and " << r.height << " has an area of " << r.calculateArea() 
             << " and a volume of " << r.calculateVolume << endl;
    }