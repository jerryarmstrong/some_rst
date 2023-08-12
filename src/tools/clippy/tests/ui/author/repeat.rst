src/tools/clippy/tests/ui/author/repeat.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(clippy::no_effect)]
fn main() {
    #[clippy::author]
    [1_u8; 5];
}


