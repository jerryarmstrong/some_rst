tests/ui/parser/keyword-box-as-identifier.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let box = 0;
    //~^ ERROR expected pattern, found `=`
    let box: bool;
    //~^ ERROR expected pattern, found `:`
    let mut box = 0;
    //~^ ERROR expected pattern, found `=`
    let (box,) = (0,);
    //~^ ERROR expected pattern, found `,`
}


