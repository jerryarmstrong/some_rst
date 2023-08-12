tests/ui/rfcs/rfc-2005-default-binding-mode/enum.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
enum Wrapper {
    Wrap(i32),
}

use Wrapper::Wrap;

pub fn main() {
    let Wrap(x) = &Wrap(3);
    println!("{}", *x);

    let Wrap(x) = &mut Wrap(3);
    println!("{}", *x);

    if let Some(x) = &Some(3) {
        println!("{}", *x);
    } else {
        panic!();
    }

    if let Some(x) = &mut Some(3) {
        println!("{}", *x);
    } else {
        panic!();
    }

    if let Some(x) = &mut Some(3) {
        *x += 1;
    } else {
        panic!();
    }

    while let Some(x) = &Some(3) {
        println!("{}", *x);
        break;
    }
    while let Some(x) = &mut Some(3) {
        println!("{}", *x);
        break;
    }
    while let Some(x) = &mut Some(3) {
        *x += 1;
        break;
    }
}


