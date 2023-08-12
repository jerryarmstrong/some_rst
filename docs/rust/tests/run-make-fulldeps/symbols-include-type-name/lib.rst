tests/run-make-fulldeps/symbols-include-type-name/lib.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Def {
    pub id: i32,
}

impl Def {
    pub fn new(id: i32) -> Def {
        Def { id: id }
    }
}

#[no_mangle]
pub fn user() {
    let _ = Def::new(0);
}


