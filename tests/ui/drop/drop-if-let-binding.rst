tests/ui/drop/drop-if-let-binding.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// regression test for issue #88307
// compile-flags: -C opt-level=s

fn main() {
    if let Some(_val) = Option::<String>::None {}
}


