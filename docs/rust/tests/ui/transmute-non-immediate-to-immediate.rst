tests/ui/transmute-non-immediate-to-immediate.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Issue #7988
// Transmuting non-immediate type to immediate type

// pretty-expanded FIXME #23616

pub fn main() {
    unsafe {
        ::std::mem::transmute::<[isize; 1],isize>([1])
    };
}


