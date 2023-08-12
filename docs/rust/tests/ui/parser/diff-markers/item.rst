tests/ui/parser/diff-markers/item.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    <<<<<<< HEAD //~ ERROR encountered diff marker
fn foo() {}
=======
fn bar() {}
>>>>>>> branch

fn main() {
    foo();
}


