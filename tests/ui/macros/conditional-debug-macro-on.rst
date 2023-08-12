tests/ui/macros/conditional-debug-macro-on.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    // exits early if println! evaluates its arguments, otherwise it
    // will hit the panic.
    println!("{:?}", { if true { return; } });

    panic!();
}


