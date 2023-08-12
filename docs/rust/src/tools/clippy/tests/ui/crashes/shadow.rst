src/tools/clippy/tests/ui/crashes/shadow.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: [i32; {
        let u = 2;
        4
    }] = [2; { 4 }];
}


