tests/ui/rfc-2091-track-caller/error-with-start.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(start)]

#[start]
#[track_caller] //~ ERROR `start` is not allowed to be `#[track_caller]`
fn start(_argc: isize, _argv: *const *const u8) -> isize {
    panic!("{}: oh no", std::panic::Location::caller());
}


