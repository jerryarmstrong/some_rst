tests/ui/occurs-check-3.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // From Issue #778

enum Clam<T> { A(T) }
fn main() { let c; c = Clam::A(c); match c { Clam::A::<isize>(_) => { } } }
//~^ ERROR mismatched types


