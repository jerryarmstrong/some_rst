tests/ui/generics/issue-80512-param-reordering-with-defaults.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

struct S<T = (), 'a>(&'a T);
//~^ ERROR lifetime parameters must be declared prior to type and const parameters


