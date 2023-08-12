tests/ui/sepcomp/auxiliary/sepcomp_lib.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C codegen-units=3 --crate-type=rlib,dylib -g

pub mod a {
    pub fn one() -> usize {
        1
    }
}

pub mod b {
    pub fn two() -> usize {
        2
    }
}

pub mod c {
    use a::one;
    use b::two;
    pub fn three() -> usize {
        one() + two()
    }
}


