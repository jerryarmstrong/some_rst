tests/ui/traits/syntax-polarity.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

#![feature(negative_impls)]

struct TestType;

impl TestType {}

trait TestTrait {}

impl !Send for TestType {}

struct TestType2<T>(T);

impl<T> TestType2<T> {}

impl<T> !Send for TestType2<T> {}

fn main() {}


