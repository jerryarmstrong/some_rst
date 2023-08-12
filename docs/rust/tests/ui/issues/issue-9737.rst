tests/ui/issues/issue-9737.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
macro_rules! f {
    (v: $x:expr) => ( println!("{}", $x) )
}

fn main () {
    let v = 5;
    f!(v: 3);
}


