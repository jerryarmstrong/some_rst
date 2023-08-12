tests/ui/operator-recovery/less-than-greater-than.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!("{}", 1 <> 2);
    //~^ERROR invalid comparison operator `<>`
}


