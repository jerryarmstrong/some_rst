src/tools/rustfmt/tests/target/issue-3709.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-edition: 2018

macro_rules! token {
    ($t:tt) => {};
}

fn main() {
    token!(dyn);
    token!(dyn);
}


