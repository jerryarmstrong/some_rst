src/tools/rustfmt/src/parse/macros/asm.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use rustc_ast::ast;
use rustc_builtin_macros::asm::{parse_asm_args, AsmArgs};

use crate::rewrite::RewriteContext;

#[allow(dead_code)]
pub(crate) fn parse_asm(context: &RewriteContext<'_>, mac: &ast::MacCall) -> Option<AsmArgs> {
    let ts = mac.args.tokens.clone();
    let mut parser = super::build_parser(context, ts);
    parse_asm_args(&mut parser, context.parse_sess.inner(), mac.span(), false).ok()
}


