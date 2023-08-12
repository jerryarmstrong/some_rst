tests/ui-fulldeps/outlive-expansion-phase.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:outlive-expansion-phase.rs
// ignore-stage1

#![feature(plugin)]
#![plugin(outlive_expansion_phase)] //~ WARNING compiler plugins are deprecated

pub fn main() {}


