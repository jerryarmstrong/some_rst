tests/ui/cfg/crt-static-on-works.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:-C target-feature=+crt-static
// only-msvc

#[cfg(target_feature = "crt-static")]
fn main() {}


