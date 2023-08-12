tests/ui/rfc-1937-termination-trait/termination-trait-main-i32.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() -> i32 {
//~^ ERROR `main` has invalid return type `i32`
//~| NOTE `main` can only return types that implement `Termination`
//~| HELP consider using `()`, or a `Result`
    0
}


