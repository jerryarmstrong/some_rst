tests/ui/issues/issue-9047.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)]
#![allow(unused_variables)]
fn decode() -> String {
    'outer: loop {
        let mut ch_start: usize;
        break 'outer;
    }
    "".to_string()
}

pub fn main() {
    println!("{}", decode());
}


