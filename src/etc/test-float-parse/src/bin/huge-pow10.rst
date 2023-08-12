src/etc/test-float-parse/src/bin/huge-pow10.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use test_float_parse::validate;

fn main() {
    for e in 300..310 {
        for i in 0..100000 {
            validate(&format!("{}e{}", i, e));
        }
    }
}


