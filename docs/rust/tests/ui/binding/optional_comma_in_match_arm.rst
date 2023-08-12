tests/ui/binding/optional_comma_in_match_arm.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_unsafe)]
// ignore-pretty issue #37199
#![allow(while_true)]

fn main() {
    let x = 1;

    match x {
        1 => loop { break; },
        2 => while true { break; },
        3 => if true { () },
        4 => if true { () } else { () },
        5 => match () { () => () },
        6 => { () },
        7 => unsafe { () },
        _ => (),
    }

    match x {
        1 => loop { break; }
        2 => while true { break; }
        3 => if true { () }
        4 => if true { () } else { () }
        5 => match () { () => () }
        6 => { () }
        7 => unsafe { () }
        _ => ()
    }

    let r: &i32 = &x;

    match r {
        // Absence of comma should not cause confusion between a pattern
        // and a bitwise and.
        &1 => if true { () } else { () }
        &2 => (),
        _ =>()
    }
}


