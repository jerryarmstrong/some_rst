tests/ui/functions-closures/fn-lval.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass



// pretty-expanded FIXME #23616

fn foo(_f: fn(isize) -> isize) { }

fn id(x: isize) -> isize { return x; }

pub fn main() { foo(id); }


