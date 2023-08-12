tests/ui/parser/nt-parsing-has-recovery.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo {
    ($e:expr) => {}
}

foo!(1 + @); //~ ERROR expected expression, found `@`
foo!(1 + @); //~ ERROR expected expression, found `@`

fn main() {
    let _recovery_witness: () = 0; //~ ERROR mismatched types
}


