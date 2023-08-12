src/tools/clippy/tests/ui/crashes/implements-trait.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(clippy::needless_borrowed_reference)]
fn main() {
    let mut v = Vec::<String>::new();
    let _ = v.iter_mut().filter(|&ref a| a.is_empty());
}


