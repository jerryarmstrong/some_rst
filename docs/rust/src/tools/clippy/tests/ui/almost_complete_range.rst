src/tools/clippy/tests/ui/almost_complete_range.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// edition:2018
// aux-build:macro_rules.rs

#![feature(exclusive_range_pattern)]
#![feature(stmt_expr_attributes)]
#![warn(clippy::almost_complete_range)]
#![allow(ellipsis_inclusive_range_patterns)]
#![allow(clippy::needless_parens_on_range_literals)]
#![allow(clippy::double_parens)]

#[macro_use]
extern crate macro_rules;

macro_rules! a {
    () => {
        'a'
    };
}
macro_rules! A {
    () => {
        'A'
    };
}
macro_rules! zero {
    () => {
        '0'
    };
}

macro_rules! b {
    () => {
        let _ = 'a'..'z';
        let _ = 'A'..'Z';
        let _ = '0'..'9';
    };
}

fn main() {
    #[rustfmt::skip]
    {
        let _ = ('a') ..'z';
        let _ = 'A' .. ('Z');
        let _ = ((('0'))) .. ('9');
    }

    let _ = 'b'..'z';
    let _ = 'B'..'Z';
    let _ = '1'..'9';

    let _ = (b'a')..(b'z');
    let _ = b'A'..b'Z';
    let _ = b'0'..b'9';

    let _ = b'b'..b'z';
    let _ = b'B'..b'Z';
    let _ = b'1'..b'9';

    let _ = a!()..'z';
    let _ = A!()..'Z';
    let _ = zero!()..'9';

    let _ = match 0u8 {
        b'a'..b'z' if true => 1,
        b'A'..b'Z' if true => 2,
        b'0'..b'9' if true => 3,
        b'b'..b'z' => 4,
        b'B'..b'Z' => 5,
        b'1'..b'9' => 6,
        _ => 7,
    };

    let _ = match 'x' {
        'a'..'z' if true => 1,
        'A'..'Z' if true => 2,
        '0'..'9' if true => 3,
        'b'..'z' => 4,
        'B'..'Z' => 5,
        '1'..'9' => 6,
        _ => 7,
    };

    almost_complete_range!();
    b!();
}

#[clippy::msrv = "1.25"]
fn _under_msrv() {
    let _ = match 'a' {
        'a'..'z' => 1,
        'A'..'Z' => 2,
        '0'..'9' => 3,
        _ => 4,
    };
}

#[clippy::msrv = "1.26"]
fn _meets_msrv() {
    let _ = 'a'..'z';
    let _ = 'A'..'Z';
    let _ = '0'..'9';
    let _ = match 'a' {
        'a'..'z' => 1,
        'A'..'Z' => 1,
        '0'..'9' => 3,
        _ => 4,
    };
}


