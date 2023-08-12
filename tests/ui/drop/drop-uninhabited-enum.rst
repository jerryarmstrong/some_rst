tests/ui/drop/drop-uninhabited-enum.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_variables)]
// pretty-expanded FIXME #23616

enum Foo { }

impl Drop for Foo {
    fn drop(&mut self) { }
}

fn foo(x: Foo) { }

fn main() { }


