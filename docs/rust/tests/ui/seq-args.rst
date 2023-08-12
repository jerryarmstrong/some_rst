tests/ui/seq-args.rs
====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    trait Seq { }

    impl<T> Seq<T> for Vec<T> {
        //~^ ERROR this trait takes 0 generic arguments but 1 generic argument
        /* ... */
    }

    impl Seq<bool> for u32 {
        //~^ ERROR this trait takes 0 generic arguments but 1 generic argument
        /* Treat the integer as a sequence of bits */
    }
}


