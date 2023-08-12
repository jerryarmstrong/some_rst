tests/ui/lambda-infer-unresolved.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_mut)]
// This should typecheck even though the type of e is not fully
// resolved when we finish typechecking the ||.


struct Refs { refs: Vec<isize> , n: isize }

pub fn main() {
    let mut e = Refs{refs: vec![], n: 0};
    let _f = || println!("{}", e.n);
    let x: &[isize] = &e.refs;
    assert_eq!(x.len(), 0);
}


