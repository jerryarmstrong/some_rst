src/tools/rustfmt/tests/source/catch.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-edition: 2018
#![feature(try_blocks)]

fn main() {
    let x = try {
        foo()?
    };

    let x = try /* Invisible comment */ { foo()? };

    let x = try {
        unsafe { foo()? }
    };

    let y = match (try {
        foo()?
    }) {
        _ => (),
    };

    try {
        foo()?;
    };

    try {
        // Regular try block
    };
}


