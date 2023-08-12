tests/ui/impl-trait/universal_hrtb_named.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn hrtb(f: impl for<'a> Fn(&'a u32) -> &'a u32) -> u32 {
    f(&22) + f(&44)
}

fn main() {
    let sum = hrtb(|x| x);
    assert_eq!(sum, 22 + 44);
}


