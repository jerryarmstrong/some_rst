tests/ui/deprecation/issue-66340-deprecated-attr-non-meta-grammar.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // The original problem in #66340 was that `find_deprecation_generic`
// called `attr.meta().unwrap()` under the assumption that the attribute
// was a well-formed `MetaItem`.

fn main() {
    foo()
}

#[deprecated(note = test)]
//~^ ERROR expected unsuffixed literal or identifier, found `test`
fn foo() {}


