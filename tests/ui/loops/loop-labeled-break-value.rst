tests/ui/loops/loop-labeled-break-value.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    loop {
        let _: i32 = loop { break }; //~ ERROR mismatched types
    }
    loop {
        let _: i32 = 'inner: loop { break 'inner }; //~ ERROR mismatched types
    }
    loop {
        let _: i32 = 'inner2: loop { loop { break 'inner2 } }; //~ ERROR mismatched types
    }
}


