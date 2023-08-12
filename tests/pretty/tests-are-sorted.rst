tests/pretty/tests-are-sorted.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-type=lib --test
// pretty-compare-only
// pretty-mode:expanded
// pp-exact:tests-are-sorted.pp

#[test]
fn m_test() {}

#[test]
fn z_test() {}

#[test]
fn a_test() {}


