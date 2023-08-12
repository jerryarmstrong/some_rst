tests/ui/span/gated-features-attr-spans.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(simd)] //~ ERROR are experimental
struct Coord {
    x: u32,
    y: u32,
}

fn main() {}


