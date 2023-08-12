tests/run-make/incr-foreign-head-span/second_crate.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate first_crate;
use first_crate::OtherTrait;

#[cfg(not(second_run))]
trait Foo: OtherTrait {}

#[cfg(second_run)]
trait Bar: OtherTrait {}


