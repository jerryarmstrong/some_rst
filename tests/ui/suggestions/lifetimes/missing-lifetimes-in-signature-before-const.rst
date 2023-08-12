tests/ui/suggestions/lifetimes/missing-lifetimes-in-signature-before-const.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// https://github.com/rust-lang/rust/issues/95616

fn buggy_const<const N: usize>(_a: &Option<[u8; N]>, _f: &str) -> &str { //~ERROR [E0106]
    return "";
}

fn main() {
    buggy_const(&Some([69,69,69,69,0]), "test");
}


