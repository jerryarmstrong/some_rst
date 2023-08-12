tests/ui/span/borrowck-ref-into-rvalue.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {
    let msg;
    match Some("Hello".to_string()) {
        //~^ ERROR temporary value dropped while borrowed
        Some(ref m) => {
            msg = m;
        },
        None => { panic!() }
    }
    println!("{}", *msg);
}


