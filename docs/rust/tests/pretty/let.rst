tests/pretty/let.rs
===================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact

// Check that `let x: _ = 0;` does not print as `let x = 0;`.

fn main() {
    let x: _ = 0;

    let _ = x;
}


