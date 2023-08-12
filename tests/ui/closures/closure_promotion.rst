tests/ui/closures/closure_promotion.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

fn main() {
    let x: &'static _ = &|| { let z = 3; z };
}


