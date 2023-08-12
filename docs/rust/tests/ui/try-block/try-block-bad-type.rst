tests/ui/try-block/try-block-bad-type.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition 2018

#![feature(try_blocks)]

pub fn main() {
    let res: Result<u32, std::array::TryFromSliceError> = try {
        Err("")?; //~ ERROR `?` couldn't convert the error
        5
    };

    let res: Result<i32, i32> = try {
        "" //~ ERROR type mismatch
    };

    let res: Result<i32, i32> = try { }; //~ ERROR type mismatch

    let res: () = try { };
    //~^ ERROR a `try` block must return `Result` or `Option`

    let res: i32 = try { 5 }; //~ ERROR a `try` block must return `Result` or `Option`
}


