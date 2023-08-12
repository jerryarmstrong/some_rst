tests/ui/parser/lifetime-in-pattern-recover.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let &'a x = &0; //~ ERROR unexpected lifetime `'a` in pattern
    let &'a mut y = &mut 0; //~ ERROR unexpected lifetime `'a` in pattern

    let _recovery_witness: () = 0; //~ ERROR mismatched types
}


