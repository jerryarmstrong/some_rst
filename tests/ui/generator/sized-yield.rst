tests/ui/generator/sized-yield.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators, generator_trait)]

use std::ops::Generator;
use std::pin::Pin;

fn main() {
   let s = String::from("foo");
   let mut gen = move || {
   //~^ ERROR the size for values of type
       yield s[..];
   };
   Pin::new(&mut gen).resume(());
   //~^ ERROR the size for values of type
}


