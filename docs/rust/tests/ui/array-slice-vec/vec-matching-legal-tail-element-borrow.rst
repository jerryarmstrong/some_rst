tests/ui/array-slice-vec/vec-matching-legal-tail-element-borrow.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_variables)]

pub fn main() {
    let x = &[1, 2, 3, 4, 5];
    let x: &[isize] = &[1, 2, 3, 4, 5];
    if !x.is_empty() {
        let el = match x {
            &[1, ref tail @ ..] => &tail[0],
            _ => unreachable!()
        };
        println!("{}", *el);
    }
}


