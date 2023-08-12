tests/ui/static/issue-5216.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() { }
struct S(Box<dyn FnMut() + Sync>);
pub static C: S = S(f); //~ ERROR mismatched types


fn g() { }
type T = Box<dyn FnMut() + Sync>;
pub static D: T = g; //~ ERROR mismatched types

fn main() {}


