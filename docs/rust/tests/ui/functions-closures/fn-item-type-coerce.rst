tests/ui/functions-closures/fn-item-type-coerce.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
// Test implicit coercions from a fn item type to a fn pointer type.

// pretty-expanded FIXME #23616

fn foo(x: isize) -> isize { x * 2 }
fn bar(x: isize) -> isize { x * 4 }
type IntMap = fn(isize) -> isize;

fn eq<T>(x: T, y: T) { }

fn main() {
    let f: IntMap = foo;

    eq::<IntMap>(foo, bar);
}


