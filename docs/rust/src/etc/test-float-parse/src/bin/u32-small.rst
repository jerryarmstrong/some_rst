src/etc/test-float-parse/src/bin/u32-small.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use test_float_parse::validate;

fn main() {
    for i in 0..(1 << 19) {
        validate(&i.to_string());
    }
}


