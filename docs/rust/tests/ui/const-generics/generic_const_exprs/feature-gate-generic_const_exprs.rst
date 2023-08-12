tests/ui/const-generics/generic_const_exprs/feature-gate-generic_const_exprs.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type Arr<const N: usize> = [u8; N - 1];
//~^ ERROR generic parameters may not be used in const operations

fn test<const N: usize>() -> Arr<N> where Arr<N>: Default {
    Default::default()
}

fn main() {
    let x = test::<33>();
    assert_eq!(x, [0; 32]);
}


