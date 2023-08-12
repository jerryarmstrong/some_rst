tests/ui/moves/move-arg.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn test(foo: isize) { assert_eq!(foo, 10); }

pub fn main() { let x = 10; test(x); }


