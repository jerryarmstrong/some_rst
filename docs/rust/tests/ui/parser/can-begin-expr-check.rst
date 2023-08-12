tests/ui/parser/can-begin-expr-check.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {

    return;
    return ();
    return as ();
    return return as ();
    return return return;

    return if true {
        ()
    } else {
        ()
    };

    loop {
        return break as ();
    }

    return enum; //~ ERROR expected one of `;`, `}`, or an operator, found keyword `enum`
}


