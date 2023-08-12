tests/ui/array-slice-vec/vec-macro-with-brackets.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]

// pretty-expanded FIXME #23616

macro_rules! vec [
    ($($e:expr),*) => ({
        let mut _temp = ::std::vec::Vec::new();
        $(_temp.push($e);)*
        _temp
    })
];

pub fn main() {
    let my_vec = vec![1, 2, 3, 4, 5];
}


