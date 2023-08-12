tests/ui/borrowck/borrowck-init-in-called-fn-expr.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let j = || -> isize {
        let i: isize;
        i //~ ERROR E0381
    };
    j();
}


