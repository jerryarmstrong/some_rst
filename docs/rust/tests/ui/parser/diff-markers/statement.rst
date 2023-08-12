tests/ui/parser/diff-markers/statement.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T {
    fn foo() {}
    fn bar() {}
}

struct S;
impl T for S {}

fn main() {
<<<<<<< HEAD //~ ERROR encountered diff marker
    S::foo();
=======
    S::bar();
>>>>>>> branch
}


