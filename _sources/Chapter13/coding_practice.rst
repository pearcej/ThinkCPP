Coding Practice
---------------

.. tabbed:: cp_13_1

    .. tab:: Question

        A pixel is the smallest controllable element of a picture represented on the screen. Images
        are comprised of numerous individual pixels, and each pixel's color sample has three numerical
        RGB (red, green, blue) components to represent the color of that pixel. The intensity value of 
        each RGB component ranges from 0 to 255, where 0 is no intensity and 255 is highest intensity.
        Write the ``struct`` definition for ``Pixel``, which has values for each component r, g, and b.

        .. activecode:: cp_13_AC_1q
           :language: cpp
           :practice: T

           #include <iostream>
           #include <vector>
           using namespace std;

           // Write your code for the struct Pixel here.

    .. tab:: Answer

        Below is one way to implement the program. We declare the ``Pixel`` struct
        and create the instance variables in order.

        .. activecode:: cp_13_AC_1a
           :language: cpp
           :optional:

           #include <iostream>
           #include <vector>
           using namespace std;

           struct Pixel {
               int r;
               int g;
               int b;
           };

.. activecode:: cp_13_AC_2q
    :language: cpp

    An image is just a matrix of pixels. Write the ``struct`` definition for ``Image``,
    which should store information about its height and width and contain a matrix 
    of ``Pixel``\s.
    ~~~~
    #include <iostream>
    #include <vector>
    using namespace std;

    struct Pixel {
        int r;
        int g;
        int b;
    };

    // Write your code for the struct Image here.