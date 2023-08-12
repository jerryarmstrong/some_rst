tests/ui/deriving/derive-partialord-correctness.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Original issue: #49650

#[derive(PartialOrd, PartialEq)]
struct FloatWrapper(f64);

fn main() {
    assert!((0.0 / 0.0 >= 0.0) == (FloatWrapper(0.0 / 0.0) >= FloatWrapper(0.0)))
}


