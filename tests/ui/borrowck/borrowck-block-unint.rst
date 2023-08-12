tests/ui/borrowck/borrowck-block-unint.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn force<F>(f: F) where F: FnOnce() { f(); }
fn main() {
    let x: isize;
    force(|| {  //~ ERROR E0381
        println!("{}", x);
    });
}


