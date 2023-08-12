tests/ui/issues/issue-3214.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T>() {
    struct Foo {
        x: T, //~ ERROR can't use generic parameters from outer function
    }

    impl<T> Drop for Foo<T> {
        //~^ ERROR this struct takes 0 generic arguments but 1 generic argument
        fn drop(&mut self) {}
    }
}
fn main() {}


