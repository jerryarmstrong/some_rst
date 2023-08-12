tests/ui/issues/issue-70724-add_type_neq_err_label-unwrap.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a() -> i32 {
    3
}

pub fn main() {
    assert_eq!(a, 0);
    //~^ ERROR binary operation `==` cannot
    //~| ERROR mismatched types
    //~| ERROR doesn't implement
}


