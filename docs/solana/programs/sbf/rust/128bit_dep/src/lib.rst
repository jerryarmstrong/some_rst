programs/sbf/rust/128bit_dep/src/lib.rs
=======================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! Solana Rust-based SBF program utility functions and types

#![allow(clippy::integer_arithmetic)]

extern crate solana_program;

pub fn uadd(x: u128, y: u128) -> u128 {
    x + y
}
pub fn usubtract(x: u128, y: u128) -> u128 {
    x - y
}
pub fn umultiply(x: u128, y: u128) -> u128 {
    x * y
}
pub fn udivide(n: u128, d: u128) -> u128 {
    n / d
}
pub fn umodulo(n: u128, d: u128) -> u128 {
    n % d
}

pub fn add(x: i128, y: i128) -> i128 {
    x + y
}
pub fn subtract(x: i128, y: i128) -> i128 {
    x - y
}
pub fn multiply(x: i128, y: i128) -> i128 {
    x * y
}
pub fn divide(n: i128, d: i128) -> i128 {
    n / d
}
pub fn modulo(n: i128, d: i128) -> i128 {
    n % d
}


