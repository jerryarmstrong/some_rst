tests/ui/array-slice-vec/mutability-inherits-through-fixed-length-vec.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


fn test1() {
    let mut ints = [0; 32];
    ints[0] += 1;
    assert_eq!(ints[0], 1);
}

fn test2() {
    let mut ints = [0; 32];
    for i in &mut ints { *i += 22; }
    for i in &ints { assert_eq!(*i, 22); }
}

pub fn main() {
    test1();
    test2();
}


