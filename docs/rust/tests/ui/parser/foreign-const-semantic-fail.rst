tests/ui/parser/foreign-const-semantic-fail.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

extern "C" {
    const A: isize;
    //~^ ERROR extern items cannot be `const`
    const B: isize = 42;
    //~^ ERROR extern items cannot be `const`
    //~| ERROR incorrect `static` inside `extern` block
}


