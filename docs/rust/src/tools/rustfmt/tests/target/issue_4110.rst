src/tools/rustfmt/tests/target/issue_4110.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn bindings() {
    let err = match (place_desc, explanation) {
        (
            Some(ref name),
            BorrowExplanation::MustBeValidFor {
                category:
                    category @ (ConstraintCategory::Return
                    | ConstraintCategory::CallArgument
                    | ConstraintCategory::OpaqueType),
                from_closure: false,
                ref region_name,
                span,
                ..
            },
        ) if borrow_spans.for_generator() | borrow_spans.for_closure() => self
            .report_escaping_closure_capture(
                borrow_spans,
                borrow_span,
                region_name,
                category,
                span,
                &format!("`{}`", name),
                "function",
            ),
        (
            ref name,
            BorrowExplanation::MustBeValidFor {
                category: ConstraintCategory::Assignment,
                from_closure: false,
                region_name:
                    RegionName {
                        source: RegionNameSource::AnonRegionFromUpvar(upvar_span, ref upvar_name),
                        ..
                    },
                span,
                ..
            },
        ) => self.report_escaping_data(borrow_span, name, upvar_span, upvar_name, span),
        (Some(name), explanation) => self.report_local_value_does_not_live_long_enough(
            location,
            &name,
            &borrow,
            drop_span,
            borrow_spans,
            explanation,
        ),
        (None, explanation) => self.report_temporary_value_does_not_live_long_enough(
            location,
            &borrow,
            drop_span,
            borrow_spans,
            proper_span,
            explanation,
        ),
    };
}


