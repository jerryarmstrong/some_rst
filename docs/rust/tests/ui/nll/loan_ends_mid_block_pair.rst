tests/ui/nll/loan_ends_mid_block_pair.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]
#![feature(rustc_attrs)]


fn main() {
}

fn nll_fail() {
    let mut data = ('a', 'b', 'c');
    let c = &mut data.0;
    capitalize(c);
    data.0 = 'e';
    //~^ ERROR [E0506]
    data.0 = 'f';
    data.0 = 'g';
    capitalize(c);
}

fn nll_ok() {
    let mut data = ('a', 'b', 'c');
    let c = &mut data.0;
    capitalize(c);
    data.0 = 'e';
    data.0 = 'f';
    data.0 = 'g';
}

fn capitalize(_: &mut char) {
}


