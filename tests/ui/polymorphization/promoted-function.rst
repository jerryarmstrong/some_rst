tests/ui/polymorphization/promoted-function.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:-Zpolymorphize=on

fn fop<T>() {}

fn bar<T>() -> &'static fn() {
    &(fop::<T> as fn())
}
pub const FN: &'static fn() = &(fop::<i32> as fn());

fn main() {
    bar::<u32>();
    bar::<i32>();
    (FN)();
}


