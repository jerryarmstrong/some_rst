tests/ui/imports/import-in-block.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main() {
    use std::mem::replace;
    let mut x = 5;
    let _ = replace(&mut x, 6);
    {
        use std::mem::*;
        let mut y = 6;
        swap(&mut x, &mut y);
    }
}


