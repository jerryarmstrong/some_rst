tests/ui/try-block/try-block-unused-delims.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: --edition 2018
// run-rustfix

#![feature(try_blocks)]
#![warn(unused_parens, unused_braces)]

fn consume<T>(_: Result<T, T>) -> T { todo!() }

fn main() {
    consume((try {}));
    //~^ WARN unnecessary parentheses

    consume({ try {} });
    //~^ WARN unnecessary braces

    match (try {}) {
        //~^ WARN unnecessary parentheses
        Ok(()) | Err(()) => (),
    }

    if let Err(()) = (try {}) {}
    //~^ WARN unnecessary parentheses

    match (try {}) {
        //~^ WARN unnecessary parentheses
        Ok(()) | Err(()) => (),
    }
}


