tests/ui/impl-trait/explicit-generic-args-with-impl-trait/not-enough-args.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f<T: ?Sized, U: ?Sized>(_: impl AsRef<T>, _: impl AsRef<U>) {}

fn main() {
    f::<[u8]>("a", b"a");
    //~^ ERROR function takes 2 generic arguments but 1 generic argument was supplied
}


