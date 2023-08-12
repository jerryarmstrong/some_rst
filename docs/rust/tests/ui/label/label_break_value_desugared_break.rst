tests/ui/label/label_break_value_desugared_break.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition 2018
#![feature(try_blocks)]

// run-pass
fn main() {
    let _: Result<(), ()> = try {
        'foo: {
            Err(())?;
            break 'foo;
        }
    };

    'foo: {
        let _: Result<(), ()> = try {
            Err(())?;
            break 'foo;
        };
    }
}


