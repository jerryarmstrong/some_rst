tests/ui/underscore-lifetime/underscore-lifetime-elison-mismatch.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x: &mut Vec<&'_ u8>, y: &'_ u8) { x.push(y); }
//~^ ERROR lifetime may not live long enough

fn main() {}


