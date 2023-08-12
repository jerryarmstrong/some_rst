tests/ui/consts/const-vecs-and-slices.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_upper_case_globals)]

static x : [isize; 4] = [1,2,3,4];
static y : &'static [isize] = &[1,2,3,4];
static z : &'static [isize; 4] = &[1,2,3,4];
static zz : &'static [isize] = &[1,2,3,4];

pub fn main() {
    println!("{}", x[1]);
    println!("{}", y[1]);
    println!("{}", z[1]);
    println!("{}", zz[1]);
    assert_eq!(x[1], 2);
    assert_eq!(x[3], 4);
    assert_eq!(x[3], y[3]);
    assert_eq!(z[1], 2);
    assert_eq!(z[3], 4);
    assert_eq!(z[3], y[3]);
    assert_eq!(zz[1], 2);
    assert_eq!(zz[3], 4);
    assert_eq!(zz[3], y[3]);
}


