compiler/rustc_builtin_macros/src/derive.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::cfg_eval::cfg_eval;

use rustc_ast as ast;
use rustc_ast::{GenericParamKind, ItemKind, MetaItemKind, NestedMetaItem, StmtKind};
use rustc_errors::{struct_span_err, Applicability};
use rustc_expand::base::{Annotatable, ExpandResult, ExtCtxt, Indeterminate, MultiItemModifier};
use rustc_feature::AttributeTemplate;
use rustc_parse::validate_attr;
use rustc_session::Session;
use rustc_span::symbol::{sym, Ident};
use rustc_span::Span;

pub(crate) struct Expander(pub bool);

impl MultiItemModifier for Expander {
    fn expand(
        &self,
        ecx: &mut ExtCtxt<'_>,
        span: Span,
        meta_item: &ast::MetaItem,
        item: Annotatable,
        _: bool,
    ) -> ExpandResult<Vec<Annotatable>, Annotatable> {
        let sess = ecx.sess;
        if report_bad_target(sess, &item, span) {
            // We don't want to pass inappropriate targets to derive macros to avoid
            // follow up errors, all other errors below are recoverable.
            return ExpandResult::Ready(vec![item]);
        }

        let (sess, features) = (ecx.sess, ecx.ecfg.features);
        let result =
            ecx.resolver.resolve_derives(ecx.current_expansion.id, ecx.force_mode, &|| {
                let template =
                    AttributeTemplate { list: Some("Trait1, Trait2, ..."), ..Default::default() };
                validate_attr::check_builtin_meta_item(
                    &sess.parse_sess,
                    &meta_item,
                    ast::AttrStyle::Outer,
                    sym::derive,
                    template,
                );

                let mut resolutions = match &meta_item.kind {
                    MetaItemKind::List(list) => {
                        list.iter()
                            .filter_map(|nested_meta| match nested_meta {
                                NestedMetaItem::MetaItem(meta) => Some(meta),
                                NestedMetaItem::Lit(lit) => {
                                    // Reject `#[derive("Debug")]`.
                                    report_unexpected_meta_item_lit(sess, &lit);
                                    None
                                }
                            })
                            .map(|meta| {
                                // Reject `#[derive(Debug = "value", Debug(abc))]`, but recover the
                                // paths.
                                report_path_args(sess, &meta);
                                meta.path.clone()
                            })
                            .map(|path| (path, dummy_annotatable(), None, self.0))
                            .collect()
                    }
                    _ => vec![],
                };

                // Do not configure or clone items unless necessary.
                match &mut resolutions[..] {
                    [] => {}
                    [(_, first_item, ..), others @ ..] => {
                        *first_item = cfg_eval(
                            sess,
                            features,
                            item.clone(),
                            ecx.current_expansion.lint_node_id,
                        );
                        for (_, item, _, _) in others {
                            *item = first_item.clone();
                        }
                    }
                }

                resolutions
            });

        match result {
            Ok(()) => ExpandResult::Ready(vec![item]),
            Err(Indeterminate) => ExpandResult::Retry(item),
        }
    }
}

// The cheapest `Annotatable` to construct.
fn dummy_annotatable() -> Annotatable {
    Annotatable::GenericParam(ast::GenericParam {
        id: ast::DUMMY_NODE_ID,
        ident: Ident::empty(),
        attrs: Default::default(),
        bounds: Default::default(),
        is_placeholder: false,
        kind: GenericParamKind::Lifetime,
        colon_span: None,
    })
}

fn report_bad_target(sess: &Session, item: &Annotatable, span: Span) -> bool {
    let item_kind = match item {
        Annotatable::Item(item) => Some(&item.kind),
        Annotatable::Stmt(stmt) => match &stmt.kind {
            StmtKind::Item(item) => Some(&item.kind),
            _ => None,
        },
        _ => None,
    };

    let bad_target =
        !matches!(item_kind, Some(ItemKind::Struct(..) | ItemKind::Enum(..) | ItemKind::Union(..)));
    if bad_target {
        struct_span_err!(
            sess,
            span,
            E0774,
            "`derive` may only be applied to `struct`s, `enum`s and `union`s",
        )
        .span_label(span, "not applicable here")
        .span_label(item.span(), "not a `struct`, `enum` or `union`")
        .emit();
    }
    bad_target
}

fn report_unexpected_meta_item_lit(sess: &Session, lit: &ast::MetaItemLit) {
    let help_msg = match lit.kind {
        ast::LitKind::Str(_, ast::StrStyle::Cooked)
            if rustc_lexer::is_ident(lit.symbol.as_str()) =>
        {
            format!("try using `#[derive({})]`", lit.symbol)
        }
        _ => "for example, write `#[derive(Debug)]` for `Debug`".to_string(),
    };
    struct_span_err!(sess, lit.span, E0777, "expected path to a trait, found literal",)
        .span_label(lit.span, "not a trait")
        .help(&help_msg)
        .emit();
}

fn report_path_args(sess: &Session, meta: &ast::MetaItem) {
    let report_error = |title, action| {
        let span = meta.span.with_lo(meta.path.span.hi());
        sess.struct_span_err(span, title)
            .span_suggestion(span, action, "", Applicability::MachineApplicable)
            .emit();
    };
    match meta.kind {
        MetaItemKind::Word => {}
        MetaItemKind::List(..) => report_error(
            "traits in `#[derive(...)]` don't accept arguments",
            "remove the arguments",
        ),
        MetaItemKind::NameValue(..) => {
            report_error("traits in `#[derive(...)]` don't accept values", "remove the value")
        }
    }
}


