tests/ui/parser/diff-markers/fn-arg.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T {
    fn foo(
<<<<<<< HEAD //~ ERROR encountered diff marker
        x: u8,
=======
        x: i8,
>>>>>>> branch
    ) {}
}

struct S;
impl T for S {}

fn main() {
    S::foo(42);
}


