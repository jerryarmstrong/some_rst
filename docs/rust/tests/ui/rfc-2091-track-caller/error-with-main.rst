tests/ui/rfc-2091-track-caller/error-with-main.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[track_caller] //~ ERROR `main` function is not allowed to be
fn main() {
    panic!("{}: oh no", std::panic::Location::caller());
}


