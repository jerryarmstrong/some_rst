tests/ui/binding/fn-pattern-expected-type-2.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    let v : &[(isize,isize)] = &[ (1, 2), (3, 4), (5, 6) ];
    for &(x, y) in v {
        println!("{}", y);
        println!("{}", x);
    }
}


