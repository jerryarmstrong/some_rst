tests/ui/parser/expr-as-stmt-2.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This is not autofixable because we give extra suggestions to end the first expression with `;`.
fn foo(a: Option<u32>, b: Option<u32>) -> bool {
    if let Some(x) = a { true } else { false }
    //~^ ERROR mismatched types
    //~| ERROR mismatched types
    && //~ ERROR mismatched types
    if let Some(y) = a { true } else { false }
}

fn main() {}


