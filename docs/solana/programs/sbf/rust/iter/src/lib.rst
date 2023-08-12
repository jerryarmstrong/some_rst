programs/sbf/rust/iter/src/lib.rs
=================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! Example Rust-based SBF program tests loop iteration

#![allow(clippy::integer_arithmetic)]

extern crate solana_program;
use solana_program::{
    custom_heap_default, custom_panic_default, entrypoint::SUCCESS, log::sol_log_64,
};

#[no_mangle]
pub extern "C" fn entrypoint(_input: *mut u8) -> u64 {
    const ITERS: usize = 100;
    let ones = [1_u64; ITERS];
    let mut sum: u64 = 0;

    for v in ones.iter() {
        sum += *v;
    }
    sol_log_64(0xff, 0, 0, 0, sum);
    assert_eq!(sum, ITERS as u64);

    SUCCESS
}

custom_heap_default!();
custom_panic_default!();

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_entrypoint() {
        assert_eq!(SUCCESS, entrypoint(std::ptr::null_mut()));
    }
}


