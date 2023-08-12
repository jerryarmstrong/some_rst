tests/ui/impl-trait/universal_hrtb_anon.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn hrtb(f: impl Fn(&u32) -> u32) -> u32 {
    f(&22) + f(&44)
}

fn main() {
    let sum = hrtb(|x| x * 2);
    assert_eq!(sum, 22*2 + 44*2);
}


