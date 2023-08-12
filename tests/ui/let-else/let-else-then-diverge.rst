tests/ui/let-else/let-else-then-diverge.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // popped up in #94012, where an alternative desugaring was
// causing unreachable code errors

#![deny(unused_variables)]
#![deny(unreachable_code)]

fn let_else_diverge() -> bool {
    let Some(_) = Some("test") else {
        let x = 5; //~ ERROR unused variable: `x`
        return false;
    };
    return true;
}

fn main() {
    let_else_diverge();
}


