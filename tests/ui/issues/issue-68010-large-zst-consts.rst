tests/ui/issues/issue-68010-large-zst-consts.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass

fn main() {
    println!("{}", [(); usize::MAX].len());
}


