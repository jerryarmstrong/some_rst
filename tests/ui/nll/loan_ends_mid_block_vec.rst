tests/ui/nll/loan_ends_mid_block_vec.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]
#![feature(rustc_attrs)]

fn main() {
}

fn nll_fail() {
    let mut data = vec!['a', 'b', 'c'];
    let slice = &mut data;
    capitalize(slice);
    data.push('d');
    //~^ ERROR [E0499]
    data.push('e');
    //~^ ERROR [E0499]
    data.push('f');
    //~^ ERROR [E0499]
    capitalize(slice);
}

fn nll_ok() {
    let mut data = vec!['a', 'b', 'c'];
    let slice = &mut data;
    capitalize(slice);
    data.push('d');
    data.push('e');
    data.push('f');
}

fn capitalize(_: &mut [char]) {
}


