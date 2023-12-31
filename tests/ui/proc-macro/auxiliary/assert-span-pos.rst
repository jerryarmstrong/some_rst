tests/ui/proc-macro/auxiliary/assert-span-pos.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // force-host
// no-prefer-dynamic

#![feature(proc_macro_diagnostic, proc_macro_span)]
#![crate_type = "proc-macro"]

extern crate proc_macro;

use proc_macro::{TokenStream, TokenTree, Span};

fn lit_span(tt: TokenTree) -> (Span, String) {
    match tt {
        TokenTree::Literal(..) |
        TokenTree::Group(..) => (tt.span(), tt.to_string().trim().into()),
        _ => panic!("expected a literal in token tree, got: {:?}", tt)
    }
}

#[proc_macro]
pub fn assert_span_pos(input: TokenStream) -> TokenStream {
    let mut tokens = input.into_iter();
    let (sp1, str1) = lit_span(tokens.next().expect("first argument"));
    let _ = tokens.next();
    let (_sp2, str2) = lit_span(tokens.next().expect("second argument"));

    let line: usize = str1.parse().unwrap();
    let col: usize = str2.parse().unwrap();

    let sp1s = sp1.start();
    if (line, col) != (sp1s.line, sp1s.column) {
        let msg = format!("line/column mismatch: ({}, {}) != ({}, {})", line, col,
            sp1s.line, sp1s.column);
        sp1.error(msg).emit();
    }

    "".parse().unwrap()
}


