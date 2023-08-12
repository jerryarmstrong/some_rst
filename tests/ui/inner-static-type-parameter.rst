tests/ui/inner-static-type-parameter.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // see #9186

enum Bar<T> { What } //~ ERROR parameter `T` is never used

fn foo<T>() {
    static a: Bar<T> = Bar::What;
//~^ ERROR can't use generic parameters from outer function
}

fn main() {
}


