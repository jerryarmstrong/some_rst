tests/ui/traits/no-fallback-multiple-impls.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Fallback {
    fn foo(&self) {}
}

impl Fallback for i32 {}

impl Fallback for u64 {}

impl Fallback for usize {}

fn main() {
    missing();
    //~^ ERROR cannot find function `missing` in this scope
    0.foo();
    // But then we shouldn't report an inference ambiguity here...
}


