tests/ui/lint/unused/unused-doc-comments-edge-cases.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_doc_comments)]

fn doc_comment_on_match_arms(num: u8) -> bool {
    match num {
        3 => true,
        /// useless doc comment
        //~^ ERROR: unused doc comment
        _ => false,
    }
}

fn doc_comment_between_if_else(num: u8) -> bool {
    if num == 3 {
        true //~ ERROR: mismatched types
    }
    /// useless doc comment
    else { //~ ERROR: expected expression, found keyword `else`
        false
    }
}

fn doc_comment_on_expr(num: u8) -> bool {
    /// useless doc comment
    //~^ ERROR: attributes on expressions are experimental
    //~| ERROR: unused doc comment
    num == 3
}

fn doc_comment_on_generic<#[doc = "x"] T>(val: T) {}
//~^ ERROR: unused doc comment

fn doc_comment_on_block() {
    /// unused doc comment
    //~^ ERROR: unused doc comment
    {
        let x = 12;
    }
}

/// unused doc comment
//~^ ERROR: unused doc comment
extern "C" {
    fn foo();
}

fn main() {}


