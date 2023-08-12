tests/ui/lint/dead-code/closure-bang.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-test FIXME(#20574)

#![deny(unreachable_code)]

fn main() {
    let x = || panic!();
    x();
    println!("Foo bar"); //~ ERROR: unreachable statement
}


