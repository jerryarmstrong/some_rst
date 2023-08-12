tests/run-make-fulldeps/sepcomp-separate/foo.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn magic_fn() -> usize {
    1234
}

mod a {
    pub fn magic_fn() -> usize {
        2345
    }
}

mod b {
    pub fn magic_fn() -> usize {
        3456
    }
}

fn main() {
    magic_fn();
    a::magic_fn();
    b::magic_fn();
}


