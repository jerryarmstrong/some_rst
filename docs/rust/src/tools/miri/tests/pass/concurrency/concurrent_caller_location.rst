src/tools/miri/tests/pass/concurrency/concurrent_caller_location.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::panic::Location;
use std::thread::spawn;

fn initialize() {
    let _ignore = initialize_inner();
}

fn initialize_inner() -> &'static Location<'static> {
    Location::caller()
}

fn main() {
    let j1 = spawn(initialize);
    let j2 = spawn(initialize);
    j1.join().unwrap();
    j2.join().unwrap();
}


