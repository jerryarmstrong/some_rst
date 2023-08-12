src/etc/test-float-parse/src/bin/few-ones.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use test_float_parse::validate;

fn main() {
    let mut pow = vec![];
    for i in 0..63 {
        pow.push(1u64 << i);
    }
    for a in &pow {
        for b in &pow {
            for c in &pow {
                validate(&(a | b | c).to_string());
            }
        }
    }
}


