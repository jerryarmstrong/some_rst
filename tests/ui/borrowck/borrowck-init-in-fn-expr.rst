tests/ui/borrowck/borrowck-init-in-fn-expr.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let f  = || -> isize {
        let i: isize;
        i //~ ERROR E0381
    };
    println!("{}", f());
}


