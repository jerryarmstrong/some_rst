tests/ui/as-precedence.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[allow(unused_parens)]
fn main() {
    assert_eq!(3 as usize * 3, 9);
    assert_eq!(3 as (usize) * 3, 9);
    assert_eq!(3 as (usize) / 3, 1);
    assert_eq!(3 as usize + 3, 6);
    assert_eq!(3 as (usize) + 3, 6);
}


