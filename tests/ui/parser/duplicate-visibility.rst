tests/ui/parser/duplicate-visibility.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

extern "C" { //~ NOTE while parsing this item list starting here
    pub pub fn foo();
    //~^ ERROR expected one of `(`, `async`, `const`, `default`, `extern`, `fn`, `unsafe`, or `use`, found keyword `pub`
    //~| NOTE expected one of 8 possible tokens
    //~| HELP there is already a visibility modifier, remove one
    //~| NOTE explicit visibility first seen here
} //~ NOTE the item list ends here


