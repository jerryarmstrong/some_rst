tests/ui/regions/regions-params.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_parens)]


fn region_identity(x: &usize) -> &usize { x }

fn apply<T, F>(t: T, f: F) -> T where F: FnOnce(T) -> T { f(t) }

fn parameterized(x: &usize) -> usize {
    let z = apply(x, ({|y|
        region_identity(y)
    }));
    *z
}

pub fn main() {
    let x = 3;
    assert_eq!(parameterized(&x), 3);
}


