tests/ui/block-result/block-must-not-have-result-res.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct R;

impl Drop for R {
    fn drop(&mut self) {
        true //~  ERROR mismatched types
    }
}

fn main() {
}


