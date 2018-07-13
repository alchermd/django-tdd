# Chapter 3 - Testing a Simple Home Page with Unit Tests

- _Django_ encourages us to structure our code into _apps_. The idea is that an _app_ can be used in several _projects_, allowing code reusability.
- _Unit Tests_ test the application from the point of view of the programmer.

An example workflow

1.  Write functional tests (fails).
2.  Write unit tests (which also fails) for the code that will make the FTs pass.
3.  Write the smallest amount of application code to make the unit tests pass.
4.  Once the unit tests pass, run the functional tests again.
