tests/ui/rfc-2361-dbg-macro/dbg-macro-requires-debug.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test ensuring that `dbg!(expr)` requires the passed type to implement `Debug`.

struct NotDebug;

fn main() {
    let _: NotDebug = dbg!(NotDebug); //~ ERROR `NotDebug` doesn't implement `Debug`
}


