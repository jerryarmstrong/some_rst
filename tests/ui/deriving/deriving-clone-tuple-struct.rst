tests/ui/deriving/deriving-clone-tuple-struct.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#![allow(dead_code)]

#[derive(Clone)]
struct S((), ());

pub fn main() {}


