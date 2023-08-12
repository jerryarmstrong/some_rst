tests/ui/lint/expansion-time.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#[warn(meta_variable_misuse)]
macro_rules! foo {
    ( $($i:ident)* ) => { $($i)+ }; //~ WARN meta-variable repeats with different Kleene operator
}

#[warn(missing_fragment_specifier)]
macro_rules! m { ($i) => {} } //~ WARN missing fragment specifier
                              //~| WARN this was previously accepted

#[warn(soft_unstable)]
mod benches {
    #[bench] //~ WARN use of unstable library feature 'test'
             //~| WARN this was previously accepted
    fn foo() {}
}

#[deprecated = "reason"]
macro_rules! deprecated {
    () => {}
}

#[allow(deprecated)]
mod deprecated {
    deprecated!(); // No warning
}

#[warn(incomplete_include)]
fn main() {
    // WARN see in the stderr file, the warning points to the included file.
    include!("expansion-time-include.rs");
}


