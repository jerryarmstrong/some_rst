tests/ui/liveness/liveness-forgot-ret.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn god_exists(a: isize) -> bool { return god_exists(a); }

fn f(a: isize) -> isize { if god_exists(a) { return 5; }; }
//~^ ERROR mismatched types

fn main() { f(12); }


