tests/ui/consts/const-tuple-struct.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Bar(isize, isize);

static X: Bar = Bar(1, 2);

pub fn main() {
    match X {
        Bar(x, y) => {
            assert_eq!(x, 1);
            assert_eq!(y, 2);
        }
    }
}


