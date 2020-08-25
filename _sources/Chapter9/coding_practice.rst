Coding Practice
---------------

.. tabbed:: cp_9_1

    .. tab:: Question

        Write the function ``rectangleInfo`` which prompts the user for the width
        and height of a rectangle. Then ``rectangleInfo`` prints out the area and 
        perimeter of the rectangle.

        .. activecode:: cp_9_AC_1q
           :language: cpp
           :practice: T
           :stdin: 4, 6

           #include <iostream>
           using namespace std;

           void rectangleInfo () {
               // Write your implementation here.
           }

           int main() {
               rectangleInfo ();
           }


    .. tab:: Answer

        Below is one way to implement the program. We prompt the user for input
        using ``cin`` before printing the area and perimeter.

        .. activecode:: cp_9_AC_1a
           :language: cpp
           :optional:

           #include <iostream>
           using namespace std;

           void rectangleInfo () {
               int height, width;
               cout << "Please enter the height and width of a rectangle separated by spaces: ";
               cin >> height >> width;
               cout << "The area of the rectangle is " << height * width << endl;
               cout << "The perimeter of the rectangle is " << 2 * (height + width) << endl;
           }

           int main() {
               rectangleInfo ();
           }

.. activecode:: cp_9_AC_2q
    :language: cpp
    :stdin: Captain America

    Write a simple function called ``greetUser`` which prompts the user 
    for their full name. Then the function outputs "Hello ``fullName``!".
    ~~~~
    #include <iostream>
    using namespace std;

    void greetUser () {
        // Write your implementation here.
    }

    int main() {
        greetUser ();
    }