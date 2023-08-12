tests/ui/borrowck/issue-104639-lifetime-order.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// check-pass

#![allow(dead_code)]
async fn fail<'a, 'b, 'c>(_: &'static str) where 'a: 'c, 'b: 'c, {}
async fn pass<'a, 'c, 'b>(_: &'static str) where 'a: 'c, 'b: 'c, {}
async fn pass2<'a, 'b, 'c>(_: &'static str) where 'a: 'c, 'b: 'c, 'c: 'a, {}
async fn pass3<'a, 'b, 'c>(_: &'static str) where 'a: 'b, 'b: 'c, 'c: 'a, {}

fn main() { }


