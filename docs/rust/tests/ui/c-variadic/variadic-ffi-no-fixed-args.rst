tests/ui/c-variadic/variadic-ffi-no-fixed-args.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    fn foo(...);
//~^ ERROR C-variadic function must be declared with at least one named argument
}

fn main() {}


