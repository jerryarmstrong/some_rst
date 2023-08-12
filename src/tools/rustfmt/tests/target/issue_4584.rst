src/tools/rustfmt/tests/target/issue_4584.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style: Visual

#[derive(Debug)]
pub enum Case {
    Upper,
    Lower,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum Case {
    Upper,
    Lower,
}

// NB - This formatting looks potentially off the desired state, but is
// consistent with current behavior. Included here to provide a line wrapped
// derive case with the changes applied to resolve issue #4584
#[derive(Add,
           Sub,
           Mul,
           Div,
           Clone,
           Copy,
           Eq,
           PartialEq,
           Ord,
           PartialOrd,
           Debug,
           Hash,
           Serialize,
           Mul)]
struct Foo {}


