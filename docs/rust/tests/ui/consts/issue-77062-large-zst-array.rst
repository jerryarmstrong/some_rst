tests/ui/consts/issue-77062-large-zst-array.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass

fn main() {
    let _ = &[(); usize::MAX];
}


