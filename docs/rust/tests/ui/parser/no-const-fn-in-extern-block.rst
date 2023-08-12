tests/ui/parser/no-const-fn-in-extern-block.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    const fn foo();
    //~^ ERROR functions in `extern` blocks cannot have qualifiers
    const unsafe fn bar();
    //~^ ERROR functions in `extern` blocks cannot have qualifiers
}

fn main() {}


