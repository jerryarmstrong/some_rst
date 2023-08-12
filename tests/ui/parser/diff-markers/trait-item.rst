tests/ui/parser/diff-markers/trait-item.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T {
<<<<<<< HEAD //~ ERROR encountered diff marker
    fn foo() {}
=======
    fn bar() {}
>>>>>>> branch
}

struct S;
impl T for S {}

fn main() {
    S::foo();
}


