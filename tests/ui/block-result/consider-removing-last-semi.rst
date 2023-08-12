tests/ui/block-result/consider-removing-last-semi.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

pub fn f() -> String {  //~ ERROR mismatched types
    0u8;
    "bla".to_string();
}

pub fn g() -> String {  //~ ERROR mismatched types
    "this won't work".to_string();
    "removeme".to_string();
}

pub fn macro_tests() -> u32 {  //~ ERROR mismatched types
    macro_rules! mac {
        () => (1);
    }
    mac!();
}

fn main() {}


