tests/ui/liveness/liveness-closure-require-ret.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn force<F>(f: F) -> isize where F: FnOnce() -> isize { f() }
fn main() { println!("{}", force(|| {})); } //~ ERROR mismatched types


