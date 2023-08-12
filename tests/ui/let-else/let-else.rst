tests/ui/let-else/let-else.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    let Some(x) = Some(1) else {
        return;
    };
    assert_eq!(x, 1);
}


