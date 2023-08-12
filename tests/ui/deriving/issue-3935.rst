tests/ui/deriving/issue-3935.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(PartialEq)]
struct Bike {
    name: String,
}

pub fn main() {
    let town_bike = Bike { name: "schwinn".to_string() };
    let my_bike = Bike { name: "surly".to_string() };

    assert!(town_bike != my_bike);
}


