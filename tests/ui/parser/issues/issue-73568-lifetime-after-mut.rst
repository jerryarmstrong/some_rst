tests/ui/parser/issues/issue-73568-lifetime-after-mut.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]
fn x<'a>(x: &mut 'a i32){} //~ ERROR lifetime must precede `mut`

macro_rules! mac {
    ($lt:lifetime) => {
        fn w<$lt>(w: &mut $lt i32) {}
        //~^ ERROR lifetime must precede `mut`
    }
}

mac!('a);

// avoid false positives
fn y<'a>(y: &mut 'a + Send) {
    //~^ ERROR expected a path on the left-hand side of `+`, not `&mut 'a`
    //~| ERROR at least one trait is required for an object type
    let z = y as &mut 'a + Send;
    //~^ ERROR expected value, found trait `Send`
}


