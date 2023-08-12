tests/ui/issues/issue-8391.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    let x = match Some(1) {
        ref _y @ Some(_) => 1,
        None => 2,
    };
    assert_eq!(x, 1);
}


