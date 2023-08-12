tests/ui/self/self-infer.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S;

impl S {
    fn f(self: _) {} //~ERROR the placeholder `_` is not allowed within types on item signatures for functions
    fn g(self: &_) {} //~ERROR the placeholder `_` is not allowed within types on item signatures for functions
}

fn main() {}


