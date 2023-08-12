tests/ui/custom_attribute.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(stmt_expr_attributes)]

#[foo] //~ ERROR cannot find attribute `foo` in this scope
fn main() {
    #[foo] //~ ERROR cannot find attribute `foo` in this scope
    let x = ();
    #[foo] //~ ERROR cannot find attribute `foo` in this scope
    x
}


