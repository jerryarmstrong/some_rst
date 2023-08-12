src/tools/rustfmt/tests/target/configs/short_array_element_width_threshold/greater_than_max_width.rs
====================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-max_width: 20
// rustfmt-short_array_element_width_threshold: 30

fn main() {
    pub const FORMAT_TEST: [u64; 5] = [
        0x0000000000000000,
        0xaaaaaaaaaaaaaaaa,
        0xbbbbbbbbbbbbbbbb,
        0xcccccccccccccccc,
        0xdddddddddddddddd,
    ];
}


