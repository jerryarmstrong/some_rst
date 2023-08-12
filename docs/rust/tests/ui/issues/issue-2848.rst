tests/ui/issues/issue-2848.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(non_camel_case_types)]

mod bar {
    pub enum foo {
        alpha,
        beta,
        charlie
    }
}

fn main() {
    use bar::foo::{alpha, charlie};
    match alpha {
      alpha | beta => {} //~  ERROR variable `beta` is not bound in all patterns
      charlie => {}
    }
}


