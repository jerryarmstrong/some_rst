tests/ui/macros/macro-pat-pattern-followed-by-or.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_macros)]
macro_rules! foo { ($x:pat | $y:pat) => {} } // should be ok
macro_rules! bar { ($($x:pat)+ | $($y:pat)+) => {} } // should be ok
macro_rules! qux { ($x:pat, $y:pat) => {} } // should be ok
macro_rules! match_any {
    ( $expr:expr , $( $( $pat:pat )|+ => $expr_arm:expr ),+ ) => { // should be ok
        match $expr {
            $(
                $( $pat => $expr_arm, )+
            )+
        }
    };
}

fn main() {
    let result: Result<i64, i32> = Err(42);
    let int: i64 = match_any!(result, Ok(i) | Err(i) => i.into());
    assert_eq!(int, 42);
}


