src/tools/clippy/tests/ui-toml/max_suggested_slice_pattern_length/index_refutable_slice.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::index_refutable_slice)]

fn below_limit() {
    let slice: Option<&[u32]> = Some(&[1, 2, 3]);
    if let Some(slice) = slice {
        // This would usually not be linted but is included now due to the
        // index limit in the config file
        println!("{}", slice[7]);
    }
}

fn above_limit() {
    let slice: Option<&[u32]> = Some(&[1, 2, 3]);
    if let Some(slice) = slice {
        // This will not be linted as 8 is above the limit
        println!("{}", slice[8]);
    }
}

fn main() {
    below_limit();
    above_limit();
}


