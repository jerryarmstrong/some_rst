tests/ui/span/range-2.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test range syntax - borrow errors.
#![feature(rustc_attrs)]
pub fn main() { #![rustc_error] // rust-lang/rust#49855
    let r = {
        let a = 42;
        let b = 42;
        &a..&b
    };
    //~^^ ERROR `a` does not live long enough
    //~| ERROR `b` does not live long enough
    r.use_ref();
}

trait Fake { fn use_mut(&mut self) { } fn use_ref(&self) { }  }
impl<T> Fake for T { }


