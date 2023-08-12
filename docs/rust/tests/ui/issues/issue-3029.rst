tests/ui/issues/issue-3029.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:so long
// ignore-emscripten no processes

#![allow(unused_allocation)]
#![allow(unreachable_code)]
#![allow(unused_variables)]

fn main() {
    let mut x = Vec::new();
    let y = vec![3];
    panic!("so long");
    x.extend(y.into_iter());
}


