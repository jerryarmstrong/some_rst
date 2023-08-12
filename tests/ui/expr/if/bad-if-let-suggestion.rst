tests/ui/expr/if/bad-if-let-suggestion.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // FIXME(compiler-errors): This really should suggest `let` on the RHS of the
// `&&` operator, but that's kinda hard to do because of precedence.
// Instead, for now we just make sure not to suggest `if let let`.
fn a() {
    if let x = 1 && i = 2 {}
    //~^ ERROR cannot find value `i` in this scope
    //~| ERROR `let` expressions in this position are unstable
    //~| ERROR mismatched types
    //~| ERROR `let` expressions are not supported here
}

fn b() {
    if (i + j) = i {}
    //~^ ERROR cannot find value `i` in this scope
    //~| ERROR cannot find value `i` in this scope
    //~| ERROR cannot find value `j` in this scope
}

fn c() {
    if x[0] = 1 {}
    //~^ ERROR cannot find value `x` in this scope
}

fn main() {}


