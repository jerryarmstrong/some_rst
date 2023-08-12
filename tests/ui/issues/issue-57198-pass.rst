tests/ui/issues/issue-57198-pass.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

mod m {
    pub fn r#for() {}
}

fn main() {
    m::r#for();
}


