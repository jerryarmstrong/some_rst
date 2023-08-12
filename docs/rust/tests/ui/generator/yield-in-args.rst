tests/ui/generator/yield-in-args.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]

fn foo(_b: &bool, _a: ()) {}

fn main() {
    || {
        let b = true;
        foo(&b, yield); //~ ERROR
    };
}


