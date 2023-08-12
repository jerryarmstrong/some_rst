tests/ui/parser/diff-markers/item-with-attr.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[attribute]
<<<<<<< HEAD //~ ERROR encountered diff marker
fn foo() {}
=======
fn bar() {}
>>>>>>> branch

fn main() {
    foo();
}


