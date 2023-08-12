src/tools/rustfmt/tests/target/issue-3665/sub_mod.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[rustfmt::skip::attributes(more_skip)]
#[more_skip(should,
      skip,
this,                               format)]
fn foo() {}

#[skip_mod_attr(should, skip,
this,                               format,in,                    master,
                    and, sub, module)]
fn bar() {}

#[skip_attr(should, not, skip, this, attribute, here)]
fn baz() {}


