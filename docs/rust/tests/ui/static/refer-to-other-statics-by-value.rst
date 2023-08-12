tests/ui/static/refer-to-other-statics-by-value.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

static A: usize = 42;
static B: usize = A;

fn main() {
    assert_eq!(B, 42);
}


