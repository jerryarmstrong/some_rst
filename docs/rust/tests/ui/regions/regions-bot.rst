tests/ui/regions/regions-bot.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// A very limited test of the "bottom" region


fn produce_static<T>() -> &'static T { panic!(); }

fn foo<T>(_x: &T) -> &usize { produce_static() }

pub fn main() {
}


