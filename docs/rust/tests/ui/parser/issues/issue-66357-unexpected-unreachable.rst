tests/ui/parser/issues/issue-66357-unexpected-unreachable.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // The problem in #66357 was that the call trace:
//
// - parse_fn_block_decl
// - expect_or
// - unexpected
// - expect_one_of
// - expected_one_of_not_found
// - recover_closing_delimiter
//
// ended up bubbling up `Ok(true)` to `unexpected` which then used `unreachable!()`.

fn f() { |[](* }
//~^ ERROR expected one of `,` or `:`, found `(`
//~| ERROR expected one of `&`, `(`, `)`, `-`, `...`, `..=`, `..`, `[`, `_`, `box`, `mut`, `ref`, `|`, identifier, or path, found `*`


