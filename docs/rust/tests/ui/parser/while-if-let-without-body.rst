tests/ui/parser/while-if-let-without-body.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let container = vec![Some(1), Some(2), None];

    let mut i = 0;
    while if let Some(thing) = container.get(i) {
        //~^ NOTE while parsing the body of this `while` expression
        //~| NOTE this `while` condition successfully parsed
        println!("{:?}", thing);
        i += 1;
    }
}
//~^ ERROR expected `{`, found `}`
//~| NOTE expected `{`


