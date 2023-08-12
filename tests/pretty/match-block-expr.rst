tests/pretty/match-block-expr.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact

fn main() {
    let x = match { 5 } { 1 => 5, 2 => 6, _ => 7, };
    assert_eq!(x, 7);
}


