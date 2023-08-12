tests/ui/cross-crate/auxiliary/moves_based_on_type_lib.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]

pub struct S {
    x: isize,
}

impl Drop for S {
    fn drop(&mut self) {
        println!("goodbye");
    }
}

pub fn f() {
    let x = S { x: 1 };
    let y = x;
    let _z = y;
}


