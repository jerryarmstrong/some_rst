tests/ui/typeck/issue-57673-ice-on-deref-of-boxed-trait.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //extern crate has_assoc_type;

//fn ice(x: Box<dyn has_assoc_type::Foo<Assoc=()>>) {
fn ice(x: Box<dyn Iterator<Item=()>>) {
    *x //~ ERROR mismatched types [E0308]
}
fn main() {}


