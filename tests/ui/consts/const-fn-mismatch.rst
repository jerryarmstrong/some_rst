tests/ui/consts/const-fn-mismatch.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we can't declare a const fn in an impl -- right now it's
// just not allowed at all, though eventually it'd make sense to allow
// it if the trait fn is const (but right now no trait fns can be
// const).

trait Foo {
    fn f() -> u32;
}

impl Foo for u32 {
    const fn f() -> u32 {
        //~^ ERROR functions in traits cannot be declared const
        22
    }
}

fn main() {}


