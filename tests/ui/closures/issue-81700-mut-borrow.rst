tests/ui/closures/issue-81700-mut-borrow.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x: &mut u32) {
    let bar = || { foo(x); };
    bar(); //~ ERROR cannot borrow
}
fn main() {}


