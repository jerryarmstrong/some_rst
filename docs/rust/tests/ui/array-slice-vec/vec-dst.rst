tests/ui/array-slice-vec/vec-dst.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    // Tests for indexing into Box<[T; n]>/& [T; n]
    let x: [isize; 3] = [1, 2, 3];
    let mut x: Box<[isize; 3]> = x.into();
    assert_eq!(x[0], 1);
    assert_eq!(x[1], 2);
    assert_eq!(x[2], 3);
    x[1] = 45;
    assert_eq!(x[0], 1);
    assert_eq!(x[1], 45);
    assert_eq!(x[2], 3);

    let mut x: [isize; 3] = [1, 2, 3];
    let x: &mut [isize; 3] = &mut x;
    assert_eq!(x[0], 1);
    assert_eq!(x[1], 2);
    assert_eq!(x[2], 3);
    x[1] = 45;
    assert_eq!(x[0], 1);
    assert_eq!(x[1], 45);
    assert_eq!(x[2], 3);
}


