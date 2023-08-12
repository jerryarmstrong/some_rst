tests/ui/fmt/format-args-capture-issue-102057.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    format!("\x7Ba}");
    //~^ ERROR cannot find value `a` in this scope
    format!("\x7Ba\x7D");
    //~^ ERROR cannot find value `a` in this scope

    let a = 0;

    format!("\x7Ba} {b}");
    //~^ ERROR cannot find value `b` in this scope
    format!("\x7Ba\x7D {b}");
    //~^ ERROR cannot find value `b` in this scope
    format!("\x7Ba} \x7Bb}");
    //~^ ERROR cannot find value `b` in this scope
    format!("\x7Ba\x7D \x7Bb}");
    //~^ ERROR cannot find value `b` in this scope
    format!("\x7Ba\x7D \x7Bb\x7D");
    //~^ ERROR cannot find value `b` in this scope
}


