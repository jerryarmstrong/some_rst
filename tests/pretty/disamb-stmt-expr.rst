tests/pretty/disamb-stmt-expr.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact

// Here we check that the parentheses around the body of `wsucc()` are
// preserved.  They are needed to disambiguate `{return n+1}; - 0` from
// `({return n+1}-0)`.

fn id<F>(f: F) -> isize where F: Fn() -> isize { f() }

fn wsucc(_n: isize) -> isize { id(|| { 1 }) - 0 }
fn main() {}


