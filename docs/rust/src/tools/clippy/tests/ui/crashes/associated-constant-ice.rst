src/tools/clippy/tests/ui/crashes/associated-constant-ice.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// Test for https://github.com/rust-lang/rust-clippy/issues/1698

pub trait Trait {
    const CONSTANT: u8;
}

impl Trait for u8 {
    const CONSTANT: u8 = 2;
}

fn main() {
    println!("{}", u8::CONSTANT * 10);
}


