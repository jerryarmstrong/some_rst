tests/ui/issues/issue-3895.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

pub fn main() {
    enum State { BadChar, BadSyntax }

    match State::BadChar {
        _ if true => State::BadChar,
        State::BadChar | State::BadSyntax => panic!() ,
    };
}


