tests/ui/rfc-2497-if-let-chains/ast-lowering-does-not-wrap-let-chains.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(let_chains)]
#![allow(irrefutable_let_patterns)]

fn main() {
    let first = Some(1);
    let second = Some(2);
    let mut n = 0;
    if let x = first && let y = second && 1 == 1 {
        assert_eq!(x, first);
        assert_eq!(y, second);
        n = 1;
    }
    assert_eq!(n, 1);
}


