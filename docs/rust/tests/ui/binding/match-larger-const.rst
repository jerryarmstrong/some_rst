tests/ui/binding/match-larger-const.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#[derive(Eq, PartialEq)]
pub struct Data([u8; 4]);

const DATA: Data = Data([1, 2, 3, 4]);

fn main() {
    match DATA {
        DATA => (),
        _ => (),
    }
}


