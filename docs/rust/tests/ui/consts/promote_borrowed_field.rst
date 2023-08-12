tests/ui/consts/promote_borrowed_field.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// From https://github.com/rust-lang/rust/issues/65727

const _: &i32 = {
    let x = &(5, false).0;
    x
};

fn main() {
    let _: &'static i32 = &(5, false).0;
}


