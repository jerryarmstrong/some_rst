tests/ui/unboxed-closures/unboxed-closures-infer-explicit-call-early.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(fn_traits)]

fn main() {
    let mut zero = || 0;
    let x = zero.call_mut(());
    assert_eq!(x, 0);
}


