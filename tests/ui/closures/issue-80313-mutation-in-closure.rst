tests/ui/closures/issue-80313-mutation-in-closure.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut my_var = false;
    let callback = || {
        my_var = true;
    };
    callback(); //~ ERROR E0596
}


