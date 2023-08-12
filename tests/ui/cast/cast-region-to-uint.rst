tests/ui/cast/cast-region-to-uint.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x: isize = 3;
    println!("&x={:x}", (&x as *const isize as usize));
}


