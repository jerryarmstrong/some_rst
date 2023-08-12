tests/ui/expr/if/if-ret.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_parens)]
// pretty-expanded FIXME #23616

fn foo() { if (return) { } } //~ WARNING unreachable block in `if`

pub fn main() { foo(); }


