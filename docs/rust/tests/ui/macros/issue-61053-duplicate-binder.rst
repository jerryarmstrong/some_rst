tests/ui/macros/issue-61053-duplicate-binder.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(meta_variable_misuse)]

macro_rules! foo {
    () => {};
    (error) => {
        macro_rules! bar {
            ($x:tt $x:tt) => { $x }; //~ ERROR duplicate matcher binding
        }
    };
}

fn main() {
    foo!();
}


