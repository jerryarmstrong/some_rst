tests/ui/macros/macro-followed-by-seq.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_macros)]
// Regression test for issue #25436: check that things which can be
// followed by any token also permit X* to come afterwards.

macro_rules! foo {
  ( $a:tt $($b:tt)* ) => { };
  ( $a:ident $($b:tt)* ) => { };
  ( $a:item $($b:tt)* ) => { };
  ( $a:block $($b:tt)* ) => { };
  ( $a:meta $($b:tt)* ) => { }
}

fn main() { }


