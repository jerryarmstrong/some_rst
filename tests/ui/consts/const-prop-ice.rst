tests/ui/consts/const-prop-ice.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

fn main() {
    [0; 3][3u64 as usize]; //~ ERROR this operation will panic at runtime
}


