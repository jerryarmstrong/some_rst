tests/ui/fmt/send-sync.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn send<T: Send>(_: T) {}
fn sync<T: Sync>(_: T) {}

fn main() {
    // `Cell` is not `Sync`, so `&Cell` is neither `Sync` nor `Send`,
    // `std::fmt::Arguments` used to forget this...
    let c = std::cell::Cell::new(42);
    send(format_args!("{:?}", c)); //~ ERROR E0277
    sync(format_args!("{:?}", c)); //~ ERROR E0277
}


