tests/ui/consts/const_prop_slice_pat_ice.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    match &[0, 1] as &[i32] {
        [a @ .., x] => {}
        &[] => {}
    }
}


