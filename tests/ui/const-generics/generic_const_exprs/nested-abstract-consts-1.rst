tests/ui/const-generics/generic_const_exprs/nested-abstract-consts-1.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

fn callee<const M2: usize>() -> usize
where
    [u8; M2 + 1]: Sized,
{
    M2
}

fn caller<const N1: usize>() -> usize
where
    [u8; N1 + 1]: Sized,
    [u8; (N1 + 1) + 1]: Sized,
{
    callee::<{ N1 + 1 }>()
}

fn main() {
    assert_eq!(caller::<4>(), 5);
}

// Test that the ``(N1 + 1) + 1`` bound on ``caller`` satisfies the ``M2 + 1`` bound on ``callee``


