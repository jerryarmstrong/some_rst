tests/ui/argument-suggestions/display-is-suggestable.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Display;

fn foo(x: &(dyn Display + Send)) {}

fn main() {
    foo();
    //~^ ERROR function takes 1 argument but 0 arguments were supplied
}


