src/tools/rustfmt/tests/source/issue-5270/merge_derives_true.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-merge_derives:true

#[rustfmt::skip::attributes(derive)]
#[allow(dead_code)]
#[derive(StructField)]
#[derive(Clone)]
struct DoNotMergeDerives {
    field: String,
}

#[allow(dead_code)]
#[derive(StructField)]
#[rustfmt::skip::attributes(derive)]
#[derive(Clone)]
struct DoNotMergeDerivesSkipInMiddle {
    field: String,
}

#[allow(dead_code)]
#[derive(StructField)]
#[derive(Clone)]
#[rustfmt::skip::attributes(derive)]
struct DoNotMergeDerivesSkipAtEnd {
    field: String,
}

#[allow(dead_code)]
#[derive(StructField)]
#[derive(Clone)]
struct MergeDerives {
    field: String,
}

mod inner_attribute_derive_skip {
    #![rustfmt::skip::attributes(derive)]

    #[allow(dead_code)]
    #[derive(StructField)]
    #[derive(Clone)]
    struct DoNotMergeDerives {
        field: String,
    }
}

#[rustfmt::skip::attributes(derive)]
mod outer_attribute_derive_skip {
    #[allow(dead_code)]
    #[derive(StructField)]
    #[derive(Clone)]
    struct DoNotMergeDerives {
        field: String,
    }
}

mod no_derive_skip {
    #[allow(dead_code)]
    #[derive(StructField)]
    #[derive(Clone)]
    struct MergeDerives {
        field: String,
    }
}


