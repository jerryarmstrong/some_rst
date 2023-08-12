src/tools/rustfmt/config_proc_macro/tests/smoke.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod config {
    pub trait ConfigType: Sized {
        fn doc_hint() -> String;
    }
}

#[allow(dead_code)]
#[allow(unused_imports)]
mod tests {
    use rustfmt_config_proc_macro::config_type;

    #[config_type]
    enum Bar {
        Foo,
        Bar,
        #[doc_hint = "foo_bar"]
        FooBar,
        FooFoo(i32),
    }
}


