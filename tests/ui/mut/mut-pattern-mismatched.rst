tests/ui/mut/mut-pattern-mismatched.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let foo = &mut 1;

    // (separate lines to ensure the spans are accurate)

     let &_ //~  ERROR mismatched types
            //~| expected mutable reference `&mut {integer}`
            //~| found reference `&_`
            //~| types differ in mutability
        = foo;
    let &mut _ = foo;

    let bar = &1;
    let &_ = bar;
    let &mut _ //~  ERROR mismatched types
               //~| expected reference `&{integer}`
               //~| found mutable reference `&mut _`
               //~| types differ in mutability
         = bar;
}


