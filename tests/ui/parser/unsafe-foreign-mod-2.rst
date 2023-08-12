tests/ui/parser/unsafe-foreign-mod-2.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" unsafe {
               //~^ ERROR expected `{`, found keyword `unsafe`
               //~| ERROR extern block cannot be declared unsafe
    unsafe fn foo();
        //~^ ERROR functions in `extern` blocks cannot have qualifiers
}

fn main() {}


