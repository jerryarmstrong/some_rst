tests/ui/tuple/one-tuple.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Why one-tuples? Because macros.


pub fn main() {
    match ('c',) {
        (x,) => {
            assert_eq!(x, 'c');
        }
    }
    // test the 1-tuple type too
    let x: (char,) = ('d',);
    let (y,) = x;
    assert_eq!(y, 'd');
}


