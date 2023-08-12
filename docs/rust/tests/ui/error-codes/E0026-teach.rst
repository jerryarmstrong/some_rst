tests/ui/error-codes/E0026-teach.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z teach

struct Thing {
    x: u32,
    y: u32
}

fn main() {
    let thing = Thing { x: 0, y: 0 };
    match thing {
        Thing { x, y, z } => {}
        //~^ ERROR struct `Thing` does not have a field named `z` [E0026]
    }
}


