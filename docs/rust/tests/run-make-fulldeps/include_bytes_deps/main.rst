tests/run-make-fulldeps/include_bytes_deps/main.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[doc = include_str!("input.md")]
pub struct SomeStruct;

pub fn main() {
    const INPUT_TXT: &'static str = include_str!("input.txt");
    const INPUT_BIN: &'static [u8] = include_bytes!("input.bin");

    println!("{}", INPUT_TXT);
    println!("{:?}", INPUT_BIN);
}


